from typing import Any

from data import random_sample
from check import check_sorted


def insertion_sort(data: list[Any]) -> None:
    if len(data) <= 1:
        return

    sorted_data = data
    for i in range(1, len(sorted_data)):
        for j in range(0, i):
            if sorted_data[i] < sorted_data[j]:
                target = sorted_data[i]
                del sorted_data[i]
                sorted_data.insert(j, target)
                break
    return sorted_data


if __name__ == "__main__":
    data = random_sample(20)
    print("Data:\n", data)
    sorted_data = insertion_sort(data)
    print("Insertion sorted data:\n", sorted_data)
    assert check_sorted(data, sorted_data)
