#ping pong

import turtle

wn=turtle.Screen()
wn.title("Pong by Vivek")
wn.bgcolor("Black")
wn.setup(width=800,height=600)
wn.tracer(0)

#left panel
paddel_left=turtle.Turtle()
paddel_left.speed(0)
paddel_left.shape("square")
paddel_left.shapesize(stretch_wid=6,stretch_len=1)
paddel_left.penup()
paddel_left.goto(-350,0)
paddel_left.color("white")

#right pannel
paddel_right=turtle.Turtle()
paddel_right.speed(0)
paddel_right.shape("square")
paddel_right.shapesize(stretch_wid=6,stretch_len=1)
paddel_right.penup()
paddel_right.goto(350,0)
paddel_right.color("white")

score_a=0
score_b=0

#score
pen=turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color("White")
pen.hideturtle()
pen.goto(0,260)
pen.write("A:0  B:0",align="Center",font=("Courier",24,"normal"))
#ball
paddel_ball=turtle.Turtle()
paddel_ball.speed(0)
paddel_ball.shape("circle")
paddel_ball.penup()
paddel_ball.goto(0,0)
paddel_ball.color("white")
paddel_ball.dx=0.2  
paddel_ball.dy=0.2

#function
def paddel_left_up():
    y=paddel_left.ycor()
    y=y+20
    paddel_left.sety(y)

def paddel_right_up():
    y=paddel_right.ycor()
    y=y+20
    paddel_right.sety(y)

def paddel_left_down():
    y=paddel_left.ycor()
    y=y-20
    paddel_left.sety(y)

def paddel_right_down():
    y=paddel_right.ycor()
    y=y-20
    paddel_right.sety(y)


#key binding
wn.listen()
wn.onkeypress(paddel_left_up,"w")
wn.onkeypress(paddel_left_down,"s")
wn.onkeypress(paddel_right_up,"i")
wn.onkeypress(paddel_right_down,"k")

#main game loop
while True:
    wn.update()

    #move the ball
    paddel_ball.setx(paddel_ball.xcor() + paddel_ball.dx)
    paddel_ball.sety(paddel_ball.ycor() + paddel_ball.dy)

    #border check
    if paddel_ball.ycor()>290:
        paddel_ball.sety(290)
        paddel_ball.dy *= -1

    if paddel_ball.ycor()<-290:
        paddel_ball.sety(-290)
        paddel_ball.dy *= -1

    if paddel_ball.xcor()>390:
        paddel_ball.goto(0,0)
        paddel_ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("A:{}  B:{}".format(score_a,score_b),align="Center",font=("Courier",24,"normal"))
    
    if paddel_ball.xcor()<-390:
        paddel_ball.goto(0,0)
        paddel_ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("A:{}  B:{}".format(score_a,score_b),align="Center",font=("Courier",24,"normal"))

    #collision
    if (paddel_ball.xcor() > 340 and paddel_ball.xcor() < 350) and (paddel_ball.ycor() < paddel_right.ycor() + 60 and paddel_ball.ycor() > paddel_right.ycor() - 60):
        paddel_ball.setx(340)
        paddel_ball.dx *= -1
    
    if (paddel_ball.xcor() < -340 and paddel_ball.xcor() > -350) and (paddel_ball.ycor() < paddel_left.ycor() + 60 and paddel_ball.ycor() > paddel_left.ycor() - 60):
        paddel_ball.setx(-340)
        paddel_ball.dx *= -1

    
