import turtle

#Exercise 1

# def gradeToMark(grade):
#     if grade >= 90:
#         return "A"
#     elif grade > 80:
#         return "B"
#     elif grade >= 70:
#         return "C"
#     elif grade >= 60:
#         return "D"
#     else:
#         return "F"
#
#
# grade = int(input("How many points did u get from the exam?:  "))
#
# print("You got", grade, "points so your grade is", gradeToMark(grade))



#Exercise 2

# def chooseColor(barHight):
#     if barHight >= 200:
#         return "red"
#     elif barHight >= 100:
#         return "yellow"
#     else:
#         return "green"
#
#
# def drawBar(t, barHight):
#     t.color(chooseColor(barHight))
#
#     t.pencolor("blue")
#     t.begin_fill()
#     t.left(90)
#     t.forward(barHight)
#
#     t.penup()
#     t.forward(5)
#     t.right(90)
#     t.forward(2)
#     t.write(barHight, font=("Arial", 8, "normal"))
#     t.backward(2)
#     t.left(90)
#     t.backward(5)
#     t.pendown()
#
#
#     t.right(90)
#     t.forward(20)
#     t.right(90)
#     t.forward(barHight)
#     t.left(90)
#     t.end_fill()
#
#
#
# def barChart(t, ls):
#     for i in ls:
#         drawBar(t, i)
#
#
# list = [48, 117, 200, 240, 160, 260, 220]
#
#
# wn = turtle.Screen()
# Lemon = turtle.Turtle()
# Lemon.pensize(2)
# wn.bgcolor("lightgreen")
#
# Lemon.penup()
# Lemon.goto(-100, 0)
# Lemon.pendown()
# barChart(Lemon, list)
#
#
# wn.exitonclick()


#Exercise 3


# def chooseColor(barHight):
#     if barHight >= 200:
#         return "red"
#     elif barHight >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# def writeNumber(t, n):
#     t.penup()
#
#     if n >= 0:
#         t.forward(5)
#         t.right(90)
#         t.forward(2)
#         t.write(n, font=("Arial", 8, "normal"))
#         t.backward(2)
#         t.left(90)
#         t.backward(5)
#
#     else:
#         t.right(180)
#         t.forward(n)
#         t.right(90)
#         t.forward(2)
#         t.write(n, font=("Arial", 8, "normal"))
#         t.backward(2)
#         t.right(90)
#         t.forward(n)
#
#     t.pendown()
#
# def drawBar(t, barHight):
#     t.color(chooseColor(barHight))
#
#     t.pencolor("blue")
#     t.begin_fill()
#     t.left(90)
#     t.forward(barHight)
#
#     writeNumber(t, barHight)
#     t.pendown()
#
#
#     t.right(90)
#     t.forward(20)
#     t.right(90)
#     t.forward(barHight)
#     t.left(90)
#     t.end_fill()
#
#
#
# def barChart(t, ls):
#     for i in ls:
#         drawBar(t, i)
#
#
# list = [-48, 117, -200, 240, -160, 260, 220]
#
#
# wn = turtle.Screen()
# Lemon = turtle.Turtle()
# Lemon.pensize(2)
# wn.bgcolor("lightgreen")
#
# Lemon.penup()
# Lemon.goto(-100, 0)
# Lemon.pendown()
# barChart(Lemon, list)
#
#
# wn.exitonclick()



#Exercise 4

def findHypot(a, b):
    hypot = (a ** 2 + b ** 2) ** 0.5
    return hypot



shortSideA = int(input("Enter the first short side: "))
shortSideB = int(input("Enter the second short side: "))

print(findHypot(shortSideA, shortSideB))

