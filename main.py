import colorgram
from turtle import Turtle, Screen, colormode
import random

# # Extract rgb colors using colorgram
# # rgb_colors = []

# # colors = colorgram.extract("painting.jpg", 30)

# # for color in colors:
# #     r = color.rgb.r
# #     g = color.rgb.g
# #     b = color.rgb.b
# #     new_color = (r, g, b)
# #     rgb_colors.append(new_color)

# # print(rgb_colors)

# # Colors extracted from painting.jpg
color_list = [(55, 99, 155), (149, 70, 98), (232, 137, 61), (244, 238, 242), (108, 174, 211), (118, 82, 58), (201, 146, 177), (199, 77, 110), (146, 134, 71), (229, 90, 59), (140, 192, 139),
              (73, 102, 89), (67, 162, 92), (6, 165, 179), (227, 161, 184), (166, 195, 219), (115, 126, 142), (11, 68, 129), (189, 17, 29), (4, 58, 112), (231, 173, 162), (172, 203, 177), (164, 199, 215), (169, 27, 24), (76, 58, 43), (86, 60, 39)]

screen = Screen()
timmy = Turtle()
colormode(255)
timmy.pensize(10)
timmy.penup()
timmy.setpos(-360, 300)


def paint(space, num):
    for i in range(num):
        for j in range(num):

            # dot
            timmy.dot(20, random.choice(color_list))

            # distance for another dot
            timmy.forward(space)
        timmy.backward(space * num)

        # direction
        timmy.right(90)
        timmy.forward(space)
        timmy.left(90)


# Main Section
timmy.penup()
paint(40, 10)

# hide the turtle
timmy.hideturtle()
