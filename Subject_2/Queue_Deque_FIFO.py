from queue import Queue

# Створюємо чергу
q = Queue()

# Додаємо елементи
q.put('a')
q.put('b')
q.put('c')

print(q.queue)

# Видаляємо елемент
q.get()
print(q.queue)

#qsize(): Повертає поточний розмір черги.
#empty(): Повертає True, якщо черга порожня, в іншому випадку — False.
#full(): Повертає True, якщо черга повна (якщо вона має обмежений розмір), в іншому випадку — False.

# Створюємо чергу
q = Queue(maxsize = 3)

# Перевіряємо, чи черга порожня
print(q.empty())

# Додаємо елементи
q.put('a')
q.put('b')
q.put('c')

# Перевіряємо, чи черга повна
print(q.full())

# Перевіряємо розмір черги
print(q.qsize())

# Видаляємо елементи
print(q.get())
print(q.get())

from queue import Queue
import random

class Client:
  def __init__(self, name):
    self.name = name
    self.operations = random.randint(1, 5) # Випадкова кількість операцій

class Bank:
  def __init__(self):
    self.clients = Queue()

  def new_client(self, client):
    self.clients.put(client)

  def serve_clients(self):
    while not self.clients.empty():
      current_client = self.clients.get()
      print(f"Обслуговуємо клієнта {current_client.name} з {current_client.operations} операцій")
      # Тут можна додати час обслуговування та іншу логіку

# Створюємо банк
bank = Bank()

# Додаємо клієнтів
for i in range(5):
  bank.new_client(Client(f"Client-{i}"))

# Обслуговуємо клієнтів
bank.serve_clients()


#
# Двостороння черга, або просто "deque" (від англ. "double-ended queue"),
# є особливою структурою даних, яка дозволяє додавати та видаляти елементи на обох кінцях
# Основні методи, які надає deque, це append(), appendleft(), pop(), popleft()
#

from collections import deque

d = deque()
print(d)

d.append('right')
d.appendleft('left')
print(d)

d.pop()
d.popleft()
print(d)

d.extend(['a','b','c'])
d.extendleft(['x','y','z'])
print(d)

# deque.rotate(n) робить циклічний зсув усіх елементів в deque на n позицій. 
d.rotate(2)
print(d)  # deque(['b', 'c', 'z', 'y', 'x', 'a'])

d.rotate(-2)
print(d) # deque(['z', 'y', 'x', 'a', 'b', 'c'])

# Обмеження розміру:
d = deque(maxlen=3)
d.extend([1, 2, 3])
print(d)  # deque([1, 2, 3])

d.append(4)
print(d)  # deque([2, 3, 4])

# Пошук у deque:
d = deque([1, 2, 3, 4, 2, 5])
print(d.count(2))  # 2
