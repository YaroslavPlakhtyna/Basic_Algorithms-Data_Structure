import numpy

stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)

print(stack.pop())
print(stack)

def peek(stack):
    return stack[-1]
print(peek(stack))

def is_empty(stack):
    return len(stack) == 0
print(is_empty(stack))

class Stack:
    def __init__(self):
        self.stack = []
    
    # Додавання елемента до стеку
    def push(self, item):
        self.stack.append(item)

    # Видалення елемента зі стеку
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    
     # Перевірка, чи стек порожній
    def is_empty(self):
        return len(self.stack) == 0
    
    # Перегляд верхнього елемента стеку без його видалення
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
s = Stack()
s.push('a')
s.push('b')
s.push('c')
print(s.peek())
print(s.pop())
print(s.peek())
print(s.is_empty())

#push — додає елемент до вершини стеку.
#pop — видаляє верхній елемент стеку (якщо він існує) і повертає його. Якщо стек порожній, метод повертає None.
#is_empty — перевіряє, чи стек порожній, повертаючи True або False.
#peek — повертає верхній елемент стеку без його видалення. Якщо стек порожній, метод не повертає нічого.