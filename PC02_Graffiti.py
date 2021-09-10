#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "/Users/mckennahamling/Desktop/pc02-graffiti-section12-mckennahamling-master/Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.penup()
turtle.pendown()
turtle.forward(375)
turtle.pensize(13)
turtle.forward(-375)
turtle.penup()
turtle.right(225)
turtle.right(90)
turtle.forward(50)
turtle.pendown()
turtle.backward(50)
turtle.right(90)
turtle.forward(50)
turtle.penup()
turtle.goto(33,190)
turtle.pensize(1)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.penup()
turtle.goto(95,190)
turtle.pendown()
turtle.color("pink")
turtle.circle(17)
turtle.penup()
turtle.goto(160,190)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
turtle.circle(19)
turtle.end_fill()
turtle.penup()
turtle.goto(230,210)
turtle.pendown()
turtle.pencolor("purple")
turtle.pensize(7)
turtle.goto(330,210)
turtle.goto(330,145)
turtle.goto(230,145)
turtle.goto(230,210)


