import turtle
import random
import math

#region global variables
DRAW_SPEED = 100
DARK_GREEN = (0, 102, 0)
DEFAULT_PEN_SIZE = 1
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
        self.turtle.pensize(DEFAULT_PEN_SIZE)
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
        self.turtle.pensize(DEFAULT_PEN_SIZE)
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

    def __init__(self, turtle, border_color, inner_color):
        self.turtle = turtle
        self.border_color = border_color
        self.inner_color = inner_color

    #draws the porthole window
    def draw_porthole(self):

        #make the fill and change the starting position of the turtle
        self.turtle.penup()
        self.turtle.setposition(self.CIRCLE_CORDS)
        self.turtle.pendown()
        self.turtle.fillcolor(53, 74, 95)
        self.turtle.begin_fill()

        #draw the circle
        self.turtle.circle(self.RADIUS)
        self.turtle.end_fill()

    def draw_curve(self, turtle, angle, dist):
        for i in range(63):
            turtle.forward(dist)
            turtle.right(angle)

    # draw_init draw the initial outline
    def draw(self):

        self.turtle.pencolor(self.border_color)
        self.turtle.pensize(12)
        self.turtle.penup()
        self.turtle.setposition(0, -225)
        self.turtle.setheading(90)
        self.turtle.pendown()
        self.turtle.fillcolor(self.inner_color)
        self.turtle.begin_fill()

        # begin drawing
        self.turtle.right(self.PANGLE)
        self.turtle.forward(self.INIT_LENGTH)

        # draw the right fin
        self.turtle.setheading(0)
        self.turtle.right(55)
        self.turtle.forward(45)
        self.turtle.right(55)
        self.turtle.forward(80)
        self.turtle.right(130)
        self.turtle.forward(40)

        self.turtle.penup()
        # self.turtle.end_fill()
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
        self.turtle.end_fill()
        self.draw_porthole()

        self.draw_flame()


    def draw_flame(self):

        # specify color and width
        self.turtle.pencolor(self.border_color)
        self.turtle.pensize(12)

        # set the position
        self.turtle.penup()
        self.turtle.setposition(-35, -115)

        # 0 = east
        self.turtle.setheading(0)
        self.turtle.pendown()

        # begin the fill and set the fill color
        self.turtle.begin_fill()
        self.turtle.fillcolor(self.inner_color)

        self.turtle.forward(65)

        self.turtle.pensize(12)
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

class Planet:
    # CIRCLE_CORDS = (100, 100)
    # RADIUS = 30

    def __init__(self, turtle, color, radius, coordinates):
        self.turtle = turtle
        self.color = color
        self.radius = radius
        self.coordinates = coordinates

    def draw(self):

        #make the fill and change the starting position of the turtle
        self.turtle.pensize(DEFAULT_PEN_SIZE)
        self.turtle.penup()
        self.turtle.setposition(self.coordinates)
        self.turtle.pendown()

        self.turtle.fillcolor(self.color)
        self.turtle.begin_fill()

        #draw the circle
        self.turtle.circle(self.radius)
        self.turtle.end_fill()


#endregion


#region functions
def setup_screen(color, screen_width, screen_height):
    screen = turtle.Screen()
    screen.setup(screen_width, screen_height)
    screen.colormode(255)
    screen.bgcolor(color)

def random_color():
    random_rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    #print(random_rgb)
    return random_rgb

def move(t, position, speed=10):
    #t.speed(speed)
    t.penup()
    t.setpos(position)
    t.pendown()

def draw_rectangle(t, length, height, position):
    move(t, position)
    for i in range(4):
        if i % 2 == 0:
            t.forward(height)
            t.right(90)
        else:
            t.forward(length)
            t.right(90)

def draw_square(t, length, position):
    draw_rectangle(t, length, length, position)

def draw_triangle(t, length_a, length_b, length_c, position, color=None):
    '''
    angle_a = arccos(((b^2) + (c^2) - (a^2))) / (2 * b * c))
    '''
    length_a = float(length_a)
    length_b = float(length_b)
    length_c = float(length_c)
    if color != None:
        t.fillcolor(color)
    else:
        t.fillcolor('white')

    print("A: {} B: {} C: {}".format(length_a, length_b, length_c))
    num = float((length_b * length_b) + (length_c * length_c) - (length_a ** 2))
    denom = float(2 * length_b * length_c)
    print("Numerator: {} Denomerator: {}".format(num, denom))
    angle_a = math.degrees(math.acos(num / denom))
    print("Angle A: {}".format(angle_a))
    num = (length_c * length_c) + (length_a * length_a) - (length_b ** 2)
    denom = 2 * length_c * length_a
    angle_b = math.degrees(math.acos(num / denom))
    print("Angle B: {}".format(angle_b))
    angle_c = 180 - angle_a - angle_b
    print("Angle C: {}".format(angle_c))
    move(t, position)
    t.begin_fill()
    t.forward(length_a)
    t.right(angle_a + angle_b)
    t.forward(length_b)
    t.right(angle_b + angle_c)
    t.forward(length_c)
    t.end_fill()
    #t.right

def crazy_triangles(t, num_of_triangles, speed='Random', pensize='Random', pencolor='Random'):
    if speed != 'Random':
        t.speed(speed)
    if pensize != 'Random':
        t.pensize(pensize)
    if pencolor != 'Random':
        t.pencolor(pencolor)
    for i in range(num_of_triangles):
        print("{}/{} triangles drawn".format(i+1, num_of_triangles))
        if pensize == 'Random':
            t.pensize(random.randint(0,10))
        if pencolor == 'Random':
            t.pencolor(random_color())
        num_a = float(random.randint(50, 100))
        num_b = float(random.randint(50, 100))
        num_c = float(random.randint(50, 100))
        #max_x, max_y = turtle.screensize()
        max_x = 300
        max_y = 300
        rand_pos = (random.randint((max_x * -1), max_x), random.randint((max_y * -1), max_y))
        if speed=='Random':
            t.speed(random.randint(0, 10))
        draw_triangle(t, num_a, num_b, num_c, rand_pos, random_color())

#endregion

def main():
    setup_screen(color="black", screen_width=1000, screen_height=700)

    artist = turtle.Turtle()
    artist.speed(DRAW_SPEED)

    ground = Ground(turtle=artist, color=DARK_GREEN, screen_width=1000, screen_height=700, height=225)
    ground.draw()

    crazy_triangles(artist, 4)

    #TODO: let user decide: left, right middle, high, low, big, small, going up, going down
    rocket = Rocket(artist, border_color="white", inner_color=random_color())
    rocket.draw()

    #stars
    star = Star(turtle=artist, size="large", color="white", height="low", side="left")
    star.draw()
    star2 = Star(turtle=artist, size="small", color="white", height="high", side="right")
    star2.draw()
    star3 = Star(turtle=artist, size="medium", color="random", height="medium", side="middle")
    star3.draw()
    star4 = Star(turtle=artist, size="random", color="random", height="medium", side="middle")
    star4.draw()

    #planets
    mercury = Planet(turtle=artist, color="light gray", radius=5, coordinates=(150, 250))
    mercury.draw()
    
    venus = Planet(turtle=artist, color="tan", radius=7, coordinates=(150, 200))
    venus.draw()
    
    earth = Planet(turtle=artist, color="green", radius=15, coordinates=(150,125))
    earth.draw()
    
    mars = Planet(turtle=artist, color="red", radius=10, coordinates=(150, 55))
    mars.draw()
    
    jupiter = Planet(turtle=artist, color="dark orange", radius=30, coordinates=(150, -30))
    jupiter.draw()
    
    saturn = Planet(turtle=artist, color="lemon chiffon", radius=25, coordinates=(150, -100))
    saturn.draw()
    
    uranus = Planet(turtle=artist, color="light blue", radius=10, coordinates=(150, -175))
    uranus.draw()
    
    neptune = Planet(turtle=artist, color="blue", radius=7, coordinates=(150, -250))
    neptune.draw()
    
    pluto = Planet(turtle=artist, color="rosy brown", radius=3, coordinates=(150, -300))
    pluto.draw()

    input()

if __name__ == "__main__":
    # execute only if run as a script
    main()
