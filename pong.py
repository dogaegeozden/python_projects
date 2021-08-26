#!/usr/bin/python3
# Copyright © 2021 All rights reserved. Doga Ege Ozden
# Simple pong in python 3 for beginners
# Part 1: Getting Started

import turtle # It's a graphical interface tool can be use for game production good for beginners.

# MUSIC # You having issues while playing the song.
# on linux import os # It's for interracting with operating system. You can use it for playing sound.
# os.system("aplay 'Same Time - Spence.mp3&'") # This is when you want to play a sound. You didn't want it. The "&" at the end of the file is preventing screen freeze that happens because of playing that file.
# on windows import winsound
# winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


# WINDOW
# wn(window) is object build for creating the game window.
# you choose the wn name you could say window as well.
wn = turtle.Screen()

# wn(window) attributes
wn.title("Pong") # Puts a title to window.
wn.bgcolor("black") # Identifies a background color.
wn.setup(width=800, height=600) # This defines the measurements of the window.
wn.tracer(0)


# SCORE
score_a = 0
score_b = 0


# PADDLE A
paddle_a = turtle.Turtle() # This is the paddle that hit's the ball. It creates the default shape.

# paddle a attributes
paddle_a.speed(0) # This is the speed of animation you need this because of turtle graphics.
paddle_a.shape("square") # This identified the paddle's shape.
paddle_a.color("white") # This identifies the paddle's color.
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # By default the shape is 20px width and 20 height. You can use shapesize method to stretch the shape to the sizes you want. 5 will make he height 5*20 and 1 will make the width 1*20.


paddle_a.penup() # Turtle's by defination draw lines and you don't want that so you should do penup.
paddle_a.goto(-350, 0) # This defines the paddle a's location so x = -350 and y = 0.

#PADDLE B
paddle_b = turtle.Turtle() # This is the paddle that hit's the ball. It cretes the default shape.

# paddle a attributes
paddle_b.speed(0) # This is the speed of animation you need this because of turtle graphics.
paddle_b.shape("square") # This identified the paddle's shape.
paddle_b.color("white") # This identifies the paddle's color.
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # By default the shape is 20px width and 20 height. You can use shapesize method to stretch the shape to the sizes you want. 5 will make he height 5*20 and 1 will make the width 1*20.


paddle_b.penup() # Turtle's by defination draw lines and you don't want that so you should do penup.
paddle_b.goto(350, 0) # This defines the paddle a's location so x = 350 and y = 0.


# BALL
ball = turtle.Turtle() # This creates the default shape 20 x 20

# Ball attributes
ball.speed(0) # This defines the anmation speed to really really fast.
ball.shape("circle") # This defines the shape of the ball/object
ball.color("white") # This defines the color of the object.
ball.penup() # This prevents turtle to draw lines.
ball.goto(0,0) # This defines the position of the shape using cordinate system.
ball.dx = 0.2 # "d" for delta change. This changes sets the balls movement 0.2 pixel on x cordinate. This is your movement speed.
ball.dy = -0.2 # This means everytime ball moves it moves -0.2 pixels on y cordinate. This is your movement speed.


# WRITING WITH PEN
pen = turtle.Turtle() # small t turtle for the module name T Turtle is for the class name.
pen.speed(0) # This is the animation speed not the movement speed.
pen.color("white") # This makes the color white.
pen.penup() # This is preventing turtle from drawing line.
pen.hideturtle() # This hides the turtle.
pen.goto(0,260) # This is location that the text will be exist on window.
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# FUNCTIONS
# You can use functions to make user able to move paddle up and down.

# Move up function for paddle a.
def paddle_a_up():
    y = paddle_a.ycor() # ycor is a turtle method it returns the y cordinate.
    y += 20 # This will add 20 pixels to y cordinate
    paddle_a.sety(y)

# Move down function for paddle a.
def paddle_a_down():
    y = paddle_a.ycor() # ycor is a turtle method it returns the y cordinate.
    y -= 20 # This will add 20 pixels to y cordinate
    paddle_a.sety(y)

# Move up function for paddle b.
def paddle_b_up():
    y = paddle_b.ycor() # ycor is a turtle method it returns the y cordinate.
    y += 20 # This will add 20 pixels to y cordinate
    paddle_b.sety(y)

# Move down function for paddle b.
def paddle_b_down():
    y = paddle_b.ycor() # ycor is a turtle method it returns the y cordinate.
    y -= 20 # This will add 20 pixels to y cordinate
    paddle_b.sety(y)

# Keyboard bindings
wn.listen() # listen method is for listening keyboard input.
wn.onkeypress(paddle_a_up, "w") # when the user presses "w" this will call the function paddle_a_up.
wn.onkeypress(paddle_a_down, "s") # when the user presses "s" this will call the function paddle_a_down.
wn.onkeypress(paddle_b_up, "Up") # when the user presses up arrowkey this will call the function paddle_b_up.
wn.onkeypress(paddle_b_down, "Down") # when the user presses down arrowkey this will call the function paddle_b_down.


# MAIN GAME LOOP
# Every game needs a main game loop.
while True:
    wn.update() # This updates the screen every time loop runs.

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290: # This says if the balls y cordinate passes 290 do the fallowing actions/commands. width = 600px ball = 20px
        ball.sety(290) # This takes the ball to center (0,0).
        ball.dy *= -1 # This reverses the ball's direction.

    elif ball.ycor() < -290: # This says if the balls y cordinate passes -290 do the fallowing actions/commands. width = 600px ball = 20px
        ball.sety(-290) # This takes the ball to center (0,0).
        ball.dy *= -1 # This reverses the ball's direction.

    if ball.xcor() > 390: # This says if the balls x cordinate passes 390 do the fallowing actions/commands. height = 800px ball = 20px
        ball.goto(0, 0) # This takes the ball to center (0,0).
        ball.dx *= -1 # This reverses the ball's direction.
        score_a += 1 # This adds one to score
        pen.clear() # This clears what is on the screen written with pen.
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) # This code keeps the score and writes it using pen on window.

    if ball.xcor() < -390: # This says if the balls x cordinate passes -390 do the fallowing actions/commands. height = 800px ball = 20px
        ball.goto(0, 0) # This takes the ball to center (0,0).
        ball.dx *= -1 # This reverses the ball's direction.
        score_b += 1 # This code addes 1 to score.
        pen.clear() # This clears what is on the screen written with pen.
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) # This code keeps the score and writes it using pen on window.


    # PADDLE AND BALL COLLISIONS
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        # Condititon 1: when the ball x cordinate passes 340 and smaller than 350 right before completely getting our from the screen. To the fallowing actions.
        # Condition 2: when the ball touches to paddle by default shape is 20x20 and you stretched it to 100x20 20+40+40=100 when the ball's y cordinate smaller then paddle_b.ycor+40 when the ball's y cordinate is bigger than paddle_b.ycor -40. Do the fallowing actions.
        ball.setx(340) #
        ball.dx *= -1 # So when it touches to paddle it reverses the direction.

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        # Condititon 1: when the ball x cordinate passes 340 and smaller than 350 right before completely getting our from the screen. To the fallowing actions.
        # Condition 2: when the ball touches to paddle by default shape is 20x20 and you stretched it to 100x20 20+40+40=100 when the ball's y cordinate smaller then paddle_b.ycor+40 when the ball's y cordinate is bigger than paddle_b.ycor -40. Do the fallowing actions.
        ball.setx(-340) #
        ball.dx *= -1 # So when it touches to paddle it reverses the direction.
