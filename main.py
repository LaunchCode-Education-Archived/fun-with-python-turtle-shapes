import turtle
import random

#region global variables
DRAW_SPEED = 100
DARK_GREEN = (0, 102, 0) 
#endregion

#region classes
class Ground:
    def __init__(self, turtle, color, screen_width, screen_height, height):
        self.turtle = turtle
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = height

    def draw(self):
        self.turtle.penup()
        print("creating ground at ", -1 * (self.screen_width/2), -1 * (self.screen_height/2), "hieght of", self.height)
        self.turtle.setposition(-1 * (self.screen_width/2), -1 * (self.screen_height/2))
        self.turtle.pendown()
        self.turtle.fillcolor(self.color)
        self.turtle.begin_fill()
        self.turtle.forward(self.screen_width)
        self.turtle.setheading(90)
        self.turtle.forward(self.height)
        self.turtle.setheading(180)
        self.turtle.forward(self.screen_width)
        self.turtle.setheading(270)
        self.turtle.forward(self.height)
        self.turtle.end_fill()
        self.turtle.penup()

class Star:
    def __init__(self, turtle, size, color, height, side):
        self.turtle = turtle
        # determine size
        if size.lower() == "random":
            self.size = random.randrange(5, 25)
        elif size.lower() == "small":
            self.size = 7
        elif size.lower() == "medium":
            self.size = 12
        else:
            self.size = 20

        # determine y location (high, medium, low)
        if height.lower() == "high":
            self.ycoord = random.randrange(225, 340)
        elif height.lower() == "medium":
            self.ycoord = random.randrange(125, 225)
        else:
            self.ycoord = random.randrange(10, 125)

        # determine x location (left, middle, right)
        if side.lower() == "left":
            self.xcoord = random.randrange(-500, -250)
        elif side.lower() == "rigth":
            self.xcoord = random.randrange(250, 500)
        else:
            self.xcoord = random.randrange(-250, 250)

        # determine color
        if color.lower() == "random":
            self.color = (random.randrange(256), random.randrange(256), random.randrange(256))
        else:
            self.color = color

    def draw(self):
        #pick up the pen and place it
        self.turtle.penup()
        self.turtle.setposition(self.xcoord, self.ycoord)
        self.turtle.pendown()

        #start the drawing
        angle = 120
        self.turtle.fillcolor(self.color)
        self.turtle.begin_fill()

        for side in range(5):
            self.turtle.forward(self.size)
            self.turtle.right(angle)
            self.turtle.forward(self.size)
            self.turtle.right(72 - angle)

        self.turtle.end_fill()

class RelativeRocket:
    def __init__(self, turtle, color, size, xcoord, ycoord):
        self.turtle = turtle
        self.color = color
        self.xcoord = xcoord
        self.ycoord = ycoord
        if size.lower() == "large":
            self.modifier = 1
        else:
            self.modifier = .5
        print("drawing rocket size", size, "modifier", self.modifier)

    # draw_init draw the initial outline
    def draw(self):
        self.draw_side(self.turtle, "left")
        self.draw_side(self.turtle, "right")

    def draw_side(self, turtle, side):
        curve_angle = -0.8 if side == "left" else 0.8
        turn_angle = -15 if side == "left" else 15
        heading = 225 if side == "left" else 322
        self.turtle.penup()
        self.turtle.setposition(self.xcoord, self.ycoord)
        self.turtle.setheading(heading)
        self.turtle.pencolor(self.color)
        self.turtle.pendown()
        self.draw_curve(self.turtle, angle=curve_angle, dist=2.3)
        self.turtle.right(turn_angle)
        self.turtle.forward(200)

    def draw_curve(self, turtle, angle, dist):
        for i in range(62):
            turtle.forward(dist)
            turtle.right(angle)    

class Rocket:
    PXCORD = 58.4743409445
    NXCORD = -58.4743409445
    YCORD = -33.7390488074
    PANGLE = 17
    NANGLE = -17
    PCURVE = 0.8
    NCURVE = -0.8
    DIST = 2.3
    INIT_LENGTH = 200
    CIRCLE_CORDS = (10.66, -30)
    RADIUS = 19
    
    def __init__(self, turtle, color, size, xcoord, ycoord):
        self.turtle = turtle
        self.color = color
        self.xcoord = xcoord
        self.ycoord = ycoord
        if size.lower() == "large":
            self.modifier = 1
        else:
            self.modifier = .5
        print("drawing rocket size", size, "modifier", self.modifier)

    # draw_init draw the initial outline
    def draw(self):
        self.turtle.pencolor(self.color)
        self.turtle.width(12 * self.modifier)
        self.turtle.penup()
        self.turtle.setposition(self.xcoord, self.ycoord)
        self.turtle.setheading(90)
        self.turtle.pendown()
        self.turtle.begin_fill()

        # begin drawing
        self.turtle.right(self.PANGLE)
        self.turtle.forward(self.INIT_LENGTH * self.modifier)

        #draw the right fin
        self.turtle.setheading(0)
        self.turtle.right(55)
        self.turtle.forward(45 * self.modifier)
        self.turtle.right(55)
        self.turtle.forward(80 * self.modifier)
        self.turtle.right(130)
        self.turtle.forward(40 * self.modifier)

        self.turtle.penup()
        self.turtle.setposition(self.PXCORD, self.YCORD)
        self.turtle.setheading(90)
        self.turtle.pendown()
        self.draw_curve(self.turtle, self.NCURVE, self.DIST * self.modifier)

        # draw the other half of the flame
        self.turtle.penup()
        self.turtle.setposition(0, -225)
        self.turtle.setheading(90)
        self.turtle.pendown()

        # begin drawing
        self.turtle.right(self.NANGLE)
        self.turtle.forward(self.INIT_LENGTH * self.modifier)

        #draw the left fin
        self.turtle.setheading(180)
        self.turtle.left(55)
        self.turtle.forward(45 * self.modifier)
        self.turtle.left(55)
        self.turtle.forward(80 * self.modifier)
        self.turtle.left(130)
        self.turtle.forward(40 * self.modifier)

        # draw the left curve
        self.turtle.penup()
        self.turtle.setposition(self.NXCORD, self.YCORD)
        self.turtle.setheading(90)
        self.turtle.pendown()

        self.draw_curve(self.turtle, self.PCURVE, self.DIST * self.modifier)
        self.turtle.end_fill()
        self.draw_porthole()
        self.draw_flame()

    def draw_porthole(self):
        #make the fill and change the starting position of the turtle
        self.turtle.penup()
        self.turtle.setposition(self.CIRCLE_CORDS)
        self.turtle.pendown()

        #draw the circle
        self.turtle.circle(self.RADIUS)
        self.turtle.end_fill()

    def draw_curve(self, turtle, angle, dist):
        for i in range(62):
            turtle.forward(dist)
            turtle.right(angle)

    def draw_flame(self):

        # specify color and width
        self.turtle.pencolor(self.color)
        self.turtle.width(12)

        # set the position
        self.turtle.penup()
        self.turtle.setposition(-35, -115)

        # 0 = east
        self.turtle.setheading(0)
        self.turtle.pendown()

        # begin the fill and set the fill color
        self.turtle.begin_fill()
        self.turtle.fillcolor(self.color)

        self.turtle.forward(65)

        self.turtle.width(1)
        self.turtle.setheading(270)
        self.turtle.penup()
        self.turtle.setposition(15, -115)
        self.turtle.pendown()

        # start drawing half of the flame
        self.turtle.right(17.5)
        self.turtle.forward(50)

        self.turtle.penup()
        self.turtle.setposition(-15, -115)
        self.turtle.setheading(270)
        self.turtle.pendown()
        self.turtle.end_fill()

        # start drawing half of the flame
        self.turtle.right(-17.5)
        self.turtle.forward(50)
        self.turtle.penup()

        self.turtle.hideturtle()
#endregion

#region functions
def setup_screen(color, screen_width, screen_height):
    screen = turtle.Screen()
    screen.setup(screen_width, screen_height)
    screen.colormode(255)
    screen.bgcolor(color)
#endregion

def main():
    setup_screen(color="black", screen_width=1000, screen_height=700)

    artist = turtle.Turtle()
    artist.speed(DRAW_SPEED)

    ground = Ground(turtle=artist, color=DARK_GREEN, screen_width=1000, screen_height=700, height=225)
    ground.draw()

    rocket2 = RelativeRocket(artist, "white", size="large", xcoord=200, ycoord=200)
    rocket2.draw()

    #TODO: let user decide: left, right middle, high, low, big, small, going up, going down
    rocket = Rocket(artist, "white", size="large", xcoord=0, ycoord=-225)
    rocket.draw()



    star = Star(turtle=artist, size="large", color="white", height="low", side="left")
    star.draw()
    star2 = Star(turtle=artist, size="small", color="white", height="high", side="right")
    star2.draw()
    star3 = Star(turtle=artist, size="medium", color="random", height="medium", side="middle")
    star3.draw()
    star4 = Star(turtle=artist, size="random", color="random", height="medium", side="middle")
    star4.draw()

    #TODO: draw random number of stars in random places and colors, use a loop

    #screen.exitonclick()
    input()

if __name__ == "__main__":
    # execute only if run as a script
    main()
