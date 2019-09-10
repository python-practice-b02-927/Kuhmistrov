from turtle import *
speed(10)
shape('triangle')
for i in range(10):
	for j in range(4):
		forward(20*i)
		right(90)
	penup()
	left(90)
	forward(10)
	left(90)
	forward(10)
	left(180)
	pendown()

input()