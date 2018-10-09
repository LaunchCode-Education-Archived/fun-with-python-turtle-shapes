import turtle
import random

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
    def __init__(self, turtle, size_type, color, level_of_screen, side_of_screen):
        self.size_type = size_type
        self.color = color
        
        self.side_of_screen = side_of_screen
        self.turtle = turtle
        # determine size
        if size_type.lower() == "random":
            self.size = random.randrange(5, 25)
        elif size_type.lower() == "small":
            self.size = 7
        elif size_type.lower() == "medium":
            self.size = 12
        else:
            self.size = 20

        # determine y location (high, medium, low)
        if level_of_screen.lower() == "high":
            self.ycoord = random.randrange(225, 340)
        elif level_of_screen.lower() == "medium":
            self.ycoord = random.randrange(125, 225)
        else:
            self.ycoord = random.randrange(10, 125)

        # determine x location (left, middle, right)
        if side_of_screen.lower() == "left":
            self.xcoord = random.randrange(-500, -250)
        elif side_of_screen.lower() == "rigth":
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
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700
    DRAW_SPEED = 100
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 102, 0) 
    BLACK = (0, 0, 0)

    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.colormode(255)
    screen.bgcolor(BLACK)

    artist = turtle.Turtle()
    artist.speed(DRAW_SPEED)

    ground = Ground(artist, DARK_GREEN, SCREEN_WIDTH, SCREEN_HEIGHT, 225)
    ground.draw()

    #TODO: let user decide: left, right middle, high, low, big, small, going up, going down
    #rocket = Rocket(artist, "white")
    #rocket.draw()

    star = Star(artist, "large", "white", "low", "left")
    star.draw()
    star2 = Star(artist, "small", "white", "high", "right")
    star2.draw()
    star3 = Star(artist, "medium", "random", "medium", "middle")
    star3.draw()
    star4 = Star(artist, "random", "random", "medium", "middle")
    star4.draw()

    #screen.exitonclick()
    input()

if __name__ == "__main__":
    # execute only if run as a script
    main()
