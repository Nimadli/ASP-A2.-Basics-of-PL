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

