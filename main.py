import rocket
import star
import turtle
import random

#TODO: let user pick bg color
BGCOLOR = (72, 61, 139)

wn = turtle.Screen()
wn.setup(575, 800)
wn.colormode(255)
wn.bgcolor(BGCOLOR)

artist = turtle.Turtle()
artist.speed(10)

#TODO: let user decide where rocket goes, left, right middle, high, low
rocket.draw(artist)

side_of_screen = input("What direction should the star go?")
#TODO: simply star draw function
star.draw(artist, random.randrange(8, 20), (random.randrange(256), random.randrange(256), random.randrange(256)), 200, side_of_screen)

raw_input()
