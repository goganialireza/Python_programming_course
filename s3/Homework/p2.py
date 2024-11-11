import turtle

turtle.colormode(255)
turtle.getscreen()
t = turtle.Turtle()
t.speed(-1)


x = 100

for i in range(270):
    t.forward(x)
    t.backward(x)
    t.left(1)



