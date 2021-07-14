
#PASS CUST_ID AND P_ID OF THE SELECTED PRODUCT
from tkinter import *
import sqlite3
from PIL import Image, ImageTk

class sel_product:
    
    def __init__(self,pid,cust_id):
        self.cust_id = cust_id
        #creating new window
        self.root = Tk()
        self.root.geometry("1920x1080")
        self.root.title("Product Details")
        
        #initialising cursor and saving data
        self.connection = sqlite3.connect('Product.db')
        self.cursor = self.connection.cursor()  
        self.p_id = (pid,)
        self.cursor.execute("SELECT * from Product where P_id = ?",self.p_id)
        self.data = self.cursor.fetchall()
        #print(self.data)
        self.pro_name = self.data[0][2]
        self.quantity = self.data[0][3]
        self.price = self.data[0][5]
        self.p_id = pid
        
        self.cursor.execute("Select * from user where cust_id = ?",(self.cust_id,))
        self.userdata = self.cursor.fetchall()
        #print(self.userdata)
        

        #creating frames
        self.title = Frame(self.root,bg = 'blue4',width = 500,height = 150)
        self.f_search = Frame(self.root,bg = 'black',width = 350,height = 50)
        self.f = Frame(self.root,bg = 'blue4',width = 1920,height = 880)
        
        self.f_search.pack(side = TOP,fill = BOTH)
        self.title.pack(fill = X)
        self.f.pack(fill = BOTH)
        
        #title
        self.name = Label(self.title,text = self.data[0][1]+" "+self.pro_name,font = ('Times New Roman',25,'bold'),fg = 'white',bg = 'blue4',justify = LEFT,anchor = W)
        self.name.place(x = 50, y = 50, width = 550, height = 45)
        
        #search
        self.back = Button(self.f_search,text = 'Back',fg = 'black',bg = 'blue3',activebackground = 'yellow',padx = 20,command = self.back)
        self.search = Button(self.f_search,text = 'Search product',font = ('Ariel',12),fg = 'white',bg = 'blue4',command = self.search)
        self.searchbar = Entry(self.f_search,bd = 2,text = 'search')
        
        self.back.place(x = 5, y = 10,width = 100, height = 30)
        self.search.place(x = 510, y = 10, width = 200 ,height = 30)
        self.searchbar.place(x = 710, y = 10,width = 300,height = 30)       
        
        #view cart
        self.view = Button(self.f_search,text = 'VIEW CART',fg = 'white',bg = 'blue3',activebackground = 'yellow',command = self.viewcart)
        self.view.place(x = 1200,y = 10,width = 100, height = 30)
        
        #description
        self.cat = Label(self.f,text = "Category : "+self.data[0][0],fg = 'white',font = ('Sans serif',15),bg = 'blue4',justify = LEFT,anchor = W)
        self.tag = Label(self.f,text = "Price : Rs."+str(self.price),fg = 'white',font = ('sans serif',15),bg = 'blue4',justify = LEFT,anchor = W)
        self.cat.place(x = 305,y = 40, width = 300, height = 25)
        self.tag.place(x = 305,y = 70, width = 250,height = 25)
        if(self.quantity == 0.0):
            self.stock = Label(self.f,text = "Out of stock",fg = 'Red', font = ('Times new roman',15,'italic'),bg = 'blue4')
            self.stock.place(x = 255, y = 130,width = 250,height = 25)
        else:
            pass
        
        #Image
        self.tv = ImageTk.PhotoImage(Image.open("tv.png"),master = self.root)
        self.fridge = ImageTk.PhotoImage(Image.open("fridge.png"),master = self.root)
        self.washing = ImageTk.PhotoImage(Image.open("washing.png"),master = self.root)
        self.laptop = ImageTk.PhotoImage(Image.open("laptop.png"),master = self.root)
        if(self.data[0][0] == 'TV'):
            self.c1 = Button(self.f, image=self.tv, width=230, height=225)
            self.c1.place(x = 5,y = 10,width = 275,height = 225)
        elif(self.data[0][0] == 'Refrigerator'):
            self.c1 = Button(self.f, image=self.fridge, width=230, height=225)
            self.c1.place(x = 5,y = 10,width = 275,height = 225)
        elif(self.data[0][0] == 'Laptop'):
            self.c1 = Button(self.f, image=self.laptop, width=230, height=225)
            self.c1.place(x = 5,y = 10,width = 275,height = 225)
        elif(self.data[0][0] == 'Washing Machine'):
            self.c1 = Button(self.f, image=self.washing, width=230, height=225)
            self.c1.place(x = 5,y = 10,width = 275,height = 225)
            
        #add to cart buttons
        self.val = IntVar()
        self.number = Spinbox(self.f, from_= 1, to = 5,width = 10, fg = 'black',bg = 'white',textvariable = self.val, font = ('Times new roman',15))
        self.cart = Button(self.f, text = 'Add to cart',fg = 'white',font = ('sans serif',15),bg = 'blue3',command = self.cart)
        if(self.quantity != 0):
            self.cart.place(x = 650,y = 350,width = 150,height = 30)
            self.number.place(x = 810,y = 350,width = 40,height = 30)
            
        self.root.mainloop()
    
    #add to cart logic
    def cart(self):
        self.total = int(self.number.get())
        self.cursor.execute("Select quantity from cart where p_id = ?",(self.p_id,))
        self.cartquantity = self.cursor.fetchall()
        if(self.cartquantity == []):
            self.cartquantity.append((0,))
        if(self.quantity < self.total):
            warning = Label(self.f,text = 'Only '+str(self.quantity)+' pieces available',fg = 'red',bg = 'khaki',font = ('Times new roman',15,'italic'))
            warning.place(x = 600, y = 390, width = 300,height = 25)
            
        elif(self.quantity - self.cartquantity[0][0] < self.total):
            self.cart.config(state = DISABLED)
            warning = Label(self.f,text = 'Cannot add more, only '+str(self.quantity)+' pieces in stock',fg = 'red',bg = 'khaki',font = ('Times new roman',15,'italic'))
            warning.place(x = 580, y = 390, width = 350,height = 25)
                
        elif(self.quantity - self.cartquantity[0][0] >= self.total):
            self.cart.config(state = ACTIVE)
            pid = self.p_id
            price = self.price
            address = self.userdata[0][3]
            try:
                self.cursor.execute("INSERT INTO cart VALUES(?,?,?,?)",(self.cust_id,self.p_id,price,self.total))
                
            except sqlite3.IntegrityError:
                self.cursor.execute("Update cart set quantity = quantity+? where p_id = ?",(self.total,self.p_id))
                
            finally:
                self.connection.commit()
            
    #go back
    def back(self):
        self.root.destroy()
        import main_page
        m = main_page.MainPage(self.cust_id)
        
    def search(self):
        search_ = self.searchbar.get()
        self.cursor.execute("SELECT * from Product where brand like ? or product_name like ? or category like ?",('%{}%'.format(search_),'%{}%'.format(search_),'%{}%'.format(search_)))
        self.connection.commit()
        s_result = self.cursor.fetchall()
        self.root.destroy()
        import search_result
        s = search_result.search_(s_result,self.cust_id,self.p_id)
    
    #go to cart page 
    def viewcart(self):
        self.root.destroy()
        import cart
        c = cart.Cart(self.cust_id,self.p_id)
    


        

        
        
