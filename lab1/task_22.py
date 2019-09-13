#!/usr/bin/python3

from pyrob.api import *

def fill_line():
    while not wall_is_on_the_right():
    	move_right()
    	fill_cell()
    while not wall_is_on_the_left():
    	move_left()

@task
def task_5_10():
    fill_cell()
    fill_line()
    while not wall_is_beneath():
    	move_down()
    	fill_cell()
    	fill_line()



if __name__ == '__main__':
    run_tasks()
