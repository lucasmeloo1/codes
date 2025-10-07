def name(x, y):
    return x, y

a = input("What's your name? ")
b = int(input("How old are you? "))
print("{} is {} years old.".format(*name(a, b)))

