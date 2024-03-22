import random


def random_sample(count=1000) -> list[int]:
    return list([random.randint(0, 1000) for _ in range(0, count)])


def partially_sorted_sample(count=1000) -> list[int]:
    data = random_sample(count)
    center = len(data) // 2
    return sorted(data[:center]) + data[center:]


def reverse_sorted_sample(count=1000) -> list[int]:
    data = random_sample(count)
    return sorted(data, reverse=True)


if __name__ == "__main__":
    print("Random data:\n", random_sample(20))
    print("Partially sorted data:\n", partially_sorted_sample(20))
    print("Reverse sorted data:\n", reverse_sorted_sample(20))
