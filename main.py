import turtle
screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("tan")

t = turtle.Turtle()


t.speed(0)
t.pencolor("black")
t.penup()
t.goto(0, 0)
t.pendown()
t.circle(35)

t.pencolor("blue")
t.penup()
t.goto(-75,0)
t.pendown()
t.circle(35)


t.pencolor("red")
t.penup()
t.goto(75,0)
t.pendown()
t.circle(35)

t.pencolor("green")
t.penup()
t.goto(35,-45)
t.pendown()
t.circle(35)

t.pencolor("yellow")
t.penup()
t.goto(-35,-45)
t.pendown()
t.circle(35)

t.pencolor("purple")
t.penup()
t.goto(0,100)
t.pendown()
t.write("Winter Olympics",font=("Arial",60,'normal'),align="center")

t.pencolor("purple")
t.penup()
t.goto(0,-150)
t.pendown()
t.write("2026",font=("Arial",60,'normal'),align="center")





t.hideturtle()
turtle.done()