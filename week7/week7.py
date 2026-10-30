import turtle


# Exercise 1

# def sumTo(n):
#     total = n * (n + 1) / 2
#     return total

# print(str(sumTo(n))



# Exercise 2

# def drawStar(t, n, size):
#     angle = 180 - 180 / n
#     for i in range(n):
#         t.forward(size)
#         t.right(angle)
#
#
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
#
# drawStar(t, 11, 100)
#
# wn.exitonclick()


# Exercise 3

# def sumTo(n):
#     total = 0
#     for i in range(1,n+1):
#         total = total + i
#     return total
#
# print(sumTo(10))
#
# n = int(input("Enter a number: "))
# print(sumTo(n))


# Exercise 4


# def mySqrt(n):
#     guess = n / 2
#     for i in range(20):
#         guess = (1/2) *(guess + n/guess)
#         print(guess)
#     return guess
#
# n = int(input("Enter a positive integer: "))
# print(mySqrt(n))



# Exercise 5

# Üçgenle ilgili anlattıklarınızı dinledim, ama kodu biraz daha erken yazdığım için değiştirmek istemedim

# def fancySquare(t, size, spriteLegNumber, spriteLegLength):
#     for i in range(4):
#         t.shape('circle')
#         t.forward(size)
#         t.stamp()
#         for i in range(spriteLegNumber):
#             t.forward(spriteLegLength)
#             t.shape('arrow')
#             t.stamp()
#             t.backward(spriteLegLength)
#             t.left(360/spriteLegNumber)
#         t.left(90)
#
#

# wn = turtle.Screen()
# Axle = turtle.Turtle()
# wn.bgcolor("lightgreen")
# Axle.pensize(2)
# Axle.color("hotpink")
#
# fancySquare(Axle, 100, 5, 50)
# wn.exitonclick()
#
# wn.exitonclick()


# Exercise 6
#
# def positiveOrNegative(num):
#     if num > 0:
#         print(str(num) + " is positive")
#     elif num < 0:
#         print(str(num) + " is negative")
#     else:
#         print(str(num) + " is zero")
#
# n = float(input("Enter a number: "))
# positiveOrNegative(n)


# Exercise 7

def drawBar(t, barHight):
    t.color("red")
    t.pencolor("blue")
    t.begin_fill()
    t.left(90)
    t.forward(barHight)

    t.penup()
    t.forward(5)
    t.right(90)
    t.forward(2)
    t.write(barHight, font=("Arial", 8, "normal"))
    t.backward(2)
    t.left(90)
    t.backward(5)
    t.pendown()


    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(barHight)
    t.left(90)
    t.end_fill()





def barChart(t, ls):
    for i in ls:
        drawBar(t, i)

list = [48, 117, 200, 240, 160, 260, 220]


wn = turtle.Screen()
Lemon = turtle.Turtle()
Lemon.pensize(2)
wn.bgcolor("lightgreen")

Lemon.penup()
Lemon.goto(-100, 0)
Lemon.pendown()
barChart(Lemon, list)


wn.exitonclick()