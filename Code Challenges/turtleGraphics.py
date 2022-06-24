def drawShape(how_far,how_much):
    if how_far>0:
        turtle.forward(how_far)
        turtle.right(how_much)
        drawShape(how_far-4,how_much)

import turtle
turtle.reset()
turtle.pen(speed=0)
turtle.delay(50)

length=500
turn_by=121
turtle.penup()
turtle.pencolor("blue")
turtle.bgcolor("black")
turtle.pensize(1.5)
turtle.setpos(-length/2,length/4)
turtle.pendown()

drawShape(length,turn_by)