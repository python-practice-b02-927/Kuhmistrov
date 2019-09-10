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

def draw_row_of_cross():
    for i in range(9):
    	draw_cross()
    	move_right(n=4)
    draw_cross()
    move_left(36)

@task(delay=0.02)
def task_2_4():
    for i in range(4):
    	draw_row_of_cross()
    	move_down(4)
    draw_row_of_cross()




if __name__ == '__main__':
    run_tasks()
