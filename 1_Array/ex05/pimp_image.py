import numpy as np
from PIL import Image


def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""
    arr = array ^ 255
    return (arr)


def ft_red(array) -> np.array:
    """Returns the red channel of the image received."""
    red_channel = array[:, :, 0]
    red_image = np.zeros_like(array)
    red_image[:, :, 0] = red_channel
    red_image = np.clip(red_image, 0, 255)
    return (red_image)


def ft_green(array) -> np.array:
    """Returns the green channel of the image received."""
    green_channel = array[:, :, 1]
    green_image = np.zeros_like(array)
    green_image[:, :, 1] = green_channel
    green_image = np.clip(green_image, 0, 255)
    return green_image


def ft_blue(array) -> np.array:
    """Returns the blue channel of the image received."""
    blue_channel = array[:, :, 2]
    blue_image = np.zeros_like(array)
    blue_image[:, :, 2] = blue_channel
    blue_image = np.clip(blue_image, 0, 255)
    return blue_image


def ft_grey(array) -> np.array:
    """Returns the grey channel of the image received"""
    arr = np.array(Image.fromarray(array).convert("L"))
    return (arr)
