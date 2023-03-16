import turtle  as t
import random


schiggy = t.Turtle()
t.colormode(255)
schiggy.speed("fastest")

'''_______________________________Function______________________________________________'''


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r , g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        schiggy.color(random_colour())
        schiggy.circle(100)
        schiggy.setheading(schiggy.heading() + size_of_gap)


'''________________________________________________'''


draw_spirograph(5)
