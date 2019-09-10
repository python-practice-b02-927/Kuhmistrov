from turtle import *
import math
speed(12)
shape('triangle')

def circle(n):
	right(90)
	for i in range(100):
		forward(n)
		left(3.6)
	left(90)

n=int(input())
for i in range(1,1+n,1):
	circle(0.5*i)
	left(180)
	circle(0.5*i)
	left(180)
input()