#!/usr/bin/python3

from pyrob.api import *

def cell_top():
    move_up()
    fill_cell()
    move_down()
    
    
def cell_down():
    move_down()
    fill_cell()
    move_up()
    
def check_fill():
    if not wall_is_above():
    	cell_top()
    if not wall_is_beneath():
    	cell_down()
    if wall_is_above() and wall_is_beneath():
    	fill_cell()

@task
def task_8_11():
    while not wall_is_on_the_right():
    	check_fill()
    	move_right(n=1)
    check_fill()


if __name__ == '__main__':
    run_tasks()
