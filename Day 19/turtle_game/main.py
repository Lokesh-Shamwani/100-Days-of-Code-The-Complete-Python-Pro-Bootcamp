from turtle import Turtle, Screen
import random

is_race_on = False

my_screen = Screen()
my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
if user_bet:
    is_race_on = True

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
ypos_gap = 35

for i in range(len(colors)):
    new_timmy = Turtle(shape="turtle")
    new_timmy.penup()
    new_timmy.color(colors[i])
    new_timmy.goto(x=-230, y=-80 + (ypos_gap) * i)
    turtles.append(new_timmy)


while is_race_on:
    for a_turtle in turtles:
        if not a_turtle.xcor() > 230:
            rand_distance = random.randint(0, 10)
            a_turtle.forward(rand_distance)
        else:
            is_race_on = False
            winner = a_turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")


my_screen.exitonclick()
