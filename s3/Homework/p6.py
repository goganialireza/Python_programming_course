import turtle
turtle.getscreen()
t = turtle.Turtle()
t.speed(-1)


x = 20

for i in range(10):
    for j in range(4):
        t.forward(x)
        t.left(90)
    x += 20




