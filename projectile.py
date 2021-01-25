import math
from math import cos, pi, tan
print("pi is: ", pi)
print("cos(pi) is", cos(pi))

degree = float(input("Input degree here: "))
theta = degree * (pi/180)
g = float(input("Input acceleration due to gravity here: "))
Vo = float(input("Input initial velocity here: "))
x = float(input("Input horizontal distance here: "))
Yo = float(input("Input height of barrel here: "))
Y = (Yo + x * tan(theta)) - (g * x ** 2) / (2 * (Vo * cos(theta)) ** 2)
print(Y)

