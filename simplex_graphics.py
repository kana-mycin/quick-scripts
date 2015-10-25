from turtle import *
from math import *
import time

def generate_points(n, radius):
	listu = []
	increment = 360/n
	for i in range(0, n):
		rads = radians(increment*i)
		listu += [(radius*sin(rads), radius*cos(rads))]
	return listu
turtle = Turtle()
turtle.speed(0)
num_points = 30
radius = 200
da_list = generate_points(num_points, radius)
turtle.pensize(1)
turtle.penup()
for i in range(0, num_points):
	current_point = da_list.pop(0)
	for other in da_list:
		turtle.goto(current_point[0], current_point[1])
		turtle.pendown()
		turtle.goto(other[0], other[1])
		turtle.penup()

while(True):
	print('potato')
	time.sleep(5)
