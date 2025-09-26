import turtle

# screen = turtle.Screen()
t = turtle.Turtle()
# t.forward(100)
# t.right(90)
# t.forward(100)
# turtle.done()

turtle.bgcolor("black")
t.speed(0)
t.color("yellow")

for i in range(300):
    t.forward(i * 2)
    t.right(150)

turtle.done()