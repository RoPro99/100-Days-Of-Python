# import  colorgram as cl
# rgb_colors = []
# colors  = cl.extract('image2.png', 40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import  turtle as tl
import random
tl.colormode(255)
tim = tl.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(0, 0, 0), (236, 186, 0), (195, 0, 56), (0, 76, 151), (254, 236, 2), (254, 254, 254), (105, 85, 0), (140, 113, 8),
              (0, 28, 56), (56, 0, 19), (236, 157, 28), (26, 62, 135), (221, 20, 52), (235, 117, 143), (234, 98, 29), (224, 46, 85), (238, 221, 2), (0, 1, 1)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numbers_of_dots = 100

for dot_count in range(1, numbers_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)







screen = tl.Screen()
screen.exitonclick()


