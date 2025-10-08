import random
import math
import time

n=(random.randint(0,100))

print("Starting countdown...")
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)  
def square_root (x):
    return math.sqrt(x)

result=square_root(n)
print(f"The result is {result:.2f} ")

