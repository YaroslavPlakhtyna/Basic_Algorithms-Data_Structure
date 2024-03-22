from typing import Any

from data import random_sample
from check import check_sorted


ArrType = list[Any]


def merge(left: ArrType, right: ArrType) -> ArrType:
    merged = ArrType()
    while len(left) and len(right):
        if left[0] <= right[0]:
            merged.append(left[0])
            left.remove(left[0])
        else:
            merged.append(right[0])
            right.remove(right[0])

    while len(left):
        merged.append(left[0])
        left.remove(left[0])
    while len(right):
        merged.append(right[0])
        right.remove(right[0])

    return merged


def merge_sort(data: ArrType) -> ArrType:
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    return merge(merge_sort(left), merge_sort(right))


if __name__ == "__main__":
    data = random_sample(20)
    print("Data:\n", data)
    sorted_data = merge_sort(data)
    print("Merge sorted data:\n", sorted_data)
    assert check_sorted(data, sorted_data)
