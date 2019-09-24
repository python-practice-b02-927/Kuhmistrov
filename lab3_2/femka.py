import graphics as gr

wight=1000
height=600

def draw_eye(window,coords):
	pass

def draw_nose(window,coords):
	pass

def draw_mounht(window,coords):
	pass

def draw_curl(window,coords, angle):	
	pass

#передаем координаты и радиус лица
def draw_hair(window,coords, radius):
	pass

def draw_face(window):
	pass

def draw_body(window):
	pass

#Отражения

def draw_left_shoulder(window,coords):
	pass

#Правое плечо будет зеркальным отражением левого

def draw_right_shoulder(window,coords):
	pass

def draw_left_hand(window):
	pass

#Правая кисть будет зеркальным отражением левого

def draw_right_hand(window):
	pass

def draw_left_arm(window):
	pass

#Правая рука будет зеркальным отражением левого

def draw_right_arm(window):
	pass

#Конец зеркальных элементов-функций

def draw_poster(window):
	pass

def main(window):
	#Рисуем саму картинку
	draw_body(window)
	draw_right_arm(window)
	draw_left_arm(window)
	#Закомментировал чтобы скомпилировать, отсутствуют координаты
	#draw_left_shoulder(window)
	#draw_right_shoulder(window)
	draw_left_hand(window)
	draw_right_hand(window)
	draw_poster(window)
	draw_face(window)
	#draw_hair(window)

window 	= gr.GraphWin("Window", width, height)

main(window)
window.getMouse()
window.close()