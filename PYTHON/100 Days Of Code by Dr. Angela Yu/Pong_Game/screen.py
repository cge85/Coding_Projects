from turtle import Screen

class Gamescreen(Screen):
    def __init__(self):
        super().__init__()
        self.screen = Screen()

    def game_screen(self):
        self.screen.screensize(1000, 1000)
        # self.screen.bgcolor("black")
        self.screen.exitonclick()