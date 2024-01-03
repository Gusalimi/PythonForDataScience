import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load
from PIL import Image


def main():
    """Main function"""
    try:
        arr = ft_load("animal.jpeg")
    except Exception:
        print("Error opening animal.jpeg")
        return
    print(arr)
    img = Image.fromarray(arr).convert("L").crop((450, 100, 850, 500))
    arr = np.array(img)[:, :, np.newaxis]
    print(f"New shape after slicing: {arr.shape} or {arr[:, :, 0].shape}")
    print(arr)
    plt.imshow(img, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
