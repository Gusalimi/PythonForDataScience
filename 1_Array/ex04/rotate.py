import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load
from PIL import Image


def transpose_arr(arr: np.array) -> np.array:
    """Transpose a numpy array"""
    rows, cols = arr.shape
    new_arr = np.empty((cols, rows), dtype=arr.dtype)
    for i in range(rows):
        for j in range(cols):
            new_arr[j, i] = arr[i, j]
    return new_arr


def main():
    """Main function"""
    try:
        arr = ft_load("animal.jpeg")
    except Exception:
        print("Error opening animal.jpeg")
        return
    img = Image.fromarray(arr).convert("L").crop((450, 100, 850, 500))
    arr = np.array(img)[:, :, np.newaxis]
    print(f"The shape of image is: {arr.shape} or {arr[:, :, 0].shape}")
    print(arr)
    arr = arr[:, :, 0]
    arr = transpose_arr(arr)
    print(f"New shape after Transpose: {arr.shape}")
    print(arr)
    plt.imshow(arr, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
