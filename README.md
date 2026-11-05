# Project: Colour Translation Module

## Introduction

This project explores RGB colour combinations by sampling equally spaced coloured dots from a reference image and translating their colours into a Python list of RGB tuples.

RGB stands for Red, Green and Blue. Each colour is represented by three numerical values corresponding to the intensity of these colour channels. For example, pure red is represented as `(255, 0, 0)`, where red has its maximum intensity and green and blue have no intensity.

The project uses `Ready_for_wonder.png` as its reference image. The image contains 8 rows and 10 columns of equally spaced coloured dots, giving a total of 80 sampling positions.

## Requirements

- Python
- Pillow (PIL) library

## Process

### 1. Importing the Image Module

The first step is to import the `Image` class from the Pillow library:

```python
from PIL import Image
```

Pillow provides tools for opening, converting, inspecting and manipulating image files.

### 2. Preparing the Reference Image

If the original image uses a format that is not suitable for the intended workflow, it can first be opened and saved in another format.

For example, an AVIF image can be opened using Pillow and saved as a PNG file:

```python
img = Image.open("colorwonder.avif")
img.save("Ready_for_wonder.png")
```

This saves the image in PNG format. It is important to distinguish between the image's file format and its colour mode: saving as PNG changes the file format, while converting to RGB changes how the pixel colours are represented.

### 3. Opening and Converting the Image to RGB

In the main Python file, the converted image can be opened and its colour mode changed to RGB:

```python
image = Image.open("Ready_for_wonder.png").convert("RGB")
```

The `.convert("RGB")` method ensures that each pixel is represented using three colour channels:

- Red (R)
- Green (G)
- Blue (B)

Each channel has an intensity value ranging from 0 to 255.

### 4. Checking the Image Dimensions

The `image.size` attribute retrieves the image dimensions as a tuple containing its width and height.

```python
print("Image dimensions:", image.size)
```

For this reference image, the dimensions are `(3840, 3184)`, meaning 3840 pixels wide and 3184 pixels high.

Checking the dimensions helps establish the boundaries of the image and provides a reference for determining the sampling coordinates.

### 5. Establishing the Sampling Coordinates

The reference image contains equally spaced coloured dots. To retrieve their colours, a sampling grid must be established using starting coordinates and spacing values.

AI assistance was used to identify the initial X and Y sampling coordinates and estimate the spacing between consecutive colour dots in the reference image.

This helped establish a consistent sampling grid for extracting colour information from the image.

The coordinates serve two purposes:

- **Starting coordinates (`start_x` and `start_y`):** Identify the initial sampling position.
- **Spacing values (`spacing_x` and `spacing_y`):** Determine the horizontal and vertical intervals between subsequent sampling positions.

The implementation and interpretation of these coordinates were used to develop the Python colour-sampling process.

### 6. Sampling the Image Using Nested Loops

The image contains 8 rows and 10 columns of coloured dots, resulting in 80 sampling positions.

Nested loops are used to iterate through these positions:

```python
for row in range(8):
    for column in range(10):
        x_cor = start_x + column * spacing_x
        y_cor = start_y + row * spacing_y

        color = image.getpixel((x_cor, y_cor))

        print(f"Coordinates: ({x_cor}, {y_cor}) | RGB: {color}")
        translate_li.append(color)
```

The outer loop processes the 8 rows, while the inner loop processes the 10 columns within each row.

The `x_cor` and `y_cor` variables determine the horizontal and vertical pixel coordinates respectively. This resembles a Cartesian coordinate system, except that an image's Y-axis increases downwards rather than upwards.

At each sampling position, `image.getpixel()` retrieves the RGB values of the corresponding pixel.

The coordinates and retrieved RGB values are printed for inspection. Each RGB tuple is then appended to `translate_li`, gradually building a list of 80 sampled colours.

## Outcome

The sampling process produces a list containing 80 RGB tuples, representing the colours extracted from the reference image.

This list can subsequently be used as input for translating the sampled colours into a visual output.
