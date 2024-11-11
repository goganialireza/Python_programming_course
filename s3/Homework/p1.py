import turtle

turtle.colormode(255)
turtle.getscreen()
t = turtle.Turtle()
t.speed(-1)


x = 1

for i in range(20):
    t.forward(x)
    t.left(90)
    x += 12

