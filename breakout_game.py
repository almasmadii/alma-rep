from turtle import Screen,Turtle
import time
import random
#breakout game

#screen
screen=Screen()
screen.bgcolor("black")
screen.title("Breakout")
screen.setup(width=800,height=600)
screen.tracer(0)

#paddle
paddle=Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=1,stretch_len=10)
paddle.color("blue")
paddle.penup()
paddle.goto(y=-250,x=0)

def go_right():
    new_x=paddle.xcor() + 21
    paddle.goto(new_x,paddle.ycor())

def go_left():
    new_x=paddle.xcor() - 21
    paddle.goto(new_x,paddle.ycor())

screen.listen()
screen.onkey(go_right,"Right")
screen.onkey(go_left,"Left")

#ball

ball=Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.x_move=10
ball.y_move=10

def move():
    new_x=ball.xcor() + ball.x_move
    new_y=ball.ycor() + ball.y_move
    ball.goto(new_x,new_y)

def bounce_x():
    ball.x_move *=- 1
def bounce_y():
    ball.y_move *= -1
def reset_pos():
    ball.goto(0,0)
    bounce_y()
#bricks
bricks=[]
colors=["red","orange","yellow","pink","green","purple","blue"]
x= -200
y= 300
for i in range(30):
    brick=Turtle()
    brick.shape("square")
    brick.color(random.choice(colors))
    brick.shapesize(stretch_wid=2, stretch_len=4)
    brick.penup()
    x = -300 + (i % 7) * 90
    y = 250 - (i // 7) * 50
    brick.goto(x=x,y=y)
    bricks.append(brick)



#scoreboard
scoreboard=Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.score=0
scoreboard.goto(0,-280)
scoreboard.write(scoreboard.score,align="center",font=("Courier",20,"normal"))
def update_scoreboard():
    scoreboard.clear()
    scoreboard.score+=1
    scoreboard.write(scoreboard.score,align="center",font=("Courier",20,"normal"))

game_is_on=True
while game_is_on:
    for brick in bricks:
        if ball.distance(brick) < 50:
            brick.hideturtle()
            brick.goto(1000,1000)
            bricks.remove(brick)
            bounce_y()
            update_scoreboard()

    time.sleep(0.1)
    move()
    screen.update()
    #detect collision
    if ball.ycor()>280 :
        bounce_y()
    elif ball.xcor() > 380 or ball.xcor() < -380:
        bounce_x()
    #detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -220:
        bounce_y()
    if ball.ycor() < -280:
        game_is_on=False

game_over=Turtle()
game_over.color("red")
game_over.write("Game Over ",align="center",font=("Courier",70,"normal"))
scoreboard.goto(0,-100)
scoreboard.write(f"Score = {scoreboard.score}",align="center",font=("Courier",70,"normal"))
screen.exitonclick()