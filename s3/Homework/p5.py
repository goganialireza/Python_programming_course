import turtle

turtle.colormode(255)
turtle.getscreen()
t = turtle.Turtle()
t.speed(-1)


x = 100

for i in range(90):
    t.forward(x)
    t.backward(x*2)
    t.forward(x)
    t.left(1)



