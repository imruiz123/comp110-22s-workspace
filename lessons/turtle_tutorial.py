from turtle import Turtle, colormode
leo: Turtle = Turtle()

bob: Turtle = Turtle() 

bob.penup()
bob.goto(60, 105)
bob.pendown()

leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)

leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.color(99, 204, 250)
colormode(255)

leo.begin_fill()
leo.end_fill()

leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")

leo.speed(50)
leo.hideturtle()