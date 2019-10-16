import time
import json
from random import randrange as rnd, choice
from tkinter import *


goldfish = {'x': 0, 'y': 0,
                'a': 0, 'clicked': False}

root = Tk()
root.geometry('800x800')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

textt = canv.create_text(400, 250, 
            text="Click Right Mouse Button to\nSTART THE GAME",
            justify=CENTER, font="Impact 40")

textt = canv.create_text(400, 350, text="tap on circles = 1",
            justify=CENTER, font="Impact 20", fill="grey")

textt = canv.create_text(400, 400, text="tap on rectangle = 20",
            justify=CENTER, font="Impact 20", fill="grey")

textt = canv.create_text(400, 450, text="<Esc> to stop the game",
            justify=CENTER, font="Impact 20", fill="black")


def create_goldfish():
    global goldfish, is_stopped
    if 'id' in goldfish:
        canv.delete(goldfish['id'])
    #canv.delete(goldfish['id'])
    goldfish = {'x': rnd(100, 700), 'y': rnd(100, 450),
                'a': rnd(5, 15), 'clicked': False}
    goldfish['id'] = canv.create_rectangle(goldfish['x'] - goldfish['a'], 
                                           goldfish['y'] - goldfish['a'],
                                           goldfish['x'] + goldfish['a'],
                                           goldfish['y'] + goldfish['a'],
                                           fill=choice(colors), width=0)
    if not is_stopped:
        root.after(500, create_goldfish)


def start_game(event):
    global is_started
    if not is_started:
        canv.delete(ALL)
        new_ball()
        movement_loop()
        hit_check()
        create_goldfish()
        is_started = True


points = 0
balls = {}
keys = {}
is_stopped = False
is_started = False


def del_ball(ball):
    if ball['id'] in balls:
        del balls[ball['id']]
        canv.delete(ball['id'])


def new_ball():
    global is_stopped
    #global x,y,r,f
    #canv.delete(ALL)
    #global counter
    #counter =+ 1
    #lol = counter%5
    b = {'x': rnd(100, 700), 'y': rnd(100, 450), 'r': rnd(30, 50), 
         'clicked': False, 
         'vx': rnd(-6, 6), 'vy': rnd(-3, 3),
         'ax': rnd(-2, 2), 'ay': rnd(-1, 1)}
    b['id'] = canv.create_oval(b['x'] - b['r'], 
                               b['y'] - b['r'], 
                               b['x'] + b['r'], 
                               b['y'] + b['r'], 
                               fill=choice(colors), width=0)
    balls[b['id']] = b
    
    if not is_stopped:
        root.after(1000, del_ball, b)
        root.after(200, new_ball)


def click(event):
    global points, goldfish, is_stopped
    if not is_stopped:
        keys = list(balls.keys())
        for k in keys:
            if (((balls[k]['x'] - event.x)**2 +
                    (balls[k]['y'] - event.y)**2)**0.5 <= balls[k]['r']) \
                    and not balls[k]['clicked']:
                balls[k]['clicked'] = True
                points += 1
                del_ball(balls[k])  
        if (abs(goldfish['x'] - event.x) <= goldfish['a']) \
                and (abs(goldfish['y'] - event.y) <= goldfish['a']) \
                and not goldfish['clicked']:
            goldfish['clicked'] = True
            points += 20
        l['text'] = points


def movement_loop():
    global is_stopped
    keys = list(balls.keys())
    for k in keys:
        canv.move(balls[k]['id'], balls[k]['vx'], balls[k]['vy'])
        balls[k]['x'] += balls[k]['vx']
        balls[k]['y'] += balls[k]['vy']
        balls[k]['vx'] += balls[k]['ax']
        balls[k]['vy'] += balls[k]['ay']

    if not is_stopped:    
        root.after(50, movement_loop) 


def hit_check():
    global is_stopped
    keys = list(balls.keys())
    for k in keys:
        if balls[k]['x'] < balls[k]['r'] \
                or balls[k]['x'] > 800 - balls[k]['r']:
            balls[k]['vx'] = -balls[k]['vx']
            balls[k]['ax'] = -balls[k]['ax']
        if balls[k]['y'] < balls[k]['r'] \
                or balls[k]['y'] > 550 - balls[k]['r']:
            balls[k]['vy'] = -balls[k]['vy']
            balls[k]['ay'] = -balls[k]['ay']

    if not is_stopped:        
        root.after(10, hit_check)


l = Label(root, bg='grey', fg='white', width=10, font=("impact", 44))
l['text'] = 0
e = Entry(root)
name = ''


def stop_game(event):
    global is_stopped, enter_name
    #root.destroy()
    is_stopped = True
    canv.delete(ALL)
    root.after(500, canv.delete, ALL)
    

def get_name(event):
    global e, name, is_stopped
    if is_stopped:
        name = e.get() + ' - ' + str(points) + '\n'
        #l['text'] = name
        leader_file = open('leaderboard.txt', 'a')
        leader_file.write(name)
        leader_file.close()


#if is_stopped:
e = Entry(root, bg="black", bd=50, fg="white", font=("impact", 22), 
        width=100)
e.pack()
enter_name = Label(root, text="Enter your name",
        justify=CENTER, font="Impact 20")
enter_name.pack()


l.pack()
canv.bind('<Button-3>', start_game)
canv.bind('<Button-1>', click)
root.bind('<Escape>', stop_game)
root.bind('<Return>', get_name)
mainloop()
