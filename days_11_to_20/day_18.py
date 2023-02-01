# from turtle import Turtle, Screen
# import random
# import turtle

# def move_forward(distance):
#     timmy_the_turtle.fd(distance)

# turtle.colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("purple")
# t = timmy_the_turtle
# # for _ in range(1,5):
# #     move_forward(50)
# #     timmy_the_turtle.right(90)
# # for _ in range(1,51):
# #     t.fd(10)
# #     t.penup()
# #     t.fd(10)
# #     t.pendown()


# # def draw_shapes(num_shapes):
# #     sides = 3
# #     count = 0
# #     while count < num_shapes:
# #         for _ in range(sides):
# #             angle = 360 / sides
# #             t.fd(100)
# #             t.right(-angle)
# #         count += 1
# #         sides += 1
    
# # draw_shapes(8)



# def random_walk():
#     for _ in range(500):
#         t.color(random_color())
#         x_heading = random.choice([-1, 1])
#         y_heading = random.choice([-1, 1])
#         pensize = random.randint(1,11)
#         t.pensize(pensize)
#         t.fd(50 * x_heading)
#         t.right(90 * x_heading)

# # random_walk()

# t.speed("fastest")
# def spiral(gap):
#     for _ in range(int(360 / gap)):
#         t.color(random_color())
#         t.circle(100)
#         t.seth(t.heading() + gap)


# spiral(1)
# screen = Screen()
# screen.exitonclick()

# # tuples
# my_tuple = (1,2,3)


#Hirst painting 
# import colorgram
from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)

# #extract colors
# rgb_colors = []
# colors = colorgram.extract("hirst.jpeg",18)
# print(colors)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

colors = [(182, 7, 45), (215, 222, 235), (159, 97, 30), (23, 95, 185), (237, 243, 239), (193, 157, 91), (246, 216, 53), (218, 145, 175), (245, 236, 240), (178, 200, 7), (68, 154, 95), (125, 43, 124), (73, 56, 50), (86, 54, 49), (70, 144, 93), (128, 159, 199), (230, 168, 185)]

t = Turtle()
t.penup()

def random_color(colors):
    return random.choice(colors)

def draw_dots(number, size, distance):
    for _ in range(number):
        t.dot(size, random_color(colors))
        t.fd(distance)

def draw_grid(x, y, z):
    """x = number of columns, y = number of rows, x = spacing between dots"""
    for _ in range(y):
        draw_dots(x, 20, z)
        position = t.pos()
        t.setpos(0, position[1] + z)

draw_grid(10, 10, 50)
screen = Screen()
screen.exitonclick()

