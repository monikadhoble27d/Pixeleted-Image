import os
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import math
def sobel_edge_detection(image):
    grayscale_image = ImageOps.grayscale(image)
    width, height = grayscale_image.size
    sobel_data = np.zeros((width, height), dtype=np.uint8)

    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_y = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            pixel_x = (
                (sobel_x[0][0] * grayscale_image.getpixel((x - 1, y - 1))) +
                (sobel_x[0][1] * grayscale_image.getpixel((x, y - 1))) +
                (sobel_x[0][2] * grayscale_image.getpixel((x + 1, y - 1))) +
                (sobel_x[1][0] * grayscale_image.getpixel((x - 1, y))) +
                (sobel_x[1][1] * grayscale_image.getpixel((x, y))) +
                (sobel_x[1][2] * grayscale_image.getpixel((x + 1, y))) +
                (sobel_x[2][0] * grayscale_image.getpixel((x - 1, y + 1))) +
                (sobel_x[2][1] * grayscale_image.getpixel((x, y + 1))) +
                (sobel_x[2][2] * grayscale_image.getpixel((x + 1, y + 1)))
            )

            pixel_y = (
                (sobel_y[0][0] * grayscale_image.getpixel((x - 1, y - 1))) +
                (sobel_y[0][1] * grayscale_image.getpixel((x, y - 1))) +
                (sobel_y[0][2] * grayscale_image.getpixel((x + 1, y - 1))) +
                (sobel_y[1][0] * grayscale_image.getpixel((x - 1, y))) +
                (sobel_y[1][1] * grayscale_image.getpixel((x, y))) +
                (sobel_y[1][2] * grayscale_image.getpixel((x + 1, y))) +
                (sobel_y[2][0] * grayscale_image.getpixel((x - 1, y + 1))) +
                (sobel_y[2][1] * grayscale_image.getpixel((x, y + 1))) +
                (sobel_y[2][2] * grayscale_image.getpixel((x + 1, y + 1)))
            )

            magnitude = math.sqrt((pixel_x * pixel_x) + (pixel_y * pixel_y))
            clamped_magnitude = np.uint8(min(255, magnitude))

            sobel_data[x, y] = clamped_magnitude

    return sobel_data



def frequency_analysis(image):
    grayscale_image = ImageOps.grayscale(image)
    width, height = grayscale_image.size
    frequency_data = np.zeros((width, height), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            freq_value = (math.sin(x * 0.1) + math.cos(y * 0.1)) * 127 + 128
            frequency_data[x, y] = int(freq_value)

    frequency_result_path = os.path.join('media', 'frequency_result.png')
    frequency_image = Image.fromarray(frequency_data)
    frequency_image.save(frequency_result_path)

    return frequency_result_path

def local_binary_pattern(image):
    grayscale_image = ImageOps.grayscale(image)
    width, height = grayscale_image.size
    lbp_data = np.zeros((width, height), dtype=np.uint8)

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            binary_string = ''
            center = grayscale_image.getpixel((x, y))

            binary_string += '1' if grayscale_image.getpixel((x - 1, y - 1)) >= center else '0'
            binary_string += '1' if grayscale_image.getpixel((x, y - 1)) >= center else '0'
            binary_string += '1' if grayscale_image.getpixel((x + 1, y - 1)) >= center else '0'
            binary_string += '1' if grayscale_image.getpixel((x + 1, y)) >= center else '0'
            binary_string += '1' if grayscale_image.getpixel((x + 1, y + 1)) >= center else '0'
            binary_string += '1' if grayscale_image.getpixel((x, y + 1)) >= center else '0'
            binary_string += '1' if grayscale_image.getpixel((x - 1, y + 1)) >= center else '0'
            binary_string += '1' if grayscale_image.getpixel((x - 1, y)) >= center else '0'

            lbp_value = int(binary_string, 2)
            lbp_data[x, y] = lbp_value

    # Save the processed image
    lbp_result_path = os.path.join('media', 'lbp_result.png')
    lbp_image = Image.fromarray(lbp_data)
    lbp_image.save(lbp_result_path)

    return lbp_result_path

def wiener_filter(image):
    grayscale_image = ImageOps.grayscale(image)
    width, height = grayscale_image.size
    corrected_data = np.zeros((width, height), dtype=np.uint8)

    # Placeholder for the actual Wiener filter implementation
    # For now, this example will simply return the grayscale image data
    for x in range(width):
        for y in range(height):
            corrected_data[x, y] = grayscale_image.getpixel((x, y))

    wiener_result_path = os.path.join('media', 'wiener_result.png')
    wiener_image = Image.fromarray(corrected_data)
    wiener_image.save(wiener_result_path)

    return wiener_result_path
