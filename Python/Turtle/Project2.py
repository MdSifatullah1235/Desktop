import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(400,600)

triangle = turtle.Turtle()

for i in range(3):
    triangle.forward(70)
    triangle.left(120)

turtle.done()