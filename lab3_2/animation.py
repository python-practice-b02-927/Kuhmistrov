import graphics as gr

SIZE_X = 1080
SIZE_Y = 720

#acceleration of gravity
g=5

window = gr.GraphWin("Animation_Win", SIZE_X, SIZE_Y)

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
    return add(coords,velocity)

def recount_velocity(velocity, acceleration):
    return add(velocity, acceleration)

def recount_acceleration(pendulum_coords, center_coords, velocity, moment_of_inertia, mass):
    radius_vector = sub(pendulum_coords, center_coords)
    distance = absolute_value(radius_vector)

main()