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

