import data

from timeit import timeit
from typing import Callable

from insertion import insertion_sort
from merge import merge_sort


def sorting_algo_test(sorting_func: Callable, name: str = "Algorithm") -> None:
    if not sorting_func:
        raise ValueError("sorting_function should be provided.")

    gl = globals()
    gl["sorting_func"] = sorting_func

    result = timeit(
        stmt="sorting_func(data.random_sample(5000))", globals=gl, number=10)
    print(f"\'{name}\' with random data:\n", result)

    result = timeit(
        stmt="sorting_func(data.partially_sorted_sample(5000))", globals=gl, number=10)
    print(f"\'{name}\' with partially sorted data:\n", result)

    result = timeit(
        stmt="sorting_func(data.reverse_sorted_sample(5000))", globals=gl, number=10)
    print(f"\'{name}\' with reverse sorted data:\n", result)


if __name__ == "__main__":
    sorting_algo_test(insertion_sort, "Insertion sort")
    sorting_algo_test(merge_sort, "Merge sort")
    sorting_algo_test(sorted, "Timsort (Python builtin)")
