class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
n = int(input("Enter number of linked list operations: "))
for _ in range(n):
    op = input("Enter operation (insert x / delete x / traverse): ").split()
    if op[0] == "insert":
        ll.insert(int(op[1]))
    elif op[0] == "delete":
        ll.delete(int(op[1]))
    elif op[0] == "traverse":
        ll.traverse()

# Complexity:
# Insert: O(1), Delete: O(n), Traverse: O(n)
