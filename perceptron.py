# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
import numpy as np
import time

trainingData = []
w1 = 0.0
w2 = 0.0
bias = 0.0
learningRate = 0.1
numEpochs = 30

WIDTH = 1000
HEIGHT = 600


def drawLines():
                my_canvas.delete("all")
                m = -w1/w2
                c = bias/w2
    
                x0 = 0
                y0 = c
                x1 = 5
                y1 = 5*m+c
    
                Ux = x1-x0
                Uy = y1-y0
    
                Umagnitude = np.sqrt(Ux*Ux+Uy*Uy)
    
                Ux = Ux/Umagnitude
                Uy = Uy/Umagnitude
    
                Ux = 100000*Ux
                Uy = 100000*Uy
            
                x0 = (x0*WIDTH/10)+WIDTH/2
                Ux = (Ux*WIDTH/10)+WIDTH/2
                y0 = (y0*HEIGHT/-10)+HEIGHT/2
                Uy = (Uy*HEIGHT/-10)+HEIGHT/2
    
                
                my_canvas.create_line(x0,y0,Ux,Uy,fill="black")
                my_canvas.create_line(x0,y0,-Ux,-Uy,fill="black")
                drawTrainingData()
              


def randomizeWeights():
    global w1
    global w2
    global bias
    
    my_canvas.delete("all")
    w1 = np.random.uniform(-1,1)
    w1String.set(str(w1))
    w2 = np.random.uniform(-1,1)
    w2String.set(str(w2))
    bias = np.random.uniform(-1,1)
    biasString.set(str(bias))
    
    m = -w1/w2
    c = bias/w2
    
    x0 = 0
    y0 = c
    x1 = 5
    y1 = 5*m+c
    
    Ux = x1-x0
    Uy = y1-y0
    
    Umagnitude = np.sqrt(Ux*Ux+Uy*Uy)
    
    Ux = Ux/Umagnitude
    Uy = Uy/Umagnitude
    
    Ux = 10000*Ux
    Uy = 10000*Uy
    
    
    x0 = (x0*WIDTH/10)+WIDTH/2
    Ux = (Ux*WIDTH/10)+WIDTH/2
    y0 = (y0*HEIGHT/-10)+HEIGHT/2
    Uy = (Uy*HEIGHT/-10)+HEIGHT/2
    
    line1 = my_canvas.create_line(x0,y0,Ux,Uy,fill="black")
    line2 = my_canvas.create_line(x0,y0,-Ux,-Uy,fill="black")
    drawTrainingData()
   
  
def resetData():
    trainingData.clear()
    randomizeWeights()
    my_canvas.delete("all")
    resultString.set("")
    
def train():
    global w1
    global w2
    global bias
    global learningRate
    global numEpochs
    
    
   
    learningRate = float(learningRateEntry.get())
    numEpochs = int(numepochsEntry.get())
    done = False
    currentEpoch = 1
    while(not done and (currentEpoch<(numEpochs+1))):
        done = True
        for item in trainingData:
            net = w1*item[0]+w2*item[1]-bias
            pw = 0
            if(net>=0):
                pw = 1
            else:
                pw = 0
                
            error = item[2]-pw
            if(error!=0):
                
                done = False
                bias = bias - learningRate*error
                biasString.set(str(bias))
                w1 = w1+learningRate*error*item[0]
                w1String.set(str(w1))
                w2 = w2+learningRate*error*item[1]
                w2String.set(str(w2))
                drawLines()
                
                
                
        currentEpoch = currentEpoch+1
                
   
    res = ""
    if(currentEpoch==(numEpochs+1)):
        res = "Failed at traning"
    else:
        res = "Training succeded"
        

    resultString.set("Finished traning.      Number of epochs: "+str(currentEpoch-1)+"\n "+res)
    
   
        
    
    
    
     
def evaluateData():
    global w1
    global w2 
    global bias
    
    for i in range(0,1000,10):
        for j in range(0,600,10):
            x = (i-WIDTH/2)*(10/WIDTH)
            y = (j-HEIGHT/2)*(-10/HEIGHT)
            net = x*w1+y*w2-bias
            pw = 0
            if(net>=0):
                pw = 1
            else:
                pw = 0
            if(pw==0):
                 my_canvas.create_oval(i,j,i+8,j+8,outline="cyan")
            else:
                 my_canvas.create_rectangle(i,j,i+8,j+8,outline="orange")
                
    
def leftClick(event):
    x = (event.x-WIDTH/2.0)*(10/WIDTH)
    y = (event.y-HEIGHT/2.0)*(-10/HEIGHT)
    trainingData.append([x,y,0])
    my_canvas.create_oval(event.x,event.y,event.x+8,event.y+8,outline="blue")
    
def rightClick(event):
    x = (event.x-WIDTH/2.0)*(10/WIDTH)
    y = (event.y-HEIGHT/2.0)*(-10/HEIGHT)
    trainingData.append([x,y,1])
    my_canvas.create_rectangle(event.x,event.y,event.x+8,event.y+8,outline="red")
    
    
def drawTrainingData():
    for item in trainingData:
        if(item[2]==0):
            x = (item[0]*WIDTH/10)+WIDTH/2
            y = (item[1]*HEIGHT/-10)+HEIGHT/2
            my_canvas.create_oval(x,y,x+8,y+8,outline="blue")
            
        elif(item[2]==1):
            x = (item[0]*WIDTH/10)+WIDTH/2
            y = (item[1]*HEIGHT/-10)+HEIGHT/2
            my_canvas.create_rectangle(x,y,x+8,y+8,outline="red")
            
   

root = Tk()



w1String = StringVar()
w2String = StringVar()
biasString = StringVar()
resultString = StringVar()

w1String.set("0.0")
w2String.set("0.0")
biasString.set("0.0")
resultString.set("")

root.title("Perceptrón")
root.geometry("1600x800")

my_canvas = Canvas(root,width=WIDTH,height=HEIGHT,bg="white")
my_canvas.bind("<Button-1>",leftClick)
my_canvas.bind("<Button-3>",rightClick)
my_canvas.grid(row=0,column=0,pady=20,padx=20)


button0 = Button(root,text="Randomize weights",pady=20,padx=10,command=randomizeWeights)
button0.grid(row=0,column=1)

button1 = Button(root,text="Start training",pady=20,padx=10,command=train)
button1.grid(row=1,column=1)

button2 = Button(root,text="Evaluate data",pady=20,padx=10,command=evaluateData)
button2.grid(row=2,column=1)

learningRateEntry = Entry(root)
learningRateEntry.insert(END,'.1')
learningRateEntry.grid(row=1,column=2)

learningRateLabel = Label(root,text="Learning Rate")
learningRateLabel.grid(row=1,column=3)

numepochsEntry = Entry(root)
numepochsEntry.insert(END,'100')
numepochsEntry.grid(row=2,column=2)

numepochsLabel = Label(root,text="Number of epochs")
numepochsLabel.grid(row=2,column=3)

w1Label = Label(root,text='w1   ')
w1Label.grid(row=1,column=4)

w1ValueLabel = Label(root,textvariable=w1String)
w1ValueLabel.grid(row=1,column=5)

w2Label = Label(root,text='w2')
w2Label.grid(row=2,column=4)

w2ValueLabel = Label(root,textvariable=w2String)
w2ValueLabel.grid(row=2,column=5)

biasLabel = Label(root,text='bias')
biasLabel.grid(row=3,column=4)

biasValueLabel = Label(root,textvariable=biasString)
biasValueLabel.grid(row=3,column=5)

resetButton = Button(root,text="Reset training data",command=resetData)
resetButton.grid(row=1,column=0)

ResultLabel = Label(root,textvariable=resultString)
ResultLabel.grid(row=2,column=0)


root.mainloop()