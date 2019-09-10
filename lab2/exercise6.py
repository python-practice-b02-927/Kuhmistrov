from turtle import *
speed(10)
shape('triangle')
n=int(input())
for i in range(n):
	forward(50)
	stamp()
	backward(50)
	right(360/n)

input()