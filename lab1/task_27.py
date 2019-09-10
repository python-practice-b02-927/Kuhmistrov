#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
	f=True
	a=1
	move_right()
	while f:
		fill_cell()
		for i in range(a):
			if wall_is_on_the_right():
				f=False
				break
			move_right()
		a+=1	
	if i+1==a:
		fill_cell()

if __name__ == '__main__':
    run_tasks()
