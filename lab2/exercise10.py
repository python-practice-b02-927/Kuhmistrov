from turtle import *
import math
speed(12)
shape('triangle')

def circle():
	right(90)
	for i in range(100):
		forward(5)
		left(3.6)
	left(90)

n=int(input())
for i in range(n):
	circle()
	left(360/n)
input()