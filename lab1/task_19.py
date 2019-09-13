#!/usr/bin/python3

from pyrob.api import *

def go_to_the_corner():
	while not wall_is_above():
		move_up()
	while not wall_is_on_the_left():
		move_left()
@task
def task_8_29():
    did_robot_leave=False
    while not wall_is_on_the_left():
    	move_left()
    if not wall_is_above():
    	go_to_the_corner()
    	did_robot_leave=True
    while not wall_is_on_the_right() and not did_robot_leave:
    	move_right()
    if not wall_is_above() and not did_robot_leave:
    	go_to_the_corner()



if __name__ == '__main__':
    run_tasks()
