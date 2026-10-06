import cv2
import matplotlib.pyplot as plt

def slice_rgb_image(image_path, row_start, row_end, col_start, col_end):
    img_bgr = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    sliced_rgb = img_rgb[row_start:row_end, col_start:col_end, :]

    sliced_bgr = cv2.cvtColor(sliced_rgb, cv2.COLOR_RGB2BGR)
    cv2.imwrite("sliced_output_rgb.jpg", sliced_bgr)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title(f"Original Image\nShape: {img_rgb.shape}")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(sliced_rgb)
    plt.title(f"Sliced Image\nShape: {sliced_rgb.shape}")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    slice_rgb_image('sample.jpg', row_start=100, row_end=400, col_start=150, col_end=450)