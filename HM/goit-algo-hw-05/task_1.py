class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    self.table[key_hash].remove(pair)
                    return True
        return False

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


if __name__ == "__main__":
    H = HashTable(5)
    print("Insertion result for ['apple', 10]:", H.insert("apple", 10))
    print("Insertion result for ['orange', 20]:", H.insert("orange", 20))
    print("Insertion result for ['banana', 30]:", H.insert("banana", 30))

    print("Value for key 'apple':", H.get("apple"))
    print("Value for key 'orange':", H.get("orange"))
    print("Value for key 'banana':", H.get("banana"))

    print("Delete result for key 'orange':", H.delete("orange"))
    print("Value for key 'orange':", H.get("orange"))
