from turtle import *

bgcolor("black")
color("orange")
pensize(3)
shape("circle")

for i in range(8):
    right(45)
    for j in range(8):
        forward(60)
        left(45)

exit()