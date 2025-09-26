import turtle
import colorsys


turtle.bgcolor('black')
turtle.speed(0)
turtle.hideturtle()
turtle.colormode(255)

num_colors = 36
colors = [colorsys.hsv_to_rgb(i/num_colors, 1, 1) for i in range(num_colors)]


for i in range(360):
    color = colors[i % num_colors]
    turtle.pencolor(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
    turtle.circle(i, 60)
    turtle.left(59)


turtle.done()