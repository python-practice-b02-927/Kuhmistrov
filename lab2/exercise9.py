from turtle import *
import math
speed(12)
shape('triangle')

def polygon(n):
	penup()
	goto(0,0)
	for i in range(n):
		goto(30*n*math.cos(i*2*math.pi/n),30*n*math.sin(i*2*math.pi/n))
		pendown()
	goto(30*n,0)

for i in range(3,14,1):
	polygon(i)

input()