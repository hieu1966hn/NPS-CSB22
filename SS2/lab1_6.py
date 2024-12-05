from turtle import *

shape('turtle')

# draw square
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

## Move to start bigger square
penup()
forward(10)
left(90)
pendown()

## draw bigger square
pensize(3)
forward(110)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(120)
left(90)

# Chèn nhấc bút lên ở đây cũng được
forward(60)
left(90)

## Move to center bigger square
penup()
forward(60)
pendown()


mainloop()