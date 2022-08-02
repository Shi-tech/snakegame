
import turtle
import time
import random

d = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake h
h = turtle.Turtle()
h.speed(0)
h.shape("square")
h.color("black")
h.penup()
h.goto(0,0)
h.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

s = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if h.direction != "down":
        h.direction = "up"

def go_down():
    if h.direction != "up":
        h.direction = "down"

def go_left():
    if h.direction != "right":
        h.direction = "left"

def go_right():
    if h.direction != "left":
        h.direction = "right"

def move():
    if h.direction == "up":
        y = h.ycor()
        h.sety(y + 20)

   if h.direction == "down":
        y = h.ycor()
        h.sety(y - 20)

    if h.direction == "left":
        x = h.xcor()
        h.setx(x - 20)

    if h.direction == "right":
        x = h.xcor()
        h.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if h.xcor()>290 or h.xcor()<-290 or h.ycor()>290 or h.ycor()<-290:
        time.sleep(1)
        h.goto(0,0)
        h.direction = "stop"

        # Hide the s
        for se in s:
            se.goto(1000, 1000)
        
        # Clear the s list
        s.clear()

        # Reset the score
        score = 0

        # Reset the d
        d = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if h.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a se
        new_se = turtle.Turtle()
        new_se.speed(0)
        new_se.shape("square")
        new_se.color("grey")
        new_se.penup()
        s.append(new_se)

        # Shorten the d
        d -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end s first in reverse order
    for index in range(len(s)-1, 0, -1):
        x = s[index-1].xcor()
        y = s[index-1].ycor()
        s[index].goto(x, y)

    # Move se 0 to where the h is
    if len(s) > 0:
        x = h.xcor()
        y = h.ycor()
        s[0].goto(x,y)

    move()    

    # Check for h collision with the body s
    for se in s:
        if se.distance(h) < 20:
            time.sleep(1)
            h.goto(0,0)
            h.direction = "stop"
        
            # Hide the s
            for se in s:
                se.goto(1000, 1000)
        
            # Clear the s list
            s.clear()

            # Reset the score
            score = 0

            # Reset the d
            d = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(d)

wn.mainloop()
