import random
import sys
from stack import Stack

stack = Stack(100000000)
memoria_actual = 0

while memoria_actual < 100000000:
    elemento = random.randint(1, 1000)
    stack.push(elemento)
    
    memoria_actual = sys.getsizeof(stack)
    
