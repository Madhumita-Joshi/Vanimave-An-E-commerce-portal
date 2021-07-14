from tkinter import*
import sqlite3
import datetime

  
class billing:
  def __init__(self,cust_id,product_data,prev_page):
       self.data = product_data
       #initialising cursor
       self.c_id=cust_id
       self.connection =sqlite3.connect('Product.db')
       self.cursor=self.connection.cursor()
       self.prev_page = prev_page
       self.sum = 0
       for row in self.data:
           self.sum = self.sum + row[0]*row[1]
       
      #first page
       self.flag=0
       self.h=Tk()
       self.h.geometry("1366x700")
       self.h.config(bg="blue4")
       self.top=Label(self.h,width=250,height=3,bg="black")
       self.top.place(x=0,y=0)

      #adding cash/card function
       self.t4=Label(self.h,text="Select mode of payment",bg="blue4",fg="white")
       self.t4.config(font=("Sans serif", 30, 'bold'))
       self.t4.place(x=570,y=150,width=500,height=100)
       self.B1=Button(self.h,text="Cash",command=lambda:self.last(2)).place(x=760,y=300,width=100)
       self.B2=Button(self.h,text="Card",command=lambda:self.card(1))
       self.B2.place(x=760,y=380,width=100)
       #back 1
       self.back1=Button(self.h,text="Back",fg="black",padx = 15,command=lambda:self.back(1),font=("Sans serif", 12))
       self.back1.place(x=5,y=7,width = 130, height = 30)
       self.connection.commit()   
    

  def last(self,flag):
        
        #last page
        self.flag = flag
        self.k=Tk()
        self.k.geometry("1920x1080")
        self.k.config(bg="snow")
        self.counter = 0

       
        if(self.flag==2):
          self.h.destroy()
          self.mode="Cash on Delivery"
          
        elif(self.flag==3):
          self.mode="Card Payment"
          self.pn=self.e4.get()
          self.q.destroy()
          
        #total bill logic
        g=160
        self.now    = datetime.datetime.now()
        tax=(5/100)*self.sum
        self.net=self.sum+673+tax
        
        

        #final cart
        self.f1 = Frame(self.k, bd=1, bg="blue4", relief=SUNKEN,width=1200,height=800)
        self.f1.place(x=820, y=0)
        self.p1=Label(self.k,text="CART",bg="blue4",fg="white",font = ('sans serif',20,'normal','underline'))
        self.p1.place(x=1100,y=40)
        for row in self.data:
            nameLabel = Label(self.k, text=row[3]+' '+row[2]+' '+row[4],font=('sans serif',14),fg="white",bg="blue4")
            priceLabel = Label(self.k, text="Rs. %s"%row[0],font=('sans serif',14),fg="white",bg="blue4")
            quantityLabel = Label(self.k, text=row[1],font=('sans serif',14),fg="white",bg="blue4")
            nameLabel.place(x=850,y=g)
            priceLabel.place(x=1220,y=g)
            quantityLabel.place(x=1180,y=g)
            g=g+40

        #billing page gui
        
        self.p1=Label(self.k,text="Product",bg="blue4",fg="white",font = ('sans serif',15,'normal','underline'))
        self.p1.place(x=850,y=100)
        self.p2=Label(self.k,text="Qt.",bg="blue4",fg="white",font = ('sans serif',15,'normal','underline'))
        self.p2.place(x=1180,y=100)
        self.p3=Label(self.k,text="Price",bg="blue4",fg="white",font = ('sans serif',15,'normal','underline'))
        self.p3.place(x=1240,y=100)
        

        
        self.cursor.execute("select Username from user where cust_id=?",(self.c_id,))
        self.b=self.cursor.fetchone()
        self.l1=Label(self.f1,text=self.b[0],bg="blue4",fg="white",font = ('sans serif',15,'normal'))
        self.l1.place(x=70,y=0)
        self.l2=Label(self.f1,text="User :",bg="blue4",fg="white",font = ('sans serif',15,'normal'))
        self.l2.place(x=0,y=0)
        self.l3=Label(self.k,text="Amount :",bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.l3.place(x=370,y=130)
        self.l4=Label(self.k,text=self.sum,bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.l4.place(x=590,y=130)
        self.l5=Label(self.k,text="Rs.",bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.l5.place(x=530,y=130)
        self.l6=Label(self.k,text="Delivery charges:",bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.l6.place(x=270,y=180)
        self.l7=Label(self.k,text="673",bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.l7.place(x=590,y=180)
        self.l8=Label(self.k,text="Rs.",bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.l8.place(x=530,y=180)
        self.l9=Label(self.k,text="GST:",bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.l9.place(x=420,y=230)
        self.l10=Label(self.k,text=tax,bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.l10.place(x=590,y=230)
        self.l11=Label(self.k,text="Rs.",bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.l11.place(x=530,y=230)
        self.m1=Label(self.k,text="Net Amount :",bg="snow",fg="red",font = ('sans serif',20,'normal'))
        self.m1.place(x=320,y=300)
        self.m2=Label(self.k,text=self.net,bg="snow",fg="red",font = ('sans serif',20,'normal'))
        self.m2.place(x=590,y=300)
        self.m3=Label(self.k,text="Rs.",bg="snow",fg="red",font = ('sans serif',20,'normal'))
        self.m3.place(x=530,y=300)
        self.cursor.execute("select address from user where cust_id=?",(self.c_id,))
        for i in self.cursor.fetchall():
            self.d=i
        self.m4=Label(self.k,text="Deliver to :",bg="snow",fg="blue4",font = ('sans serif',20,'normal'),)
        self.m4.place(x=340,y=400)
        self.m5=Label(self.k,text=self.d[0],bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.m5.place(x=530,y=400)
        self.m8=Label(self.k,text="Payment mode:",bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.m8.place(x=290,y=450)
        
        self.m9=Label(self.k,text=self.mode,bg="snow",fg="blue4",font = ('sans serif',20,'normal'))
        self.m9.place(x=530,y=450)
        

        #confirm button
        self.B=Button(self.k,text="CONFIRM",command=self.ty,bg="blue4",fg='white',width=10)
        self.B.place(x=490,y=600)
        

        if(self.flag == 2):
            self.back3=Button(self.k,text="Back",fg="black",padx = 15,font=("Sans serif", 12),command=lambda:self.back(2))
            self.back3.place(x=5,y=7,width = 130, height = 30)
        elif(self.flag == 3):
            self.back3=Button(self.k,text="Back",fg="black",padx = 15,font=("Sans serif", 12),command=lambda:self.back(3))
            self.back3.place(x=5,y=7,width = 130, height = 30)


  def card(self,index):
      self.counter = 1
      if(index == 1):
          self.h.destroy()
      else:
          pass
     #account detail
      self.q=Tk()
      self.q.geometry("1920x1080")
      self.q.config(bg="blue4")
      self.top=Label(self.q,width=250,height=3,bg="black")
      self.top.place(x=0,y=0)
      self.t9=Label(self.q,text="Enter Account number",height=2,bg="blue4",fg="white",font = ('sans serif',16,'normal'))
      self.t9.place(x=630,y=100)
      self.e2=Entry(self.q)
      self.e2.place(x=630,y=150,width=210)
      self.b2=Button(self.q,text="Submit",command=self.cvv)
      self.b2.place(x=850,y=150,width=100,height=21)
      self.back2=Button(self.q,text="Back",fg="black",padx = 15,command=lambda:self.back(2),font=("Sans serif", 12))
      self.back2.place(x=5,y=7,width = 130, height = 30)
        
  def cvv(self):
        
        self.ac=self.e2.get()
        self.t10=Label(self.q,text="Enter cvv ",height=2,bg="blue4",fg="white",font = ('sans serif',16,'normal'))
        self.t10.place(x=630,y=220)
        self.e3=Entry(self.q)
        self.e3.place(x=630,y=270,width=210)
        self.b3=Button(self.q,text="Submit",command=self.pin)
        self.b3.place(x=850,y=270,width=100,height=21)
       
  def pin(self):
        self.cv=self.e3.get()
        self.flag=1
        self.t11=Label(self.q,text="Enter pin ",height=2,bg="blue4",fg="white",font = ('sans serif',16,'normal'))
        self.t11.place(x=630,y=340)
        self.t11.config(font=("Sans serif",11))
        self.e4=Entry(self.q)
        self.e4.place(x=630,y=390,width=210)
        self.b4=Button(self.q,text="Submit",command=lambda:self.last(3))
        self.b4.place(x=850,y=390,width=100,height=21)

  def ty(self):
      
       self.B.destroy()
       if self.flag==2:
         self.cursor.execute("INSERT into payment(bill,cust_id,type) values(?,?,'Cash')",(self.net,self.c_id))
         self.connection.commit()
       elif(self.flag == 3):
         self.cursor.execute("INSERT into payment(bill,cust_id,cvv,acc_no,pin,type) values(?,?,?,?,?,'Card')",(self.net,self.c_id,self.cv,self.ac,self.pn))
         self.connection.commit()

       self.cursor.execute("select p_id,quantity from cart where cust_id = ?",(self.c_id,))
       self.quantity = self.cursor.fetchall()
       self.connection.commit()
       for row in self.quantity:
           self.cursor.execute("UPDATE Product set quantity = quantity - ? where p_id = ?",(row[1],row[0]))
           self.connection.commit()

       self.cursor.execute("Delete from cart where cust_id=?",(self.c_id,))
       self.connection.commit()
       
       self.cursor.execute("select max(ord_id) from payment where cust_id = ?",(self.c_id,))
       self.ord_id = self.cursor.fetchall()
       self.m6=Label(self.k,text="Your order was placed at:",bg="snow",fg="red",font = ('sans serif',20,'normal'))
       self.m6.place(x=215,y=600)
       self.m7=Label(self.k,text=self.now.strftime("%B %d, %Y %H:%M:%S"),bg="snow",fg="red",font = ('sans serif',20,'normal'))
       self.m7.place(x=550,y=600)
       self.p5=Label(self.k,text='Your Order ID is = '+str(self.ord_id[0][0]),bg="blue4",fg="yellow",font = ('sans serif',15,'normal'))
       self.p5.place(x=430,y=530)       
       self.thanks = Label(self.f1,text = "Thank you for shopping at Vanimave!",bg = 'blue4',fg = 'white',font= ('sans serif',20,'bold'))
       self.thanks.place(x =25,y=600)
       self.back3.destroy()
       self.back4=Button(self.k,text="Back to store",fg="black",padx = 15,command=lambda:self.back(4),font=("Sans serif", 12))
       self.back4.place(x=5,y=7,width = 130, height = 30)

  def back(self,index):
       self.index = index
       
       if(self.index == 1):
           
           self.h.destroy()
           import cart
           c=cart.Cart(self.c_id,self.prev_page)
           
       elif(self.index == 2):
           if(self.counter == 0):
               self.k.destroy()
           elif(self.counter == 1):
               self.q.destroy()
           self.__init__(self.c_id,self.data,self.prev_page)

       elif(self.index == 3):
           self.k.destroy()
           self.card(0)
           
       elif(self.index == 4):
           self.k.destroy()
           import main_page
           m = main_page.MainPage(self.c_id)

