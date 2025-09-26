import turtle

# Set up the turtle screen
turtle.bgcolor("black")
turtle.speed(10)
turtle.width(2)

# Set up colors for the flower petals
colors = ["red", "yellow", "blue", "green", "purple", "orange"]

# Draw the flower
for i in range(36):
    turtle.color(colors[i % len(colors)])  # Alternate between the colors
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(100)
    turtle.left(10)  # Rotate to create the flower effect

# Hide the turtle after drawing
turtle.hideturtle()

# Finish the drawing
turtle.done()
