#Розглянемо реалізацію двозв'язного списку на Python

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

"""
self.data — змінна для зберігання даних будь-якого формату у вузлі.
self.next — вказівник на наступний вузол у списку. Початково встановлено на None, бо при створенні вузла ми ще не знаємо, який буде наступний вузол.
self.prev — вказівник на попередній вузол у списку. З тих самих причин початкове значення встановлено на None."""

class Node:
   def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
