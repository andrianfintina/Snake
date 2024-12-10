from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.show_score()
    
    def show_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
