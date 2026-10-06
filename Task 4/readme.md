# Task 4: 2D Matrix Slicing

## 1. Source Image

<img width="612" height="408" alt="sample" src="https://github.com/user-attachments/assets/5c04e46c-ab99-467e-ba3a-865c66acbc39" />


---

## 2. Implementation Outputs

**Python Output (`sliced_output_rgb.jpg`)**

<img width="300" height="300" alt="sliced_output_rgb" src="https://github.com/user-attachments/assets/816e6bc2-6408-4597-9b71-08d56651713b" />

**Java Output (`slicedImage.jpg`)**


<img width="300" height="300" alt="slicedImage" src="https://github.com/user-attachments/assets/ef30eacb-9a15-41d6-81c7-9d5cfaf1a5a1" />

---

It can be seen from the images that the resulting images are the same for Java and Python. Both images take the slice of pixels from 100 to 400 for the row and 150 to 450 for the column. C++ was omitted because it lacks a built-in naative image library. Handling formats like JPEG or PNG in pure C++ requires either heavy external libraries or third-party decoders. Java, on the other hand, has BufferedImage which is built into it.
