from turtle import *

#painting a house
#drawing a square
speed(15)
width(7)
color("orange")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#door

forward(70)
color("black")
begin_fill()
left(90)
forward(120) #heigh of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#windows
left(90)
penup()
goto(20, 180)
pendown()
right(60)
forward(40)
right(270)
forward(50)
right(270)
forward(40)
left(90)
forward(50)

penup()
goto(130, 180)
pendown()

left(90)

forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)

exitonclick()