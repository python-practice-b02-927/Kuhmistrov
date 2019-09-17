#!/usr/bin/python3

from pyrob.api import *

def Go_to_the_left():
	while not wall_is_on_the_left():
		move_left()

@task(delay=0.001)
def task_8_30():
	Go_to_the_left()
	while not(wall_is_on_the_right() and wall_is_beneath()):
		move_right()
		if not wall_is_beneath():
			move_down()
			Go_to_the_left()
	Go_to_the_left()




if __name__ == '__main__':
    run_tasks()
