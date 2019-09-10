#!/usr/bin/python3

from pyrob.api import *

def draw_cross():
	move_right()
	fill_cell()
	move_down()
	fill_cell()
	move_right()
	fill_cell()
	move_down()
	move_left()
	fill_cell()
	move_up()
	move_left()
	fill_cell()
	move_up()

@task
def task_2_2():
    move_down()
    for i in range(4):
    	draw_cross()
    	move_right(n=4)
    draw_cross()


if __name__ == '__main__':
    run_tasks()
