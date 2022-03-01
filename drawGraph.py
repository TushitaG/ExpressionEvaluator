# Name: Tushita Govindaraj
# StudentID: 2012155
# Class: DAAA/FT/2B/02
from turtle import Turtle, Screen, mainloop

class GraphTurtle(Turtle):
    #Draw the axis in turtle screen. 
    def drawAxis(self):
        myPen = Turtle()
        myPen.speed(0)
        screen = Screen()
        screen.bgcolor("#000000")
        myPen.pensize(2)
        myPen.color("white")
        myPen.penup()
        myPen.goto(-200,0)
        myPen.pendown()
        myPen.goto(200,0)
        myPen.penup()
        myPen.goto(0,-200)
        myPen.pendown()
        myPen.goto(0,200)
        
    #Draw a line graph on existing turtle screen according to gradient and constant specified by user
    def drawLinearGraph(self,a,c):
        
        myPen = Turtle()
        myPen.color('white')
        myPen.penup()

        for x in range(-50,51):
            y = a * x + c
            myPen.goto(x,y)
            myPen.pendown()
        
        myPen.penup()
        myPen.goto(-100,100)
        equation = ""
        if a==0:
            equation = " y = " + str(c)
        else:
            if c>0:
                equation = " y = " + str(a) + "x + " + str(c) 
            elif c<0:
                equation = " y = " + str(a) + "x " + str(c) 
            else:
                equation = " y = " + str(a)

        myPen.write(equation,"14pt bold")
        mainloop()