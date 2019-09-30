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
    absolute_velocity = absolute_value(velocity)
    angular_acceleration = (g * mass * radius_vector.x) / (distance * moment_of_inertia)

    normal_acceleration = gr.Point(((-1) * radius_vector.x * absolute_velocity**2)/(distance**2),
    ((-1) * radius_vector.y * absolute_velocity**2)/(distance**2))

    tangential_acceleration = gr.Point(angular_acceleration * (-1) * radius_vector.y, angular_acceleration * radius_vector.x)

    return add(normal_acceleration,tangential_acceleration)

def recount_pendulum_angle(pendulum_coords, center_coords):
    radius_vector = sub(pendulum_coords, center_coords)
    distance = absolute_value(radius_vector)
    return radius_vector.x/distance




main()