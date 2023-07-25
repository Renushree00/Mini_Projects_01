import turtle
import winsound

gm = turtle.Screen()
gm.title("Pong")
gm.setup(width=800, height=600)
gm.bgcolor("black")
gm.tracer(0)
# It stops the window from updating and we have to manually update it. It speeds up a game quite a bit.

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
# Here, turtle is a module and Trutle is a class.
paddle_a.speed(0)
# It sets the speed to the max. possible speed.
paddle_a.shape('square')
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color("white")
ball.penup()
ball.goto(0, 0)
# d means delta(change). Every times the ball moves it moves by 0.1 px.
ball.dx = 0.1
ball.dy = -0.1

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center', font=('Courier', 20, 'normal'))

# Function for paddle a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20             # It will move the paddle 20 px upward
    paddle_a.sety(y)    # set y as new y

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20             
    paddle_a.sety(y)    

# Function for paddle a
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20             
    paddle_b.sety(y)    

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20             
    paddle_b.sety(y)    

# Keyboard binding
gm.listen()             # Listen for keyboard input
gm.onkeypress(paddle_a_up, "w")
gm.onkeypress(paddle_a_down, "s")
gm.onkeypress(paddle_b_up, "Up")
gm.onkeypress(paddle_b_down, "Down")

while True:
    gm.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    ''' Height of the screen is 600px which means 300 up and 300 down.
    But the ball itself is 20px high and 20px wide. So the border will be > 300-20. But in order to pass the paddle we have to consider 290px as it is off the screen.
    '''
    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        # It will reverse the direction
        ball.dy *= -1
        winsound.PlaySound("mixkit-ball-bouncing-in-the-ground-2077.wav", winsound.SND_FILENAME and winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("mixkit-ball-bouncing-in-the-ground-2077.wav", winsound.SND_FILENAME and winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        # score updating
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 20, 'normal'))
        winsound.PlaySound("mixkit-ball-bouncing-in-the-ground-2077.wav", winsound.SND_FILENAME and winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        # score updating
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 20, 'normal'))
        winsound.PlaySound("mixkit-ball-bouncing-in-the-ground-2077.wav", winsound.SND_FILENAME and winsound.SND_ASYNC)

    # Ball and paddle collision
    ''' The paddle is of 5x2 = 10 px . Screen is 350 up and 350 down'''
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("mixkit-ball-bouncing-in-the-ground-2077.wav", winsound.SND_FILENAME and winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("mixkit-ball-bouncing-in-the-ground-2077.wav", winsound.SND_FILENAME and winsound.SND_ASYNC)

