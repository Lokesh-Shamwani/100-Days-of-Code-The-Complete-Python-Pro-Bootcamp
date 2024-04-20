import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            x_pos = 300
            y_pos = random.randint(-240, 240)
            new_car.goto(x=x_pos, y=y_pos)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for each_car in self.all_cars:
            each_car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
