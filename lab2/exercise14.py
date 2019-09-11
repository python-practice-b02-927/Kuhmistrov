from turtle import *
import math
speed(12)
shape('triangle')

def nstar(n):
	for i in range(n):
		forward(300)
		left(1800/n)

n=int(input())
nstar(n)

input()