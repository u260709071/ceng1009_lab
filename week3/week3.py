Current_Year = 2024
Birth_Year = int(input("""In which year were you born?
  """))

Age = Current_Year - Birth_Year
print("You are " + str(Age) + " years old.")import math
radius = float(input("""Give me the radius of the circle.
  """))
Circumference  = 2 * math.pi * radius
print(Circumference)
Starting_Day = str(input("""In which day will your vacation start at?
  """))
#I think i am using too many if's
if Starting_Day == "Monday":
    Starting_Day = 0
if Starting_Day == "Tuesday":
    Starting_Day = 1
if Starting_Day == "Wednesday":
    Starting_Day = 2
if Starting_Day == "Thursday":
    Starting_Day = 3
if Starting_Day == "Friday":
    Starting_Day = 4
if Starting_Day == "Saturday":
    Starting_Day = 5
if Starting_Day == "Sunday":
    Starting_Day = 6

Vacation_Length = int(input("""How many days will your vacation take?
  """))

End_of_Vacation = (Starting_Day + Vacation_Length) % 7

if End_of_Vacation == 0:
    End_of_Vacation = "Monday"
if End_of_Vacation == 1:
    End_of_Vacation = "Tuesday"
if End_of_Vacation == 2:
    End_of_Vacation = "Wednesday"
if End_of_Vacation == 3:
    End_of_Vacation = "Thursday"
if End_of_Vacation == 4:
    End_of_Vacation = "Friday"
if End_of_Vacation == 5:
    End_of_Vacation = "Saturday"
if End_of_Vacation == 6:
    End_of_Vacation = "Sunday"

print("Your vacation will end at a " + End_of_Vacation)

Fahrenheit = float(input("""How many Fahrenheits should i convert to Celcius
  """))
Celsius = (Fahrenheit - 32) * 5 / 9

print( str(Fahrenheit) + " Fahrenheit is " + str(Celsius) + " Celsius")print("Let me compute your MPG.")

Miles_Driven = float(input("""How many miles have u driven for?
  """))
Gallons_Used = float(input("""How many gallons have you used?"""))

print("Your MPG is " + str(Miles_Driven/Gallons_Used))print("")

Length1 = float(input("""Enter the first length of the rectangle.
  """))
Length2 = float(input("""Enter the second length of the rectangle.
  """))

print("The Area of your rectangle is " + str(Length1 * Length2))
starting_day = int(input("Enter the starting day: "))
length_of_vacation = int(input("Enter the length: "))

total = starting_day + length_of_vacation
print("Your vacation will end at day " + str((total % 7)))
