#Day 19
# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.fd(10)

# def move_backwards():
#     tim.back(10)

# def move_left():
#     new_heading = tim.heading() + 10
#     tim.seth(new_heading)

# def move_right():
#     new_heading = tim.heading() - 10
#     tim.seth(new_heading)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(key="p", fun=move_forwards)
# screen.onkey(key="o", fun=move_backwards)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="e", fun=move_right)
# screen.onkey(key="c", fun=clear)

# screen.exitonclick()
from turtle import Turtle, Screen
import random
race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def random_walk():
    return random.randint(0,16)

starting_y = -180
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=starting_y )
    starting_y += 60
    turtles.append(new_turtle)

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        turtle.fd(random_walk())
        if turtle.xcor() >= 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! {winner} turtle is the winner!")
            else:
                print(f"You lose! {winner} turtle is the winner!")
            


    



screen.exitonclick()
