#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    f=False
    while not wall_is_on_the_left() and not f:
    	move_left()
    if not wall_is_above() and not f:
    		f=True
    		move_up()
    while not wall_is_on_the_right() and not f:
    	move_right()
    	if not wall_is_above():
    		f=True
    		move_up()
    if f:
    	while not wall_is_on_the_left():
    		move_left()
    	while not wall_is_above():
    		move_up()



if __name__ == '__main__':
    run_tasks()
