#import sys
#sys.path.append('')

import graphics as gr

SIZE_X = 1080
SIZE_Y = 720

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

#  Начальное положение шарика
coords = gr.Point(200, 200)
#  Скорость
velocity = gr.Point(50, -40)
#ускорение
a=gr.Point(10,5)

#functions

def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                      point_1.y + point_2.y)

    return new_point

def draw_circle(coords):
    circle = gr.Circle(coords, 30)
    circle1 = gr.Circle(coords, 50)
    circle2 = gr.Circle(coords, 70)
    circle3 = gr.Circle(coords, 100)
    circle4 = gr.Circle(coords, 140)
    circle5 = gr.Circle(coords, 160)

    circle.setFill('red')
    circle1.setFill('orange')
    circle2.setFill('yellow')
    circle3.setFill('green')
    circle4.setFill('blue')
    circle5.setFill('magenta')
  
    circle5.draw(window)
    circle4.draw(window)
    circle3.draw(window)
    circle2.draw(window)
    circle1.draw(window)
    circle.draw(window) 

def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)    

def check_coords(coords, velocity):
    if coords.y - 120< 0 or coords.y + 120> SIZE_Y:
        velocity.y = -velocity.y
    if coords.x - 120< 0 or coords.x + 120> SIZE_X:
        velocity.x = -velocity.x   



while True:
    clear_window()

    draw_circle(coords)
    coords = add(coords, velocity)
    velocit = add(velocity,a)

    check_coords(coords, velocity)

    gr.time.sleep(0.02)