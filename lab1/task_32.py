#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
	was_filled=0
	#if cell_is_filled():
		#was_filled+=1
	#else:
		#fill_cell()
		#wall_is_beneath()
	while wall_is_beneath():
		if wall_is_above() and wall_is_beneath():
			if cell_is_filled():
				was_filled+=1
			else:
				fill_cell()
		if not wall_is_above():
			while not wall_is_above():
				move_up()
				if cell_is_filled():
					was_filled+=1
				else:
					fill_cell()
			while not wall_is_beneath():
				move_down()
		move_right()
	#while wall_is_beneath():
		#move_left()
	#move_right()
	#print(ax)
	mov("ax",was_filled)

if __name__ == '__main__':
    run_tasks()
