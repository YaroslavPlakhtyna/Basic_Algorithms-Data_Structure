from typing import Any


def check_sorted(data: list[Any], sorted_data: list[Any]) -> bool:
    return len(data) == len(sorted_data) and sorted(data) == sorted_data
