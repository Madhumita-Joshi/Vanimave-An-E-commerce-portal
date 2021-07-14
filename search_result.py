# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 00:20:13 2020

@author: Nishant
"""

from tkinter import *
import sqlite3

class search_:
        
    def __init__(self,s_result,cust_id,pid):
        self.s_result = s_result
        self.cust_id = cust_id
        self.pid = pid
        self.t = Tk()
        self.t.geometry("1920x1080")
        self.f1 = Frame(self.t,bg = "Blue4",width = 1920,height = 80,relief = SUNKEN,bd = 2)
        self.f2 = Frame(self.t,bg = "Blue4",width = 1920,height = 900)
        self.f1.pack(side = TOP)
        self.f2.pack()
        self.title = Label(self.f1,text = 'Search Results',font = ('Sans serif',30,'bold','underline'),bg = 'blue4',fg = 'white')
        self.title.place(x = 610,y = 30)
        self.proname = Label(self.f2,text = 'Product Name',font = ('comic sans',20,'bold'), fg = 'khaki',bg = 'blue4')
        self.price = Label(self.f2,text = 'PRICE',font = ('comic sans',20,'bold'), fg = 'khaki',bg = 'blue4')
        self.proname.place(x = 100,y = 50)
        self.price.place(x = 650,y = 50)
        self.back = Button(self.f1,text = 'Back',fg = 'black',bg = 'blue3',activebackground = 'yellow',padx = 20,command = self.back)
        self.back.place(x = 30,y = 50,width = 75)
        self.sort = Button(self.f1,text = 'Sort by price',fg = 'white',bg = 'blue3',command = self.sort)
        self.sort.place(x = 1250,y = 50)
        self.y = 120
        for i in self.s_result:
            self.place(i,self.y)
            self.y = self.y + 50
        self.t.mainloop()
        
    def place(self,i,y):
        
        self.item = Label(self.f2,text = i[1]+' '+i[2]+' '+i[0],font = ('Sans serif',15),anchor = W,bg = 'blue4',fg = 'white')
        self.item.place(x = 100, y = y)
        self.item_price = Label(self.f2,text = 'RS. '+ str(i[5]),font = ('sans serif',15),bg = 'blue4',fg = 'white')
        self.item_price.place(x = 650, y = y)
        self.view = Button(self.f2,text = 'View product',command = lambda i=i: self.view_prod(i))
        self.view.place(x = 900, y = y)
        
    def view_prod(self,data):
        self.t.destroy()
        from sel_product import sel_product
        sp = sel_product(data[4],self.cust_id)

    def back(self):
        self.t.destroy()
        import sel_product
        s = sel_product.sel_product(self.pid,self.cust_id)
        
    def sort(self):
        self.f2.destroy()
        self.f2 = Frame(self.t,bg = "Blue4",width = 1920,height = 900)
        self.f2.pack()
        self.proname = Label(self.f2,text = 'Product Name',font = ('comic sans',20,'bold'), fg = 'khaki',bg = 'blue4')
        self.price = Label(self.f2,text = 'PRICE',font = ('comic sans',20,'bold'), fg = 'khaki',bg = 'blue4')
        self.proname.place(x = 100,y = 50)
        self.price.place(x = 650,y = 50)
        self.s_result.sort(key = lambda x:x[5])
        self.y = 120
        for i in self.s_result:
            self.place(i,self.y)
            self.y = self.y + 50
    
