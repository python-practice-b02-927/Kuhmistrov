from turtle import *
import math
speed(12)
shape('triangle')

def halfcircle(n):
	for i in range(100):
		forward(n)
		right(1.8)

left(90)
for i in range(10):
	halfcircle(2)
	halfcircle(0.4)

input()