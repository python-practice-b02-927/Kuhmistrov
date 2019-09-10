#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    a=0
    while a<5:
    	move_right()
    	if cell_is_filled():
    		a+=1


if __name__ == '__main__':
    run_tasks()
