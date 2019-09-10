#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    a=0
    f=True
    while not wall_is_on_the_right() and f and (a!=3):
    	move_right()
    	if a==3:
    		f=False
    	elif cell_is_filled():
    		a+=1
    	else:
    		a=0



if __name__ == '__main__':
    run_tasks()
