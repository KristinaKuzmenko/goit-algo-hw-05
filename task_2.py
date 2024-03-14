import random


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iter_count = 0

    while low < high:
        mid = (high + low) // 2
        iter_count += 1

        if arr[mid] == x:
            return iter_count, arr[mid]

        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid

    upper_bound = arr[low] if low < len(arr) and arr[low] >= x else None
    return iter_count, upper_bound


# Тестування
arr = [random.random() for _ in range(1000)]
arr.sort()
x = 0.55
iterations, upper_bound = binary_search(arr, x)
if upper_bound is not None:
    print(f"Upper bound of {x} is {upper_bound}, found in {iterations} iterations")
else:
    print(f"Element is not present in array, {iterations} iterations was made")
