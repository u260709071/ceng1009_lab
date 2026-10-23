import turtle

wn = turtle.Screen()
wn.bgcolor('Lightgreen')

tess = turtle.Turtle()

# -- functions --

def drawPoly(someturtle, somesides, somesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(angle)

def drawSpiral(someturtle, angle):
    size = 1
    for i in range(100):
        someturtle.forward(size)
        someturtle.left(angle)
        size = size + 1

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)

def drawSprite(someturtle, legnumber, leglength):
    someturtle.shape('circle')
    someturtle.stamp()
    for i in range(legnumber):
        someturtle.forward(leglength)
        someturtle.backward(leglength)
        someturtle.left(360 / legnumber)

def drawStar(someturtle, somesize):
    for i in range(5):
        someturtle.forward(somesize)
        someturtle.right(144)





# -- exercises --

# Exercise 1
# tess.color('hotpink')
# drawPoly(tess, 8, 50)

# Exercise 2
# tess.color('blue')
# for i in range(20):
#     drawPoly(tess, 4, 100)
#     tess.left(18)
#

# Exercise 3
# tess.pencolor('blue')
# tess.penup()
# tess.goto(-150, 0)
# tess.pendown()
# drawSpiral(tess, 90)
#
# tess.penup()
# tess.goto(150, 0)
# tess.pendown()
# drawSpiral(tess, 89)
#


# Exercise 4

# drawEquitriangle(tess, 100)
#


# Exercise 5

# tess.color("hotpink")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# for i in range(5):
#     drawStar(tess, 100)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()

# Exercise 6

drawSprite(tess, 15, 120)



# -- finish --
wn.exitonclick()



