# Testing out the turtle module

import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')

"""
slowpoke.forward(100)
slowpoke.right(90)
slowpoke.forward(100)
slowpoke.right(90)
slowpoke.forward(100)
slowpoke.right(90)
slowpoke.forward(100)
"""
i = 0
while i < 4:
    slowpoke.forward(100)
    slowpoke.right(90)
    i+=1

turtle.mainloop()