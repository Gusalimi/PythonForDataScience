from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Loads an image from a path and returns it as a numpy array"""
    if (not isinstance(path, str)):
        raise TypeError("path must be a string")
    if (not path.endswith(".jpg") and not path.endswith(".jpeg")
            and not path.endswith(".png")):
        raise ValueError("path must be a .png, .jpg or .jpeg file")
    try:
        img = Image.open(path)
    except FileNotFoundError:
        raise FileNotFoundError("path must be a valid path to a file")
    except PermissionError:
        raise PermissionError("path must be a valid path to a file")
    arr = np.array(img)
    return arr
