import graphics as gr
import math

SIZE_X = 1080
SIZE_Y = 720

#acceleration of gravity
g=10

window = gr.GraphWin("Animation_Win", SIZE_X, SIZE_Y)

background = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
background.setFill('black')
background.draw(window)

def add_coords(point_1, point_2):
    total = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return total

def sub_coords(point_1, point_2):
    total = gr.Point(point_1.x - point_2.x, point_1.y - point_2.y)
    return total

def absolute_value(vector):
    result = (vector.x**2 + vector.y**2)**0.5
    return result

def recount_coords(coords, velocity):
    return add_coords(coords,velocity)

def recount_velocity(velocity, acceleration):
    return add_coords(velocity, acceleration)

def recount_acceleration(pendulum_coords, center_coords, velocity, moment_of_inertia, mass):
    radius_vector = sub_coords(pendulum_coords, center_coords)
    distance = absolute_value(radius_vector)
    absolute_velocity = absolute_value(velocity)
    angular_acceleration = (g * mass * radius_vector.x) / (distance * moment_of_inertia)

    normal_acceleration = gr.Point(((-1) * radius_vector.x * absolute_velocity**2)/(distance**2),
    ((-1) * radius_vector.y * absolute_velocity**2)/(distance**2))

    tangential_acceleration = gr.Point(angular_acceleration * (-1) * radius_vector.y, angular_acceleration * radius_vector.x)

    return add_coords(normal_acceleration,tangential_acceleration)

def recount_pendulum_angle(pendulum_coords, center_coords):
    radius_vector = sub_coords(pendulum_coords, center_coords)
    distance = absolute_value(radius_vector)
    return radius_vector.x/distance

def drawing_pendulum(pendulum_coords, pendulum_angle, pendulum_side):
    c=pendulum_coords
    a=pendulum_angle
    s=pendulum_side / 1.41
    pendulum = gr.Polygon(gr.Point((c.x - s*math.sin(math.pi/4 - a)),(c.y - s*math.cos(math.pi/4 - a))),
               gr.Point((c.x + s*math.cos(math.pi/4 - a)),(c.y - s*math.sin(math.pi/4 - a))),
               gr.Point((c.x + s*math.sin(math.pi/4 - a)),(c.y + s*math.cos(math.pi/4 - a))),
               gr.Point((c.x - s*math.cos(math.pi/4 - a)),(c.y + s*math.sin(math.pi/4 - a))))
    #pendulum = gr.Circle(pendulum_coords, pendulum_side)
    pendulum.setFill('white')
    pendulum.undraw()


#main body begins there ->

pendulum_coords = gr.Point(540, 480)
center_coords = gr.Point(540, 360)
velocity = gr.Point(5, 0)
pendulum_side = 60
distance = absolute_value(sub_coords(pendulum_coords,center_coords))
mass = 200
moment_of_inertia = mass * (pendulum_side**2/12 + distance**2)

kernel = gr.Line(center_coords,pendulum_coords)
kernel.setFill('white')
kernel.setWidth(3)
kernel.draw(window)

pendulum = gr.Rectangle(gr.Point(480,540),gr.Point(600,420))
pendulum.setFill('white')
pendulum.draw(window)

while True:
        pendulum_coords = recount_coords(pendulum_coords, velocity)
        kernel.undraw()
        kernel = gr.Line(pendulum_coords, center_coords)
        kernel.setFill('white')
        kernel.setWidth(3)
        kernel.draw(window)

        drawing_pendulum(pendulum_coords, recount_pendulum_angle(pendulum_coords, center_coords), pendulum_side)
        acceleration = recount_acceleration(pendulum_coords, center_coords, velocity, moment_of_inertia, mass)
        velocity = recount_velocity(velocity, acceleration)

        gr.time.sleep(0.02)    