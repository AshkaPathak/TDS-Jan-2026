from PIL import Image
import numpy as np

# (scrambled_row, scrambled_col) -> (original_row, original_col)
MAPPING = {
    (0,0):(2,1),(0,1):(1,1),(0,2):(4,1),(0,3):(0,3),(0,4):(0,1),
    (1,0):(1,4),(1,1):(2,0),(1,2):(2,4),(1,3):(4,2),(1,4):(2,2),
    (2,0):(0,0),(2,1):(3,2),(2,2):(4,3),(2,3):(3,0),(2,4):(3,4),
    (3,0):(1,0),(3,1):(2,3),(3,2):(3,3),(3,3):(4,4),(3,4):(0,2),
    (4,0):(3,1),(4,1):(1,2),(4,2):(1,3),(4,3):(0,4),(4,4):(4,0),
}

def main():

    img = Image.open("jigsaw.webp").convert("RGB")

    w, h = img.size
    tile_w, tile_h = w//5, h//5

    # reconstruct
    reconstructed = Image.new("RGB",(w,h))

    for (sr,sc),(orow,ocol) in MAPPING.items():

        tile = img.crop((
            sc*tile_w,
            sr*tile_h,
            (sc+1)*tile_w,
            (sr+1)*tile_h
        ))

        reconstructed.paste(tile,(ocol*tile_w,orow*tile_h))

    arr = np.array(reconstructed,dtype=np.float32)

    r = arr[:,:,0]
    g = arr[:,:,1]
    b = arr[:,:,2]

    # luminance grayscale
    gray_float = 0.2126*r + 0.7152*g + 0.0722*b

    # round-half-up
    gray = np.floor(gray_float + 0.5)

    gray = np.clip(gray,0,255).astype(np.uint8)

    # pseudo-RGB grayscale
    rgb_gray = np.stack([gray,gray,gray],axis=2)

    out = Image.fromarray(rgb_gray)

    out.save("reconstructed_grayscale.png")

    print("done")

if __name__=="__main__":
    main()
