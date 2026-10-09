#for i in range(1,101):
#    print("We like Python's turtles!")


#Exercise 2
for i in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    print("One of the months of the year is " + i)


#Exercise 3
for i in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print(i)

for i in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print(str(i) + ", " + str(i**2))


#Exercise 4
import turtle
# Scr = turtle.Screen()
# Billy = turtle.Turtle()
# Billy.pensize(3)
# for i in range(3):
#     Billy.forward(100)
#     Billy.left(120)
#
# Bully = turtle.Turtle()
# Bully.pensize(3)
# Bully.penup()
# Bully.forward(200)
# Bully.pendown()
# for i in range(4):
#     Bully.forward(100)
#     Bully.left(90)
#
# Bobby = turtle.Turtle()
# Bobby.pensize(3)
# Bobby.penup()
# Bobby.backward(300)
# Bobby.pendown()
# for i in range(6):
#     Bobby.forward(100)
#     Bobby.left(60)
#
# Raiden = turtle.Turtle()
# Raiden.pensize(3)
# Raiden.penup()
# Raiden.right(90)
# Raiden.forward(300)
# Raiden.left(90)
# Raiden.pendown()
# for i in range(8):
#     Raiden.forward(100)
#     Raiden.left(45)

# Scr.exitonclick()


#Exercise 5
# numberOfSides = int(input("How many sides do you need?   -"))
# sideLength = int(input("What do you want the length of those sides to be?   -"))
# color = input("What do you want the color of those sides to be?   -")
# colorFill = input("What about the color filling?   -")
#
# Scr = turtle.Screen()
# Bob = turtle.Turtle()
# Bob.color(color)
# #I gotta find a way to fill the shape
# Bob.fillcolor(colorFill)
# for i in range(numberOfSides):
#     Bob.forward(sideLength)
#     Bob.left(360 / numberOfSides)
#
# Scr.exitonclick()


#Exercise 8
Scr = turtle.Screen()
Tutle = turtle.Turtle()
Tutle.color("Blue")
Tutle.pensize(3)
Tutle.penup()
Tutle.shape("turtle")
Tutle.stamp()

for i in range(12):
    Tutle.forward(100)
    Tutle.pendown()
    Tutle.forward(25)
    Tutle.penup()
    Tutle.forward(50)
    Tutle.stamp()
    Tutle.backward(175)
    Tutle.left(30)
