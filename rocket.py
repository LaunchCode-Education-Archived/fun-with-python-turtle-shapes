

import random

#final variables
PXCORD = 58.4743409445
NXCORD = -58.4743409445
YCORD = -33.7390488074
PANGLE = 17
NANGLE = -17
PCURVE = 0.8
NCURVE = -0.8
DIST = 2.3
COLOR = 'white'

INIT_LENGTH = 200
CIRCLE_CORDS = (10.66, -30)
RADIUS = 19

#draws the porthole window
def draw_porthole(turtle):

    #make the fill and change the starting position of the turtle
    turtle.penup()
    turtle.setposition(CIRCLE_CORDS)
    turtle.pendown()

    #draw the circle
    turtle.circle(RADIUS)
    turtle.end_fill()


# draw the curve on the top of the rocket
def draw_curve(turtle, angle, dist):

    #create a loop for the curve
    for i in range(62):

        turtle.forward(dist)
        turtle.right(angle)

# draw_init draw the initial outline
def draw(nt1):

    nt1.pencolor(COLOR)
    nt1.width(12)
    nt1.penup()
    nt1.setposition(0, -225)
    nt1.setheading(90)
    nt1.pendown()

    # begin drawing
    nt1.right(PANGLE)
    nt1.forward(INIT_LENGTH)

    #draw the right fin
    nt1.setheading(0)
    nt1.right(55)
    nt1.forward(45)
    nt1.right(55)
    nt1.forward(80)
    nt1.right(130)
    nt1.forward(40)

    nt1.penup()
    nt1.setposition(PXCORD, YCORD)
    nt1.setheading(90)
    nt1.pendown()
    draw_curve(nt1, NCURVE, DIST)

    # draw the other half of the flame
    nt1.penup()
    nt1.setposition(0, -225)
    nt1.setheading(90)
    nt1.pendown()

    # begin drawing
    nt1.right(NANGLE)
    nt1.forward(INIT_LENGTH)

    #draw the left fin
    nt1.setheading(180)
    nt1.left(55)
    nt1.forward(45)
    nt1.left(55)
    nt1.forward(80)
    nt1.left(130)
    nt1.forward(40)

    # draw the left curve
    nt1.penup()
    nt1.setposition(NXCORD, YCORD)
    nt1.setheading(90)
    nt1.pendown()

    #draw the curves
    draw_curve(nt1, PCURVE, DIST)

    #draw the circle
    draw_porthole(nt1)

    draw_flame(nt1)

    nt1.hideturtle()

# draw_flame
def draw_flame(flame):

    # specify color and width
    flame.pencolor(COLOR)
    flame.width(12)

    # set the position
    flame.penup()
    flame.setposition(-35, -115)

    # 0 = east
    flame.setheading(0)
    flame.pendown()

    # begin the fill and set the fill color
    flame.begin_fill()
    flame.fillcolor(COLOR)

    flame.forward(65)

    flame.width(1)
    flame.setheading(270)
    flame.penup()
    flame.setposition(15, -115)
    flame.pendown()

    # start drawing half of the flame
    flame.right(17.5)
    flame.forward(50)

    flame.penup()
    flame.setposition(-15, -115)
    flame.setheading(270)
    flame.pendown()
    flame.end_fill()

    # start drawing half of the flame
    flame.right(-17.5)
    flame.forward(50)
    flame.penup()

    flame.hideturtle()
