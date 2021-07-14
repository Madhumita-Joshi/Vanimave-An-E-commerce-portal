# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:48:40 2020

@author: Nishant
"""

from tkinter import *
import sqlite3
import time

class Login:
    def __init__(self):
        #creating a frame
        self.t = Tk()
        self.t.geometry("1920x1080")
        self.t.title("Vanimave")
        #self.t = t
        self.f1 = Frame(self.t,bg = 'blue4',width = 1920,height = 200)
        self.f1.pack(fill = BOTH)
        self.f2 = Frame(self.t,bg = 'Blue4',width = 1920, height = 350)
        self.f2.pack(fill = BOTH)
        self.f3 = Frame(self.t,bg = 'Blue4',width = 1920, height = 400)
        self.f3.pack(fill = BOTH)
        self.greet = Label(self.f1,text = 'Welcome To ',fg = 'White',bg = 'Blue4',font = ('sans serif',50,'bold'),justify = CENTER)
        self.greet_v = Label(self.f1,text = 'V',fg = 'White',bg = 'Blue4',font = ('Times',80,'bold','italic'),justify = CENTER)
        self.greet_ = Label(self.f1,text = 'animave',fg = 'White',bg = 'Blue4',font = ('sans serif',50,'bold'),justify = CENTER)
        self.greet.place(x = 420, y = 90)
        self.greet_v.place(x = 830,y = 65,width = 96)
        self.greet_.place(x = 920,y = 100,width = 265,height = 65)
        #adding labels and entry boxes
        self.uname = Label(self.f2,text = 'Username',fg = 'White',bg = 'Blue4',font = ('sans serif',20,'normal'))
        self.text1 = Entry(self.f2,bd = 2)
        self.pword = Label(self.f2,text = 'Password',fg = 'White',bg = 'Blue4',font = ('sans serif',20,'normal'))
        self.text2 = Entry(self.f2,bd = 2)
        self.text2.config(show = '*')
        
        self.uname.place(x = 630,y = 170)
        self.text1.place(x = 775,y = 180)
        self.pword.place(x = 632,y = 220)
        self.text2.place(x = 775,y = 230)
        
        #adding submit button
        self.submit = Button(self.f2,text = 'SUBMIT',fg = 'white',bg = 'Blue4',command = self.read)
        self.submit.place(x = 740, y =270)
        
        #adding sign up function
        self.new = Label(self.f3,text = "Don't have an account? Sign up by clicking here",bg = 'blue4',fg = 'yellow')
        self.signup = Button(self.f3,text = 'Sign Up',bg = 'Blue4',fg = 'white',command = self.add)
        self.new.place(x = 640, y=0)
        self.signup.place(x = 740, y =25)
        
        
        #initialising cursor
        self.connection = sqlite3.connect('Product.db')
        self.cursor = self.connection.cursor()   
        self.t.mainloop()
    def read(self):
            self.k = 0
            self.n = ''
            self.cursor.execute("SELECT * FROM user")
            data = self.cursor.fetchall()
            self.connection.commit()
            for i in data:
                if(self.text1.get() == i[0] and self.text2.get() == i[1]):
                    self.k = 1
                    self.n = i
                    
            if(self.k==1):
                self.t.destroy()
                import main_page
                m = main_page.MainPage(self.n[4])
                
            else:
                self.text2.delete(0,END)
                self.text1.delete(0,END)
                self.deny = Label(self.f2,text = "Invalid credentials",font = ('sans serif',15,'italic'),bg = 'blue4',fg = 'red')
                self.deny.place(x = 680,y = 135)
                self.deny.after(1000,self.deny.destroy)

    #call class of next page and pass cust_id as parameter
            #signup
    def add(self):
        #self.t.destroy()
        #self.t2= Tk()
        self.t2 = Toplevel(self.t)
        self.t2.geometry("1920x1080")
        self.t2.title("Sign Up")
        
        #frames
        self.signin = Frame(self.t2,bg = 'blue4',width = 1920,height = 200)
        self.frame = Frame(self.t2,bg = 'blue4',width = 1920,height = 600)
        self.signin.pack(fill = BOTH)
        self.frame.pack(fill = BOTH)
        
        #widgets for signup
        self.title = Label(self.signin,text = 'Sign Up',font = ('sans serif',50,'bold'),fg = 'white',bg = 'blue4')
        self.title.place(x = 630, y = 90)
        self.username = Label(self.frame,text = 'Username',font = ('sans serif',20),fg = 'white',bg = 'blue4')
        self.untext = Entry(self.frame,bd = 2)
        self.username.place(x = 630,y = 120)
        self.untext.place(x = 775,y = 130)
        self.password = Label(self.frame,text = 'Password',font = ('sans serif',20),fg = 'white',bg = 'blue4')
        self.ptext = Entry(self.frame,bd = 2)
        self.ptext.config(show = '*')
        self.password.place(x = 632,y = 170)
        self.ptext.place(x = 775,y = 180)
        self.email = Label(self.frame,text = 'Email',font = ('sans serif',20),fg = 'white',bg = 'blue4')
        self.etext = Entry(self.frame,bd = 2)
        self.email.place(x = 632,y = 220)
        self.etext.place(x = 775,y = 230)
        self.address = Label(self.frame,text = 'Address',font = ('sans serif',20),fg = 'white',bg = 'blue4')
        self.atext = Entry(self.frame,bd = 2)
        self.address.place(x = 630,y = 270)
        self.atext.place(x = 775,y = 280)
        self.submit = Button(self.frame,text = 'CREATE ACCOUNT',fg = 'white',bg = 'blue4',command = self.confirm)
        self.submit.place(x = 710,y = 330)
        
        
    def confirm(self):
        if(self.untext.get() != '' and self.ptext.get() != '' and self.etext.get() != '' and self.atext.get() != ''):
            try:    
                self.cursor.execute("INSERT INTO user(Username,Password,email,address) VALUES(?,?,?,?)",(self.untext.get(),self.ptext.get(),self.etext.get(),self.atext.get()))
                self.connection.commit()
                self.t2.destroy()
            
            except sqlite3.IntegrityError:
            
                self.atext.delete(0,END)
                self.etext.delete(0,END)
                self.ptext.delete(0,END)
                self.untext.delete(0,END)
                error = Label(self.frame,text = 'User already exists',fg = 'red',bg = 'blue4',font = ('Ariel',15))
                error.place(x = 670,y = 70)
                error.after(1500,error.destroy)
            
                
        else:
                
                error = Label(self.frame,text = 'Please enter details in all the fields',fg = 'red',bg = 'blue4',font = ('Ariel',15))
                error.place(x = 620,y = 70)
                error.after(1500,error.destroy)
        
        
l = Login()

