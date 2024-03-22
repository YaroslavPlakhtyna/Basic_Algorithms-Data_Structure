#Вузол — це об'єкт, який містить два атрибути: data (дані), які представляють значення вузла, 
# і next, який вказує на наступний вузол у списку.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Оскільки у зв’язаному списку кожен вузол має посилання на наступний вузол,
# то потрібно задавати атрибут self.head , який вказує на перший вузол.
        
# Цей вузол називається "головою" списку, тому він і має назву head.
class LinkedList: 
    def __init__(self):
        self.head = None
#Найпростіший спосіб вставити новий вузол — це вставити його в кінець списку.
    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

# Додавання в початок теж досить просте:
def inser_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.data
    self.data = new_node

# Вставка вузла після заданого вузла:
def insert_after(self, prev_node: Node, data):
    if prev_node is None:
        print("Попереднього вузла не існує.")
        return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

#Пошук вузлів
def search_element(self, data) -> Node | None:
    cur = self.head
    while cur:
        if cur.data == data:
            return cur
        cur = cur.next
    return None

#Видалення вузлів
def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
        self.head = cur.next
        cur = None
        return
    prev = None
    while cur and cur.data != key:
        prev = cur
        cur = cur.next
    if cur is None:
        return
    prev.next = cur.next
    cur = None


## Повний приклад, що реалізує зв'язний список, буде виглядати таким чином:
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
        while cur.next:
            cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)



