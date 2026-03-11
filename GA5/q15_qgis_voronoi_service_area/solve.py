import geopandas as gpd
import numpy as np
from scipy.spatial import Voronoi
from shapely.geometry import Polygon
from shapely.ops import unary_union

# Convert infinite Voronoi regions to finite polygons
def voronoi_finite_polygons_2d(vor, radius=None):
    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")

    new_regions = []
    new_vertices = vor.vertices.tolist()

    center = vor.points.mean(axis=0)
    if radius is None:
        radius = np.ptp(vor.points, axis=0).max() * 2
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    for p1, region_index in enumerate(vor.point_region):
        vertices = vor.regions[region_index]

        if all(v >= 0 for v in vertices):
            new_regions.append(vertices)
            continue

        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]

        for p2, v1, v2 in ridges:
            if v2 < 0:
                v1, v2 = v2, v1
            if v1 >= 0:
                continue

            t = vor.points[p2] - vor.points[p1]
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])

            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius

            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())

        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:, 1] - c[1], vs[:, 0] - c[0])
        new_region = [v for _, v in sorted(zip(angles, new_region))]

        new_regions.append(new_region)

    return new_regions, np.asarray(new_vertices)


# Load points
gdf = gpd.read_file("q-geospatial-qgis-gap.geojson")

# Reproject to metric CRS
gdf = gdf.to_crs(epsg=3857)

# Extract coordinates
points = np.array([[geom.x, geom.y] for geom in gdf.geometry])

# Build Voronoi
vor = Voronoi(points)
regions, vertices = voronoi_finite_polygons_2d(vor)

# Clip to buffered bounding box (similar to QGIS buffer region idea)
minx, miny, maxx, maxy = gdf.total_bounds
dx = maxx - minx
dy = maxy - miny
buffer_x = dx * 0.1
buffer_y = dy * 0.1
bbox = Polygon([
    (minx - buffer_x, miny - buffer_y),
    (maxx + buffer_x, miny - buffer_y),
    (maxx + buffer_x, maxy + buffer_y),
    (minx - buffer_x, maxy + buffer_y)
])

polys = []
for region in regions:
    polygon = Polygon(vertices[region])
    polygon = polygon.intersection(bbox)
    polys.append(polygon)

vor_gdf = gpd.GeoDataFrame(geometry=polys, crs=gdf.crs)

# Area in km²
vor_gdf["area_km2"] = vor_gdf.geometry.area / 1_000_000

largest = vor_gdf["area_km2"].max()
print(round(largest, 2))
