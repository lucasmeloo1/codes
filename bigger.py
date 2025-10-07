def maior(x, y):
    if x > y:
        return x
    elif y > x:
        return y


a = int(input('Enter a number: ')) 
b = int(input('Enter another number: '))
if a!=b:
    print(maior(a, b))
else:
    print('They are equal!')



