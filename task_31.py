#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
	cango=True
	while not wall_is_on_the_left():
		move_left()
	while cango:
		f=False
		while not wall_is_on_the_right():
			if not wall_is_beneath():
				f=True
			move_right()
		if not wall_is_beneath():
			f=True
		while not wall_is_on_the_left():
			move_left()
		if f:
			while not wall_is_on_the_right():
				if not wall_is_beneath():
					move_down()
					while not wall_is_on_the_left():
						move_left()
				move_right()
			if not wall_is_beneath():
				move_down()
				while not wall_is_on_the_left():
					move_left()
		else:
			cango=f




if __name__ == '__main__':
    run_tasks()
