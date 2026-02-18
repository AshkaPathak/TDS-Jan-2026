# GA2 — Q1: Lossless Image Compression (< 400 Bytes)

## Problem Summary

Download the provided image and compress it **losslessly** to a file size under **400 bytes**.

Lossless means:
- Every pixel must be identical to the original.
- No color changes.
- No resizing.
- No cropping.
- No visual degradation.

The compressed file must be strictly less than 400 bytes.

---

## Initial Observations

- Image dimensions: 500 × 500
- Flat background
- A few solid colored shapes
- `magick -format "%k"` revealed **27 unique colors**

This indicates:
- Low entropy
- Small color palette
- High compressibility
- Ideal candidate for palette-based or modern lossless compression

---

## Attempt 1: PNG Optimization (Failed to Go Below 400B)

### Step 1 — Convert to indexed PNG (lossless remap)

```bash
magick original.png -unique-colors palette.png
magick original.png +dither -remap palette.png PNG8:compressed.png
```

### Step 2 — Optimize PNG

```bash
oxipng -o 6 -Z --strip safe compressed.png
```

Result:
```
697 bytes
```

### Step 3 — Verify pixel equality

```bash
magick compare -metric AE original.png compressed.png null: 2>&1
```

Output:
```
0 (0)%
```

Meaning:
- Pixel identical
- Fully lossless

However, PNG structural overhead prevented size from going below 400 bytes.

---

## Key Insight

PNG has unavoidable structural overhead:

- IHDR chunk
- PLTE chunk
- IDAT chunk
- IEND chunk
- zlib compression container

For a 500×500 image, even palette PNG could not reach < 400 bytes.

Therefore, a different lossless format was required.

---

## Final Solution: Lossless WebP

WebP lossless uses:

- Better entropy coding
- Color caching
- More efficient small-palette encoding
- Lower structural overhead

### Step 1 — Convert to lossless WebP

```bash
brew install webp
cwebp -lossless -z 9 original.png -o compressed.webp
```

### Output

```
Lossless-ARGB compressed size: 268 bytes
Palette size: 27
```

Final size:
```
268 bytes
```

Which satisfies:
- Strictly less than 400 bytes
- Pixel-perfect identical

---

## Verification

Lossless WebP preserves exact pixel values.

To verify:

```bash
dwebp compressed.webp -ppm -o decompressed.ppm
magick compare -metric AE original.png decompressed.ppm null: 2>&1
```

Expected output:
```
0 (0)%
```

This confirms:
- No pixel differences
- Fully lossless compression

---

## Final File

Submitted file:
```
compressed.webp
Size: 268 bytes
```

---

## Why This Worked

The image had:
- Only 27 unique colors
- Large flat regions
- Very low entropy

WebP’s lossless compression outperformed PNG’s deflate-based compression due to:

- Better modeling of color reuse
- More efficient entropy coding
- Lower format overhead

PNG could not go below 697 bytes.
WebP reduced it to 268 bytes.

---

## GitHub Steps

```bash
mkdir -p GA2/q01_image_compression
mv original.png GA2/q01_image_compression/
mv compressed.webp GA2/q01_image_compression/

git add GA2/q01_image_compression
git commit -m "GA2 Q1: lossless image compression under 400 bytes using WebP"
git push
```

---

## Conclusion

The correct approach was not aggressive PNG brute forcing.

It required:
- Understanding image entropy
- Evaluating color count
- Recognizing PNG structural limitations
- Selecting a more efficient lossless format

Final Result:
✔ Lossless  
✔ Pixel-identical  
✔ 268 bytes  
✔ Accepted by portal  

