
# coding: utf-8

# In[31]:


#!/usr/bin/env python3

"""Planets.py: 模拟太阳系六行星运行公转

__author__ = "迟家明"
__pkuid__  = "1700012459"
__email__  = "chijiaming@pku.edu.cn"
"""


import math
import turtle

sun=turtle.Turtle() 
sun.shape("circle")
sun.color("yellow")

mercury=turtle.Turtle()
venus=turtle.Turtle()
earth=turtle.Turtle()
mars=turtle.Turtle()
jupiter=turtle.Turtle()
saturn=turtle.Turtle()

mercury.shape("circle")
venus.shape("circle")
earth.shape("circle")
mars.shape("circle")
jupiter.shape("circle")
saturn.shape("circle")

mercury.color("grey")
venus.color("orange")
earth.color("blue")
mars.color("red")
jupiter.color("green")
saturn.color("black")

mercury.hideturtle()
mercury.up()
mercury.forward(30)
mercury.left(90)
mercury.down()
mercury.showturtle()
mercury.pensize(1)

venus.hideturtle()
venus.up()
venus.forward(70)
venus.left(90)
venus.down()
venus.showturtle()
venus.pensize(1)

earth.hideturtle()
earth.up()
earth.forward(100)
earth.left(90)
earth.down()
earth.showturtle()
earth.pensize(1)

mars.hideturtle()
mars.up()
mars.forward(140)
mars.left(90)
mars.down()
mars.showturtle()
mars.pensize(1)

jupiter.hideturtle()
jupiter.up()
jupiter.forward(270)
jupiter.left(90)
jupiter.down()
jupiter.showturtle()
jupiter.pensize(1)

saturn.hideturtle()
saturn.up()
saturn.forward(390)
saturn.left(90)
saturn.down()
saturn.showturtle()
saturn.pensize(1)

"""第一部分：initialization of sun and planets"""

p=[mercury,venus,earth,mars,jupiter,saturn]
vx=[0,0,0,0,0,0]
vy=[270,190,170,140,100,80]
x=[1,1,1,1,1,1]
y=[1,1,1,1,1,1]
ax=[1,1,1,1,1,1]
ay=[1,1,1,1,1,1]

for i in range(100000):
    for j in range(6):
        t=0.01
        x[j],y[j]=p[j].position()       
        ax[j]=-3000000*x[j]*((x[j]**2+y[j]**2)**(-1.5))
        ay[j]=-3000000*y[j]*((x[j]**2+y[j]**2)**(-1.5))
        vx[j]=vx[j]+t*ax[j]
        vy[j]=vy[j]+t*ay[j]       
        p[j].goto(x[j]+vx[j]*t,y[j]+vy[j]*t)

"""第二部分：defining the motion of planets"""
     


