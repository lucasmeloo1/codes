import random

while True:
    n = random.randint(1,10)
    def double(n):
        return n * 2
    print ('The number is {}, the result is {}.'.format(n, (double(n))))
    again=input('Again?? (y/n): ').lower()
    if again != "y":
        break
