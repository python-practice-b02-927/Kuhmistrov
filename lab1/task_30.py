#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    a=0
    while not wall_is_on_the_right():
    	move_right()
    	a+=1
    move_left(n=a)
    a+=1
    
    
    for i in range(1,a,1):
    	for j in range(1,a,1):
    		if (not i==j) and (not i+j==a+1):
    			fill_cell()
    		move_right()
    	j+=1
    	if (not i==j) and (not i+j==a+1):
    		fill_cell()
    	move_left(n=a-1)
    	move_down()
    i=a	
    for j in range(1,a,1):
    	if (not i==j) and (not i+j==a+1):
    		fill_cell()
    	move_right()
    j+=1
    if (not i==j) and (not i+j==a+1):
    	fill_cell()
    move_left(n=a-1)




if __name__ == '__main__':
    run_tasks()
