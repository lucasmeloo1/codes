# Average of four student scores
n = int(input('Enter a number:'))
n1 = int(input('Enter another number:'))
n2 = int(input('Enter one more number:'))
n3 = int(input('Enter the last number:'))
m = (n+n1+n2+n3)/4
print('The average student score between {}, {}, {} and {} is {:.1f}'.format(n, n1, n2, n3, m))