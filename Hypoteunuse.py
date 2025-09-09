import math
c1=int(input('Enter the length of the opposite cathetus: '))
c2=int(input('Enter the length of the adjacent cathetus: '))
h=math.hypot(c1, c2)
print ('The hypoteunuse is {:.2f}'.format (h))