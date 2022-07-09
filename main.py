import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(car.car_speed)
    screen.update()
    car.create_car()
    car.move()

    # Detect collision with the car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            player.reset_position()
            score.reset()

    # Detect when player hits the end of the screen
    if player.ycor() > player.finish_line:
        # Move the player to its starting position
        player.reset_position()
        # Add a point to score
        score.add_point()
        # Increase car speed
        car.increase_speed()

screen.exitonclick()
