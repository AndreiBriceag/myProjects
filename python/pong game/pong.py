import turtle
import winsound

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_1 = 0
score_2 = 0

# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 | Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Func
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20 #moves up 20px
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20 #moves down 20px
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20 #moves up 20px
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20 #moves down 20px
    paddle_right.sety(y)

# Keyboard bindings for paddles movement
window.listen()
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")

# Main loop
while True:
    window.update()
    
    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("pong game/bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("pong game/bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score_1,score_2), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score_1,score_2), align="center", font=("Courier", 24, "normal"))

# bounce on paddles
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pong game/bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pong game/bounce.wav", winsound.SND_ASYNC)