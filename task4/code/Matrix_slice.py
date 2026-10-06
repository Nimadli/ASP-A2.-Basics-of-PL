import os
from pathlib import Path
import cv2
import numpy as np


def slice_matrix_2d(matrix, row_start, row_end, col_start, col_end):
    height, width = matrix.shape[:2]
    if row_start < 0 or row_end > height or col_start < 0 or col_end > width:
        raise ValueError(
            f"Slice boundary [{row_start}:{row_end}, {col_start}:{col_end}] is out of bounds for matrix dimensions {height}x{width}"
        )

    return matrix[row_start:row_end, col_start:col_end]


def main():
    image_path = "sample.jpg"
    output_path = "sliced_output_rgb.jpg"

    num_matrix = np.array([
        [10, 11, 12, 13, 14],
        [20, 21, 22, 23, 24],
        [30, 31, 32, 33, 34],
        [40, 41, 42, 43, 44]
    ])
    num_slice = slice_matrix_2d(num_matrix, row_start=1, row_end=3, col_start=2, col_end=5)
    print("Original 2D Matrix:\n", num_matrix)
    print("\nSliced 2D Sub-Matrix (Rows 1:3, Cols 2:5):\n", num_slice)

    img_matrix = cv2.imread(str(image_path))

    print(f"Original Image Dimensions: {img_matrix.shape[0]}x{img_matrix.shape[1]} (Height x Width)")

    r_start, r_end = 100, 400
    c_start, c_end = 150, 450

    sliced_img_matrix = slice_matrix_2d(img_matrix, r_start, r_end, c_start, c_end)

    print(f"Sliced Image Dimensions:   {sliced_img_matrix.shape[0]}x{sliced_img_matrix.shape[1]}")

    cv2.imwrite(str(output_path), sliced_img_matrix)


if __name__ == "__main__":
    main()