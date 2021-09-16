FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.hideturtle()
        self.goto(-275, 260)
        self.write_level()
    
    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font= FONT)
    
    def increase_level(self):
        self.level += 1
        self.write_level()
        
    def game_over(self):
        self.penup()
        self.goto(-70, 0)
        self.write(f"GAME OVER", font= FONT)
        