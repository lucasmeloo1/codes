numbers = []

for i in range (5):
    n = int(input('Enter a number: '))
    numbers.append(n)

print('The biggest number is', max(numbers))
print('The smallest number is', min(numbers))
print('The average is', sum(numbers)/len(numbers))

def double_list(lst):
    new_list = []
    for num in lst:
        new_list.append(num * 2)
    return new_list
print('Doubled numbers: ', double_list(numbers))