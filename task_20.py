#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    for i in range(12):
    	for i in range(27):
    		fill_cell()
    		move_right()
    	move_down()
    	for i in range(27):
    		move_left()


if __name__ == '__main__':
    run_tasks()
