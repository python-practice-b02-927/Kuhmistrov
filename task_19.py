#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    f=False
    if not wall_is_above():
    		f=True;
    while not wall_is_on_the_left():
    	move_left()
    	if not wall_is_above():
    		f=True;
    while not wall_is_on_the_right() and not f:
    	move_right()
    	if not wall_is_above():
    		f=True;
    if f:
    	while not wall_is_above():
    		move_up()
    	while not wall_is_on_the_left():
    		move_left()
    else:
    	while not wall_is_on_the_right():
    		move_right()



if __name__ == '__main__':
    run_tasks()
