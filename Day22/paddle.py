from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        return self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        return self.goto(self.xcor(), self.ycor() - 20)
