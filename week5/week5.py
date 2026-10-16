import random
import math
import turtle

#exercise 1
# for i in range(10):
#     print(random.random())

#exercise 2
# for i in range(10):
#     print(random.randint(25, 35))


# #exercise 3
# a = int(input("enter the side a of your triangle"))
# b = int(input("enter the side b of your triangle"))
# c= math.sqrt(a**2 + b**2)
#
# print(c)


#exercise 3.1
# a = int(input("enter the side a of your triangle"))
# b = int(input("enter the side b of your triangle"))
# c = math.hypot(a,b)
#
# print(c)


#exercise 4
# def areaOfCircle(r):
#     area = math.pi * r**2
#     return area
#
# print(areaOfCircle(5))


#exercise 5

# def drawStar(t, side):
#     t.left(36)
#     for i in range(5):
#         t.forward(side)
#         t.left(144)
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# drawStar(tess, 100)
#
# screen.exitonclick()

#exercise 6

# def drawsquare(t, length):
#     for i in range(5):
#         for i in range(4):
#             t.forward(length)
#             t.left(90)
#         t.penup()
#         t.forward(length*2)
#         t.pendown()
#
# totle = turtle.Turtle()
# scr = turtle.Screen()
# scr.bgcolor("lightgreen")
# totle.color("pink")
# totle.pensize(3)
#
# drawsquare(totle, 20)
#
# scr.exitonclick()


#exercise 7 my try

def drawWeirdNonSpiralShape(t, firstSide):
    for l in range(1,6):
        for i in range(4):
            t.fd(firstSide*l)
            t.lt(90)
        t.penup()
        t.right(90)
        t.fd(10)
        t.right(90)
        t.fd(10)
        t.right(180)
        t.pendown()

tuotle = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor("lightgreen")
tuotle.pensize(3)
tuotle.color("pink")

drawWeirdNonSpiralShape(tuotle, 20)

scr.exitonclick()