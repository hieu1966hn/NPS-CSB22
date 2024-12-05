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

# move to start bigger square
penup()
forward(10)
left(90)
pendown()

# draw bigger square
pensize(3)
forward(110)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(10)

# move to center
penup()
forward(50)
left(90)
forward(60)

mainloop()