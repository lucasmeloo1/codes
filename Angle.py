import math
angle=int(input('Enter an angle: '))
s=math.sin(math.radians(angle))
c=math.cos(math.radians(angle))
t=math.tan(math.radians(angle))
print('The sine of {:.2f} is {:.2f}\nThe cosine of {:.2f} is {:.2f}\nThe tangent of {:.2f} is {:.2f}'.format(angle, s, angle, c, angle, t))