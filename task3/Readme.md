# Matrix Multiplication Performance: C++ vs. Python (NumPy)

## 1. Summary

* **Code Complexity:** Python requires significantly fewer lines of code (~29 lines) compared to C++ (~77 lines) due to native high-level abstractions.
* **Small Matrix Performance ($2 \times 3$ and $3 \times 2$):** C++ is better at small matrix operations ($10^{-6}\text{ seconds}$ vs. $10^{-4}\text{ seconds}$) because of Python overhead.
* **Large Matrix Performance ($1000 \times 1000$):** NumPy finishes in under **$0.05\text{ seconds}$**, whereas naive C++ takes **$8\text{--}9\text{ seconds}$**. This massive performance advantage comes from low-level optimizations embedded in NumPy's underlying engine.

---

## 2. Performance Comparison Overview

| Metric / Scenario | C++ (Naive Implementation) | Python (NumPy) | Primary Technical Driver |
| :--- | :--- | :--- | :--- |
| **Lines of Code (LOC)** | ~77 lines | ~29 lines | Python syntax and standard libraries require less setup boilerplate. |
| **Small Matrix Execution ($2 \times 3 \times 2$)** | **$\approx 10^{-6}\text{ s}$** | $\approx 10^{-4}\text{ s}$ | C++ avoids Python interpreter call-stack and memory allocation overhead. |
| **Large Matrix Execution ($1000 \times 1000$)** | $\approx 8.0\text{--}9.0\text{ s}$ | **$< 0.05\text{ s}$** | NumPy uses multi-threading, SIMD hardware instructions, and cache blocking. |
| **Optimized Loop C++ ($i\text{-}k\text{-}j$)** | $\approx 6.0\text{ s}$ | $< 0.05\text{ s}$ | Swapping loops optimizes linear memory access and improves L1/L2 cache hit rates. |

---

## 3. Performance Analysis

### Small Matrices ($2 \times 3$ & $3 \times 2$)
For trivial matrix sizes typical of basic unit tests:
* **C++ :** Executing at $\approx 10^{-6}\text{ seconds}$, C++ runs compiled, low-level instructions directly on stack memory.
* **Python Overhead:** Executing at $\approx 10^{-4}\text{ seconds}$, Python is roughly $100\times$ slower. Every `A @ B` call requires Python to inspect object types, and allocate Python heap wrappers.

### Large Matrices ($1000 \times 1000$)
For large matrices executing $2 \times N^3$ (2 billion) floating-point operations:
* **Python (NumPy):** Finishes in **$< 0.05\text{ seconds}$**.
* **Why NumPy is Faster:**
  1. **Multi-Threading:** NumPy offloads computations to BLAS backends (such as OpenBLAS, Intel MKL, or Apple Accelerate) that automatically distribute work across all available CPU cores.
  2. **Cache Tiling (Blocking):** NumPy breaks large matrices into smaller sub-blocks that fit directly inside high-speed **L1 and L2 CPU caches**, avoiding expensive main RAM fetch cycles.
  3. **SIMD Vectorization:** Modern CPUs use AVX/AVX-512 vector instructions to multiply multiple numbers in a single clock cycle.

# AI Generated Code

## C++
```
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <cassert>
#include <iomanip>

using namespace std;

// Generic 2D Matrix Multiplication: C = A x B
// A: (m x n), B: (n x p), C: (m x p)
vector<vector<double>> multiply_matrices(const vector<vector<double>>& A, const vector<vector<double>>& B) {
    size_t m = A.size();
    size_t n = A[0].size();
    size_t p = B[0].size();

    // Cache-friendly row-major ordering (i-k-j loop pattern)
    vector<vector<double>> C(m, vector<double>(p, 0.0));
    for (size_t i = 0; i < m; ++i) {
        for (size_t k = 0; k < n; ++k) {
            for (size_t j = 0; j < p; ++j) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return C;
}

// Unit Test 1: Identity Matrix Multiplication
void test_identity_multiplication() {
    vector<vector<double>> A = {{1, 2}, {3, 4}};
    vector<vector<double>> I = {{1, 0}, {0, 1}};
    auto result = multiply_matrices(A, I);
    assert(result == A);
    cout << "[PASS] Test Identity Matrix Multiplication\n";
}

// Unit Test 2: Known Result Matrix Multiplication
void test_known_values() {
    vector<vector<double>> A = {{1, 2, 3}, {4, 5, 6}}; // 2x3
    vector<vector<double>> B = {{7, 8}, {9, 10}, {11, 12}}; // 3x2
    vector<vector<double>> expected = {{58, 64}, {139, 154}}; // 2x2
    
    auto result = multiply_matrices(A, B);
    for (size_t i = 0; i < result.size(); ++i) {
        for (size_t j = 0; j < result[0].size(); ++j) {
            assert(abs(result[i][j] - expected[i][j]) < 1e-9);
        }
    }
    cout << "[PASS] Test Known Matrix Values Multiplication\n";
}

int main() {
    // Run Unit Tests First
    cout << "--- Running Unit Tests ---\n";
    test_identity_multiplication();
    test_known_values();
    cout << "All unit tests passed successfully!\n\n";

    // User Input for General Case Dimensions
    size_t m, n, p;
    cout << "Enter dimensions m, n, p (for A: m x n and B: n x p): ";
    if (!(cin >> m >> n >> p) || m == 0 || n == 0 || p == 0) {
        cerr << "Invalid matrix dimensions.\n";
        return 1;
    }

    // Populate random matrices
    mt19937 rng(42);
    uniform_real_distribution<double> dist(1.0, 10.0);

    vector<vector<double>> A(m, vector<double>(n));
    vector<vector<double>> B(n, vector<double>(p));

    for (size_t i = 0; i < m; ++i)
        for (size_t j = 0; j < n; ++j)
            A[i][j] = dist(rng);

    for (size_t i = 0; i < n; ++i)
        for (size_t j = 0; j < p; ++j)
            B[i][j] = dist(rng);

    // Benchmarking
    auto start = chrono::high_resolution_clock::now();
    auto C = multiply_matrices(A, B);
    auto end = chrono::high_resolution_clock::now();
    
    chrono::duration<double, milli> duration = end - start;
    cout << fixed << setprecision(3);
    cout << "C++ Matrix Multiplication (" << m << "x" << n << " * " << n << "x" << p << ") completed in: " 
         << duration.count() << " ms\n";

    return 0;
}
```
## Python
```
import time
import numpy as np

def benchmark_numpy_multiplication():
    print("--- NumPy Matrix Multiplication ---")
    try:
        m = int(input("Enter dimension m: "))
        n = int(input("Enter dimension n: "))
        p = int(input("Enter dimension p: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    np.random.seed(42)
    A = np.random.rand(m, n)
    B = np.random.rand(n, p)

    start_time = time.perf_counter()
    C = np.matmul(A, B)  # or A @ B
    end_time = time.perf_counter()

    elapsed_ms = (end_time - start_time) * 1000
    print(f"NumPy Matrix Multiplication ({m}x{n} * {n}x{p}) completed in: {elapsed_ms:.3f} ms")

if __name__ == "__main__":
    benchmark_numpy_multiplication()
```

The above code has been written by AI. It has given the output in milliseconds instead of seconds which might be more suitable for comparing the efficiencies of both programs. The AI gave the user the option of choosing the sizes themselves and later generate random matrices based on those sizes.

AI also changed the order of loops in C++ program to make the memory access faster which was very nice and something that I did not implement in my original code. No custom prompt was given to AI other than providing the problem statement.
