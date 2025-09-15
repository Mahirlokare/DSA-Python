class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])

ht = HashTable(10)
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("grape", 300)
ht.display()
print("Search banana:", ht.search("banana"))
ht.delete("banana")
ht.display()
