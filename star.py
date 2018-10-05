#draw_star method
def draw(turtle, size, color, ycoord, side_of_screen):

    xcoord = 200
    if side_of_screen == "left":
        xcoord = -200

    #pick up the pen and place it
    turtle.penup()
    turtle.setposition(xcoord, ycoord)
    turtle.pendown()

    #start the drawing
    angle = 120
    turtle.fillcolor(color)
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)

    turtle.end_fill()
