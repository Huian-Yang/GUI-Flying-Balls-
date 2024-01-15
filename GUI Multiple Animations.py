from tkinter import *
from Ball_Class import *
import time

window = Tk()

WIDTH = 500  #constant (not gonna change)
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,120,8,7,"orange")

while True:
    volley_ball.move() #call move function
    tennis_ball.move()
    basket_ball.move()
    window.update() #refreshes the window
    time.sleep(0.01) #time delay
    
window.mainloop()