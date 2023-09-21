import turtle
import random

# screen
FONT = ("Arial", 20, "normal")
screen = turtle.Screen()
screen.title("Catch The Turtle")
screen.bgcolor("black")
game_over = False
turtle_list = list()
countdown_turtle =turtle.Turtle()
# score setup
scoreTurtle = turtle.Turtle()
score = 0


def score_setup():
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    scoreTurtle.hideturtle()
    scoreTurtle.up()
    scoreTurtle.setpos(0, y)
    scoreTurtle.down()
    scoreTurtle.color("green")
    scoreTurtle.write("Score : 0", move=False, align="center", font=FONT)
    scoreTurtle.hideturtle()


grid_size = 10


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        scoreTurtle.clear()
        scoreTurtle.write("Score: {}".format(score), move=False, align="center", font=FONT)

    t.penup()
    t.onclick(handle_click)
    t.color("red")
    t.shape("turtle")
    t.shapesize(1.5, 1.5)
    t.setpos(x * grid_size, y * grid_size)
    turtle_list.append(t)


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtles():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles, 500)

def count_time(time):
    global game_over
    countdown_turtle.hideturtle()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.hideturtle()
    countdown_turtle.up()
    countdown_turtle.setpos(0, y-30)
    countdown_turtle.clear()

    if time >0:
        countdown_turtle.color("red")
        countdown_turtle.write("Time: {} ".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: count_time(time-1),1000)
    else:
        game_over = True
        hide_turtles()
        countdown_turtle.setpos(0, 0)
        countdown_turtle.color("RED")
        countdown_turtle.write("Game Over", move=False, align="center", font=("Arial", 50, "normal"))
        scoreTurtle.clear()
        scoreTurtle.penup()
        scoreTurtle.setpos(0, -50)
        scoreTurtle.write("Score : {}".format(score), move=False, align="center", font=FONT)
        if score < 10:
            scoreTurtle.penup()
            scoreTurtle.setpos(0, -80)
            scoreTurtle.color("purple")
            scoreTurtle.write("NOOB!!!", move=False, align="center", font=FONT)
        else:
            scoreTurtle.penup()
            scoreTurtle.setpos(0, -80)
            scoreTurtle.color("green")
            scoreTurtle.write("Well PLayed", move=False, align="center", font=FONT)

turtle.tracer(0)
score_setup()
setup_turtles()
hide_turtles()
show_turtles()
count_time(10)
turtle.tracer(1)
turtle.mainloop()
