import graphics as gr

SIZE_X = 1080
SIZE_Y = 720

window = gr.GraphWin("Animation_Win", SIZE_X, SIZE_Y)

def add_coords(point_1, point_2):
    total = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return total

def sub_coords(point_1, point_2):
    total = gr.Point(point_1.x - point_2.x, point_1.y - point_2.y)
    return total



main()