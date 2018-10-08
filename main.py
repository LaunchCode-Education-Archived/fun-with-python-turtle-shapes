import turtle
import random

#region classes
class Star:
    def __init__(self, turtle, size, color, ycoord, side_of_screen):
        self.size = size
        self.color = color
        self.ycoord = ycoord
        self.side_of_screen = side_of_screen
        self.turtle = turtle
    
    def draw(self):
        xcoord = 200
        if self.side_of_screen == "left":
            xcoord = -200

        #pick up the pen and place it
        self.turtle.penup()
        self.turtle.setposition(xcoord, self.ycoord)
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

class Rocket:
    #final variables
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
    
    def __init__(self, turtle, color):
        self.turtle = turtle
        self.color = color
    
    #draws the porthole window
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

    # draw_init draw the initial outline
    def draw(self):

        self.turtle.pencolor(self.color)
        self.turtle.width(12)
        self.turtle.penup()
        self.turtle.setposition(0, -225)
        self.turtle.setheading(90)
        self.turtle.pendown()

        # begin drawing
        self.turtle.right(self.PANGLE)
        self.turtle.forward(self.INIT_LENGTH)

        #draw the right fin
        self.turtle.setheading(0)
        self.turtle.right(55)
        self.turtle.forward(45)
        self.turtle.right(55)
        self.turtle.forward(80)
        self.turtle.right(130)
        self.turtle.forward(40)

        self.turtle.penup()
        self.turtle.setposition(self.PXCORD, self.YCORD)
        self.turtle.setheading(90)
        self.turtle.pendown()
        self.draw_curve(self.turtle, self.NCURVE, self.DIST)

        # draw the other half of the flame
        self.turtle.penup()
        self.turtle.setposition(0, -225)
        self.turtle.setheading(90)
        self.turtle.pendown()

        # begin drawing
        self.turtle.right(self.NANGLE)
        self.turtle.forward(self.INIT_LENGTH)

        #draw the left fin
        self.turtle.setheading(180)
        self.turtle.left(55)
        self.turtle.forward(45)
        self.turtle.left(55)
        self.turtle.forward(80)
        self.turtle.left(130)
        self.turtle.forward(40)

        # draw the left curve
        self.turtle.penup()
        self.turtle.setposition(self.NXCORD, self.YCORD)
        self.turtle.setheading(90)
        self.turtle.pendown()

        self.draw_curve(self.turtle, self.PCURVE, self.DIST)
        self.draw_porthole()
        self.draw_flame()

    # draw_flame
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

def main():
    #TODO: let user pick bg color
    BGCOLOR = (72, 61, 139)

    wn = turtle.Screen()
    wn.setup(575, 800)
    wn.colormode(255)
    wn.bgcolor(BGCOLOR)

    artist = turtle.Turtle()
    artist.speed(10)

    #TODO: let user decide where rocket goes, left, right middle, high, low
    rocket = Rocket(artist, "white")
    rocket.draw()

    side_of_screen = "left" #input("What direction should the star go?")
    #TODO: simply star draw function
    star = Star(artist, random.randrange(8, 20), (random.randrange(256), random.randrange(256), random.randrange(256)), 200, side_of_screen)
    star.draw()

    input()

if __name__ == "__main__":
    # execute only if run as a script
    main()
