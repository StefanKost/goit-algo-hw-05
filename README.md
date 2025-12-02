# goit-algo-hw-05
Search algorithms

## Task 1 (Hash Table)
```bash
python hash_table.py
```

## Task 2 (Binary Search)
Calculate the number of iterations and find the upper bound of the first element that is equal to or greater than the target.
```bash
python binary_search.py
```

## Task 3 (Substring search algorithms comparison)
Compare substring search algorithms: **Boyer-Moore**, **Knuth-Morris-Pratt**, and **Rabin-Karp**.

---

### Results

![Benchmark Results](https://github.com/user-attachments/assets/1787ba65-d136-43a6-8e55-fef2de7c9ade)

---

### Conclusions

1. **Boyer-Moore is the fastest** algorithm in all tests
    - Article 1: `0.050`s (existing), `0.210`s (fictional)
    - Article 2: `0.024`s (existing), `0.280`s (fictional)

2. **Performance ranking**:
    - Boyer-Moore: consistently fastest
    - Knuth-Morris-Pratt: second place
    - Rabin-Karp: slowest, especially for fictional patterns

3. **Why Boyer-Moore performs best**:
    - Uses a skip table to jump over unnecessary characters
    - Compares the pattern from right to left, enabling faster mismatch detection
    - Remains highly efficient even for fictional patterns, outperforming Knuth-Morris-Pratt and Rabin-Karp by a significant margin

4. **Fictional vs Existing patterns**:
    - All algorithms are slower on fictional patterns because the full text must be scanned
    - The slowdown is most pronounced for **Rabin-Karp**, which increases from `~0.4`s to `~2–3`s