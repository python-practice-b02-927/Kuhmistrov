from turtle import *
speed(10)
shape('triangle')
for i in range(2000):
	left(2)
	forward(0.001*(1 + (i)**2)**0.5)


input()