import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

cars = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_car()
    cars.move_cars()
    score.write_level()
    
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
         
    if player.is_at_finish_line():
         player.go_to_start()
         score.increase_level()
         cars.level_up()
           
screen.exitonclick()