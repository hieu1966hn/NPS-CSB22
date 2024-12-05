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

# move to center
penup()
left(90)
forward(50)
left(90)
forward(50)

# move to new square corner
left(45)
forward(50)
left(90)
forward(50)
left(90)
pendown()

# draw square
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

# move to center
penup()
left(90)
forward(50)
left(90)
forward(50)
left(45)

mainloop()