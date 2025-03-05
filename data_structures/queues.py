from collections import deque

#Crear una cola
task_queue = deque()

#Agregar elementos
task_queue.append("Task1")
task_queue.append("Task2")

#Eliminar el primer elemento (FIFO)
print(task_queue.popleft())