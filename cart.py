


import sqlite3
from tkinter import *


class Cart:
    def __init__(self,cid,prev_page):
        self.cust_id = cid
        self.s=0
        self.tp=1
        self.cart=Tk()
        self.cart.config(bg = "blue4")
        self.cart.geometry('1920x1080')
        self.con=sqlite3.connect('Product.db')
        self.cur=self.con.cursor()
        self.c = 0
        self.prev_page = prev_page

        
        
        
        #cart=Toplevel()
        
        self.top=Frame(self.cart,bg = "blue4")
        self.top.pack(side=TOP,fill = X)
        self.car=LabelFrame(self.cart,text='Cart Items',height = 400,width = 1900,font = ("dejavu sans",20,"bold"),fg = "white",bg = "blue4")
        self.car.pack(fill = BOTH,expand = YES,padx='20')
        self.checkOutFrame = Frame(self.cart,bg = "blue4")
        self.checkOutFrame.pack(expand = YES)
        #self.index = 0
        
        self.place()
        self.cart.title('Cart')
        self.backToStoreBtn = Button(self.top, text="Back To Store", font=("Candara",15,"bold"),fg="red",bg="white",cursor="hand2",command=self.back)
        self.backToStoreBtn.pack(side = LEFT)
        
        
        
        self.cart.mainloop()
    
    def place(self):
        self.cur.execute('select c.price,c.quantity,p.product_name,p.brand,p.category,c.p_id from Product p, Cart c where p.p_id = c.p_id and cust_id = ?',(self.cust_id,))
        #self.con.commit()
        self.data = self.cur.fetchall()
        
        self.l1=Label(self.car,text="Product Name",font=("Candara",18,"underline"),fg="white",bg = "blue4")
        self.l1.place(x=100,y=50,width=300,height=30)
        self.l2=Label(self.car,text="Price",font=("Candara",18,"underline"),fg="white",bg = "blue4")
        self.l2.place(x=645,y=50,width=90,height=30)
        self.l3=Label(self.car,text="Quantity",font=("Candara",18,"underline"),fg="white",bg = "blue4")
        self.l3.place(x=950,y=50,width=90,height=30)
        x=100
        y=100
        for row in self.data:
            buttons=[]

            nameLabel = Label(self.car, text=row[3]+' '+row[2]+' '+row[4],font=("Candara",15),fg="white",bg = "blue4",anchor = W)
            priceLabel = Label(self.car, text="Rs. %s"%row[0],font=("Candara",13),fg="yellow",bg = "blue4")
            quantityLabel = Label(self.car, text=row[1],font=("Candara",15),fg="white",bg = "blue4")
        
            remfrCartBtn = Button(self.car, text="Remove From Cart", font=("Candara",11,"bold"),fg="red",bg="white",cursor="hand2", command=lambda row=row:self.remove(row))

            buttons.append(row)
            nameLabel.place(x=100,y=y,width=500,height=30)
            priceLabel.place(x=650,y=y,width=90,height=30)
            quantityLabel.place(x=950,y=y,width=90,height=30)
            remfrCartBtn.place(x=1100,y=y,width=150,height=30)
            #self.index += 1    
            self.tp=row[0]*row[1]
            self.s=self.s+self.tp
            y=y+40
        if(self.data == []):
            #self.car.destroy()
            self.l1.destroy()
            self.l2.destroy()
            self.l3.destroy()
            self.empty = Label(self.cart,text='Cart is empty',font = ('Candara',20,'italic'),fg = 'red',bg = "blue4")
            self.empty.place(x=550,y=200,width=400,height=50)
        self.totalPriceLabel = Label(self.checkOutFrame, text="Total Price : Rs. %s" %self.s , font=("Candara",14,"bold"),fg="white",bg = "blue4")
        self.totalPriceLabel.pack(side = LEFT)
        self.buyBtn = Button(self.checkOutFrame, text="Buy Now", font=("Candara",15,"bold"),fg="indigo",bg="white",cursor="hand2",command=lambda:self.bn(self.cust_id,self.data),relief = RAISED,bd = 3)
        self.buyBtn.pack(padx="10")
        
    def remove(self,row):
        self.cur.execute("DELETE from cart where p_id = ?",(row[5],))
        self.con.commit()
        self.car.destroy()
        self.checkOutFrame.destroy()
        
        self.car=LabelFrame(self.cart,text='Cart Items',bg = "blue4",font = ("dejavu sans",20,"bold"),fg = "white")
        self.car.pack(fill='both',expand='yes',padx='20',pady='10')
        self.checkOutFrame = Frame(self.cart, pady="10",bg = "blue4")
        self.checkOutFrame.pack(expand = 'yes')
        self.s = 0
        self.tp = 0
        self.place()

    def bn(self,cust_id,data):
        if(data != []):
            self.cart.destroy()
            import billing
            b = billing.billing(self.cust_id,data,self.prev_page)
        elif(data == []):
            self.emp = Label(self.checkOutFrame,text = "Cart is empty",fg = 'red',bg = 'blue4',font = ('Times',15,'italic'))
            self.emp.pack(side = BOTTOM)
            self.emp.after(1500,self.emp.destroy)
            
    def back(self):
        self.cart.destroy()
        if(self.prev_page == 'mp'):            
            import main_page
            m = main_page.MainPage(self.cust_id)
            
        elif(str(int(self.prev_page)).isdigit()):
            import sel_product
            s = sel_product.sel_product(self.prev_page,self.cust_id)



