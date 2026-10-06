# Task 4: 2D Matrix Slicing

## 1. Source Image

<img width="612" height="408" alt="sample" src="https://github.com/user-attachments/assets/cc737006-dfe4-42e0-a62a-c4b79b259bd5" />


---

## 2. Implementation Outputs

**Python Output (`sliced_output_rgb.jpg`)**

<img width="300" height="300" alt="sliced_output_rgb" src="https://github.com/user-attachments/assets/73393dec-8f79-41ec-9583-4f49fc485023" />


**Java Output (`slicedImage.jpg`)**

<img width="300" height="300" alt="slicedImage" src="https://github.com/user-attachments/assets/bdd51e4c-6e15-4b0c-adb9-036cdafbcc42" />

---

It can be seen from the images that the resulting images are the same for Java and Python. Both images take the slice of pixels from 100 to 400 for the row and 150 to 450 for the column. C++ was omitted because it lacks a built-in native image library. Handling formats like JPEG or PNG in pure C++ requires either heavy external libraries or third-party decoders. Java, on the other hand, has `BufferedImage` which is built into it.


# AI Generated Code

## C++

```
#include <iostream>
#include <vector>
#include <fstream>
#include <cassert>

using namespace std;

// Structure representing an RGB Image
struct RGB {
    unsigned char r, g, b;
};

// Generic 2D Slicing Function for Grayscale/RGB Matrix
vector<vector<RGB>> slice_matrix(const vector<vector<RGB>>& matrix, 
                                 size_t row_start, size_t row_end, 
                                 size_t col_start, size_t col_end) {
    size_t rows = row_end - row_start;
    size_t cols = col_end - col_start;
    vector<vector<RGB>> slice(rows, vector<RGB>(cols));

    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            slice[i][j] = matrix[row_start + i][col_start + j];
        }
    }
    return slice;
}

// Save sliced output to PPM visual image format
void save_ppm(const std::string& filename, const vector<vector<RGB>>& img) {
    size_t height = img.size();
    size_t width = img[0].size();

    ofstream out(filename, ios::binary);
    out << "P6\n" << width << " " << height << "\n255\n";

    for (size_t i = 0; i < height; ++i) {
        for (size_t j = 0; j < width; ++j) {
            out.put(img[i][j].r);
            out.put(img[i][j].g);
            out.put(img[i][j].b);
        }
    }
    out.close();
}

int main() {
    size_t width, height;
    cout << "Enter image grid width and height (e.g. 500 500): ";
    cin >> width >> height;

    // Create a synthetic image gradient
    vector<vector<RGB>> image(height, vector<RGB>(width));
    for (size_t i = 0; i < height; ++i) {
        for (size_t j = 0; j < width; ++j) {
            image[i][j] = { static_cast<unsigned char>((i * 255) / height),
                            static_cast<unsigned char>((j * 255) / width),
                            128 };
        }
    }

    size_t r_start, r_end, c_start, c_end;
    cout << "Enter crop coordinates (row_start row_end col_start col_end): ";
    cin >> r_start >> r_end >> c_start >> c_end;

    assert(r_end <= height && c_end <= width && r_start < r_end && c_start < c_end);

    auto cropped = slice_matrix(image, r_start, r_end, c_start, c_end);
    save_ppm("cpp_cropped_output.ppm", cropped);

    cout << "Cropped visual image saved to 'cpp_cropped_output.ppm' successfully.\n";
    return 0;
}
```

## Python

```
import numpy as np
from PIL import Image

def run_numpy_slicing():
    print("--- NumPy 2D Image Slicing ---")
    width = int(input("Enter image width: "))
    height = int(input("Enter image height: "))

    # Generate synthetic RGB test pattern matching C++ version
    y, x = np.ogrid[:height, :width]
    r = (y * 255 // height).astype(np.uint8)
    g = (x * 255 // width).astype(np.uint8)
    b = np.full((height, width), 128, dtype=np.uint8)
    img_array = np.dstack((r, g, b))

    print(f"Generated Synthetic Image Shape: {img_array.shape}")

    r_start = int(input("Enter row_start: "))
    r_end = int(input("Enter row_end: "))
    c_start = int(input("Enter col_start: "))
    c_end = int(input("Enter col_end: "))

    # 2D Slicing operation (view on multi-channel array)
    cropped_array = img_array[r_start:r_end, c_start:c_end, :]

    # Save output to compare against C++ image
    cropped_image = Image.fromarray(cropped_array)
    cropped_image.save("numpy_cropped_output.png")
    print("Cropped visual image saved to 'numpy_cropped_output.png' successfully.")

if __name__ == "__main__":
    run_numpy_slicing():

```

No custom prompt other than problem statement was given to the AI. It chose to implement the matrix slice in C++ unlike me. The python code is nothing unusual. It uses numpy to slice the array and then use another library to convert the rgb values back to an image.

In C++ code AI implemented a custom RGB class, used that RGB class and vectors to create a Matrix of colors and implemented slicing over that matrix. However, the image is not read from any directories and custom image selection is not possible. The code generates the image itself and slices that. When prompted to add the option of adding a custom image it resorted to external libraries such as `OpenCV` and `libpng`. This is the reason I avoided using C++ for image handling and instead used Java for the task.