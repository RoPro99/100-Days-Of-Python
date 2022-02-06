import turtle
from turtle import Turtle ,Screen
import  random
tim = Turtle()
tim.shape("turtle")
#tim.color("OrangeRed1")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# timmy_teh_turtle.forward(100)
# timmy_teh_turtle.forward(100)
# timmy_teh_turtle.right(90)
# timmy_teh_turtle.forward(100)
# timmy_teh_turtle.right(90)
# timmy_teh_turtle.forward(100)
# timmy_teh_turtle.right(90)
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
turtle.colormode(255)
# colours = ["CornflowerBlue", "IndianRed", "DeepSkyBlue", "wheat", "SeaGreen", "DarkOrchid", "OrangeRed1"]
directions = [0, 90, 180, 270]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side)
def random_color():
    r= random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r , g , b)
    return color
#tim.pensize(15)
tim.speed("fastest")
# for _ in range(500):
#     tim.forward(30)
#     tim.color(random_shape())
#     tim.setheading(random.choice(directions))
def draw_spriograpgh(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
            tim.color(random_color())
            tim.circle(100)
            tim.setheading(tim.heading() + size_of_gap)


draw_spriograpgh(5)







screen = Screen()
screen.exitonclick()
