import turtle
import time
from food import *
from snake import *

win = turtle.Screen()
win.title("Snake Game")
width = 500
height = 500
win.setup(width=width, height= height)
win.bgcolor("orange")

snake = Snake(0,0)
win.listen()
win.onkey(snake.keyUp,"w")
win.onkey(snake.keyDown,"s")
win.onkey(snake.keyLeft,"a")
win.onkey(snake.keyRight,"d")

win.onkey(snake.keyUp,"Up")
win.onkey(snake.keyDown,"Down")
win.onkey(snake.keyLeft,"Left")
win.onkey(snake.keyRight,"Right")

food = Food()

while True:
    win.update()
    time.sleep(0.094)
    snake.Move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.Extend()

    if snake.CheckSelfCollision() or snake.checkWallsCollision(width,height):
        food.refresh()
        snake.refresh()
        

win.mainloop()
