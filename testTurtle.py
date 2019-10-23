import turtle
def turn(x,y):
    turtle.left(45)
turtle.penup()
turtle.goto(-300,240)
turtle.pendown()
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.onclick(turn)
