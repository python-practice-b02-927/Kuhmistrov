import graphics as gr

width=1000
height=600

def draw_eye(window,coords):
	pass

def draw_nose(window,coords):
	pass

def draw_mounth(window,coords):
	pass

def draw_curl(window,coords, angle):	
	pass

#передаем координаты и радиус лица
def draw_hair(window,coords, radius):
	pass

def draw_face(window):
	pass

def draw_body(window):
	body=gr.Circle(gr.Point(width/2,height+100),250)
	body.setFill('orange')
	body.draw(window)

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
	left_arm=gr.Polygon(gr.Point(310,550),gr.Point(120,225),gr.Point(140,210),gr.Point(340,540))
	left_arm.setFill('yellow')
	left_arm.draw(window)

#Правая рука будет зеркальным отражением левого

def draw_right_arm(window):
	rigth_arm=gr.Polygon(gr.Point(690,550),gr.Point(880,225),gr.Point(860,210),gr.Point(660,540))
	rigth_arm.setFill('yellow')
	rigth_arm.draw(window)

#Конец зеркальных элементов-функций

def draw_poster(window):
	pass

def main(window):
	#Рисуем фон
	background=gr.Rectangle(gr.Point(0,0),gr.Point(width,height))
	background.setFill("black")
	background.draw(window)

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

window=gr.GraphWin("Window",width,height)

main(window)
window.getMouse()
window.close()