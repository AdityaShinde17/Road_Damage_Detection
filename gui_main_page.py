# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:37:36 2023

@author: sheet
"""

import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For image recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Road Damage Detection")
#------------------Frame----------------------



#-------function------------------------

def reg():
    
##### tkinter window ######
    
    print("reg")
    from subprocess import call
    call(["python", "registration.py"])   



def login():
    
##### tkinter window ######
    
    print("log")
    from subprocess import call
    call(["python", "login.py"])   
    


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('m1.jpeg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Road Damage Detection", font=('times', 40,' bold '), height=1, width=50,bg="brown",fg="white")
lbl.place(x=0, y=0)

framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="pink")
framed.grid(row=0, column=0, sticky='nw')
framed.place(x=20, y=90)
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(framed, text='Login Now',width=15,height=2,bg='dark blue',fg='white',command=login,font='bold').place(x=30,y=65)
button1 = tk.Button(framed, text='Register',width=15,height=2,bg='dark blue',fg='white',command=reg,font='bold').place(x=250,y=65)


root.mainloop()
