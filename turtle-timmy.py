import turtle
from turtle import Turtle,Screen
import random

my_Turtle = Turtle()
my_Turtle.width(2)
my_Turtle.shape()
turtle.colormode(255)
#Drawing a dashed square
# def one_line():
#   for i in range(10):
#      Ahmad_Turtle.pendown()
#      Ahmad_Turtle.forward(10)
#      Ahmad_Turtle.penup()
#      Ahmad_Turtle.forward(10)
#
# for i in range (4):
#     one_line()
#     Ahmad_Turtle.right(90)



#Drawing triangel,square,pentagon,hexagon,heptagon,......
# Ahmad_Turtle.color(random.choice(colors))
# for i in range(3):
#
#    Ahmad_Turtle.forward(100)
#    Ahmad_Turtle.right(120)
#
# Ahmad_Turtle.color(random.choice(colors))
# for i in range(4):
#
#    Ahmad_Turtle.forward(100)
#    Ahmad_Turtle.right(90)
#
# Ahmad_Turtle.color(random.choice(colors))
# for i in range(5):
#
#    Ahmad_Turtle.forward(100)
#    Ahmad_Turtle.right(72)
#
# Ahmad_Turtle.color(random.choice(colors))
# for i in range(6):
#
#    Ahmad_Turtle.forward(100)
#    Ahmad_Turtle.right(60)
#
# Ahmad_Turtle.color(random.choice(colors))
# for i in range(7):
#
#    Ahmad_Turtle.forward(100)
#    Ahmad_Turtle.right(float(360/7))
#
# Ahmad_Turtle.color(random.choice(colors))
# for i in range(8):
#
#    Ahmad_Turtle.forward(100)
#    Ahmad_Turtle.right(float(360/8))
#
# Ahmad_Turtle.color(random.choice(colors))
# for i in range(9):
#
#    Ahmad_Turtle.forward(100)
#    Ahmad_Turtle.right(float(360/9))
#
# Ahmad_Turtle.color(random.choice(colors))
# for i in range(10):
#
#    Ahmad_Turtle.forward(100)
#    Ahmad_Turtle.right(float(360/10))

# drawing a random turtle movement with random color choices

def random_color():
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   return (r,g,b)

a=True

# direction=[0,90,180,270]
#
# Ahmad_Turtle.pensize(10)
#
#
# for i in range(1,1000):
#        Ahmad_Turtle.color(random_color())
#        Ahmad_Turtle.forward(30)
#        Ahmad_Turtle.setheading(random.choice(direction))
my_Turtle.speed("fastest")
my_Turtle.color(random_color())
my_Turtle.circle(100)
x=my_Turtle.heading()
print(x)
while x<360:
   y = x+10
   my_Turtle.setheading(y)
   my_Turtle.color(random_color())
   my_Turtle.circle(100)
   x=y





screen= Screen()
screen.exitonclick()


