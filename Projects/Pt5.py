# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle
import math
import time
import random


def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(
		    f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(
		    f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")


def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)


def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x, y)
    window.update()
    return sprite


def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)


def draw_rectangle(color="black", x=0, y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)


# Section 2: Setup
lebron_points = 0
speed_points = 0
fast = create_sprite("speed", -300, -300)
basketball = create_sprite("Lebron", 300, 300)
set_background("green")
# TODO - set the starting value for your variable


def move_up():
    fast.setheading(90)
    fast.forward(5)


def move_down():
    fast.setheading(270)
    fast.forward(5)


def move_left():
    fast.setheading(180)
    fast.forward(5)


def move_right():
    fast.setheading(0)
    fast.forward(5)


def move_uplebron():
    basketball.setheading(90)
    basketball.forward(5)


def move_downlebron():
    basketball.setheading(270)
    basketball.forward(5)


def move_leftlebron():
    basketball.setheading(180)
    basketball.forward(5)


def move_rightlebron():
    basketball.setheading(0)
    basketball.forward(5)


window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

window.onkeypress(move_uplebron, "Up")
window.onkeypress(move_downlebron, "Down")
window.onkeypress(move_leftlebron, "Left")
window.onkeypress(move_rightlebron, "Right")


# Section 3: Controls
# TODO - define your controls
# TODO - pick keys for each control

# Section 4: Game Loop
window.listen()
timer = 0
while True:
    time.sleep(0.00000000001)
    timer += 1
    get_distance(basketball, fast)
    if get_distance(basketball, fast) < 50:
        lebron_points += 1
    window.update()
    
    if lebron_points > 2:
         print ("tagger wins")
         break
