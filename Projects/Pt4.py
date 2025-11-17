#makes the red spiral
import turtle 
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t. goto(0,0)
t.color("crimson")
t.speed(100)

for i in range (700):
    t.forward(5 + i)
    t.left(73)

#makes the white spiral
import turtle 
t3 = turtle.Turtle()
t3.goto(2,2)
t3.color("white")
t3.speed(100)

for i in range (700):
    t3.forward(5 + i)
    t3.left(73)

#makes the green spiral
    import turtle 
t2 = turtle.Turtle()
t2.goto(4,4)
t2.color("green")
t2.speed(100)

for i in range (700):
    t2.forward(5 + i)
    t2.left(73)

turtle.exitonclick()
