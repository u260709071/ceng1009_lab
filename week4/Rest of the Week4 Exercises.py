#These were all done at home and not in the lab class

import turtle

#Exercise 6
# scr = turtle.Screen()
# Mehmet = turtle.Turtle()
# Mehmet.shape("turtle")
#
# Mehmet.forward(100)
# for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
#     Mehmet.left(i)
#     Mehmet.forward(100)
#
# scr.exitonclick()



#Exercise 7
# scr = turtle.Screen()
# Mitya = turtle.Turtle()
# Mitya.shape("turtle")
# Mitya.color("blue")
# Mitya.pensize(3)
#
# Mitya.left(36)
# for i in range(5):
#     Mitya.forward(300)
#     Mitya.left(144)
#
# scr.exitonclick()



#Exercise 9
scr = turtle.Screen()
brudah = turtle.Turtle()
brudah.shape("circle")
brudah.stamp()

legQuantity = int(input("How many legs do you want on your sprite?   -"))

for i in range(legQuantity):
    brudah.forward(200)
    brudah.backward(200)
    brudah.left(360/legQuantity)

scr.exitonclick()