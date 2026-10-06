# Memory Usage Analysis: Python Tuples vs Lists

To understand the difference in memory overhead between tuples and lists in Python, it is helpful to observe how their sizes scale across varying contents and sizes.

## 1. Experimental Code and Measurements

```
# 1. Empty Containers
tpl = ()
print(tpl.__sizeof__())  # Output: 24 bytes

lst = []
print(lst.__sizeof__())  # Output: 40 bytes


# 2. Containers with 3 Elements
tpl = (1, 2, 3)
print(tpl.__sizeof__())  # Output: 48 bytes

lst = [1, 2, 3]
print(lst.__sizeof__())  # Output: 72 bytes


# 3. Containers with 4 Elements
tpl = (1, 2, 3, 4)
print(tpl.__sizeof__())  # Output: 56 bytes

lst = [1, 2, 3, 4]
print(lst.__sizeof__())  # Output: 72 bytes


# 4. Containers with Large Integers
large_int = 123159187239817239487123904871029387410928375190283750192837091287350918

tpl = (1, 2, large_int)
print(tpl.__sizeof__())  # Output: 48 bytes

lst = [1, 2, large_int]
print(lst.__sizeof__())  # Output: 72 bytes

```

## 2. Key Insights and Explanations

### Base Overhead: Empty Containers

* **Empty Tuple (`24 bytes`):** Because tuples are **immutable**, their size is fixed at creation. Their struct header contains only the essential fields: reference count, type pointer, and object length ($3 \times 8 = 24$ bytes).

* **Empty List (`40 bytes`):** Because lists are **mutable** dynamic arrays, Python tracks two additional parameters in the list struct header:

  1. `ob_item` (8 bytes): Pointer to the array of item references.

  2. `allocated` (8 bytes): Counter tracking reserved capacity slots.

  This adds an extra $16\text{ bytes}$ ($24 + 16 = 40$ bytes).

### Dynamic Growth & Pre-allocation in Lists

When creating `lst = [1, 2, 3]`, Python pre-allocates buffer space for **4 slots** ($40\text{ base} + 4 \times 8\text{ bytes} = 72\text{ bytes}$) to optimize future `.append()` calls.

Consequently, when the list expands to 4 items (`lst = [1, 2, 3, 4]`), its memory size **remains 72 bytes** because it fills the already pre-allocated slot without requesting new memory.

In contrast, the tuple grows strictly by **8 bytes per item** ($24 \to 48 \to 56$ bytes).

### Pointer Indirection and Large Values

An interesting property of both lists and tuples is that replacing small items with **extremely large integers does not change the container size** reported by `__sizeof__()`.

* **3 Small Integers:** `(1, 2, 3)` occupies **48 bytes** (tuple) and **72 bytes** (list).

* **2 Small Integers + 1 Large Integer:** `(1, 2, large_int)` still occupies **48 bytes** (tuple) and **72 bytes** (list).

This occurs because Python containers store **8-byte memory pointers** pointing to objects stored elsewhere in RAM, rather than storing raw numeric values inside the container struct itself.
