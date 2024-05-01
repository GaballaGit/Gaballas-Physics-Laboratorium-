import turtle
import math

window = turtle.Screen()
window.bgcolor(50/255, 50/255, 50/255)

main_dot = turtle.Turtle()
main_dot.pensize(3)
main_dot.shape("circle")
main_dot.color(0,1,0)
main_dot.pendown()
main_dot.setposition(0, 0)

x = 0
y = 0
while True:
    if x >= math.pi*2:
        x = 0
        y = 0 
    else:
        x += 0.1
        y += 0.1
    # setposition(x,y)
    main_dot.setposition(math.cos(y)*100,math.sin(x)*100)

turtle.done()