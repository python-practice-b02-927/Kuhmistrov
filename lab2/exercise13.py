from turtle import *
import math
speed(12)
shape('triangle')

def halfcircle(r):
	for i in range(100):
		forward(r*math.sin(math.pi/100))
		left(1.8)
def circle(r):
	for i in range(100):
		forward(2*r*math.sin(math.pi/100))
		left(3.6)

penup()
goto(200,0)
left(90)

pendown()
begin_fill()
circle(100)
color('yellow')
end_fill()
color('black')
penup()

goto(72.5,50)

pendown()
begin_fill()
circle(12.5)
color('blue')
end_fill()
color('black')
penup()

goto(127.5,50)

pendown()
left(180)
begin_fill()
circle(12.5)
color('blue')
end_fill()
color('black')
left(180)
penup()

goto(100,-25)

pendown()
width(5)

forward(50)

width(1)
penup()

goto(50,-25)
left(180)
pendown()
width(3)
color('red')
halfcircle(50)
color('black')

input()