def find_upper_bound(data: list[float], value: float) -> tuple[int, float | None]:
    if not data:
        return 0, None

    left = 0
    right = len(data) - 1
    iterations = 0
    upper_bound = None
    sorted_data = sorted(data)

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if sorted_data[mid] >= value:
            upper_bound = sorted_data[mid]
            right = mid - 1
        else:
            left = mid + 1

    return iterations, upper_bound


if __name__ == "__main__":
    items = [0.9, 1.4, 2.8, 3.6, 4.2, 6.5, 7.7, 8.3]

    print(f"List: {items}\n")

    for target in [1.0, 4.0, 2.9, 9.0, 7.6, 5.5]:
        result = find_upper_bound(items, target)
        print(f"Target: {target:>5} -> iterations: {result[0]}, upper_bound: {result[1]}")
