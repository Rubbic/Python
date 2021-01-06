#funcion cola
from collections import deque

cola = deque(["Alex","Roel","Juan"])
print(cola)
cola.append("Maria")
cola.append("Arnoldo")
print(cola)


persona = cola.popleft() 
print(persona)
print(cola)