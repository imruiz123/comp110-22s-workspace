from turtle import Turtle, colormode, done 
colormode(255)
leo: Turtle = Turtle()

bob: Turtle = Turtle() 
colormode(250)

bob.forward(300)
bob.left(90)
bob.forward(300) 
bob.left(90)
bob.forward(300)
bob.left(90)
bob.forward(300) 
bob.left(90) 

bob.penup()
bob.goto(60, 105)
bob.pendown()

side_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length * 0.97)
    bob.left(123)
    i = i + 1
bob.fillcolor(23, 65, 100)

bob.speed(65)
bob.hideturtle()


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

leo.fillcolor(32, 67, 94) 

leo.begin_fill()
j: int = 0
while (j < 4):
    leo.forward(300)
    leo.left(120)
    j = j + 1
leo.end_fill()


done()
leo.speed(50)
leo.hideturtle()