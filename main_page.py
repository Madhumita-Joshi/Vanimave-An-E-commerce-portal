

from tkinter import *
from PIL import Image, ImageTk
import sqlite3


class MainPage:

    def __init__(self, cust_id):
        # Tkinter object initialisation
        self.t1 = Tk()
        self.t1.title("Vanimave Electronic Store")
        self.t1.geometry("1880x1080")
        self.t1.config(bg='Blue4')
        self.t1_top = Frame(self.t1, bg='blue4', width=1400, height=200,relief = SUNKEN,bd = 2)
        self.t1_top.pack()
        self.t1_bottom = Frame(self.t1, bg="blue4")
        self.t1_bottom.pack()

        # Data base initialisation
        self.connection = sqlite3.connect('Product.db')
        self.cursor = self.connection.cursor()

        self.cust_id = (cust_id,)
        # getting user data from database
        self.cursor.execute("SELECT username FROM user where cust_id = ?", self.cust_id)
        self.cid = self.cursor.fetchall()
        self.cust_id = cust_id
        self.connection.commit()

        # Top Frame(Search label and entry box for searching)
        self.backlg= Button(self.t1_top,text='Back',width=10,bg='blue4',fg='white',command = self.backlg)
        self.backlg.place(x=10,y=10)
        self.viewct= Button(self.t1_top,text='View Cart',width=10,bg='blue4',fg='white',command = lambda: self.viewcart(0))
        self.viewct.place(x = 1240, y = 10)
        self.greet = Label(self.t1_top, text="Welcome to Vanimave Electronic Store", bg='blue4', fg='white', pady=20)
        self.greet.config(font=("Sans serif", 30, 'bold'))

        #user name
        self.user = Label(self.t1_top, text="User :{}".format(self.cid[0][0]), font=('Times', 17), fg='yellow',bg='blue4')
        self.l1 = Label(self.t1_top, text="Search", font=('ariel', 14, 'bold'), bg='blue4', fg='white')
        self.e1 = Entry(self.t1_top, width=70, bd=2)
        self.b1 = Button(self.t1_top, command=lambda: self.display(self.e1.get()), width=15, text="Search")

        self.greet.place(x=380, y=50)
        self.user.place(x=1200, y=85)
        self.e1.place(x=550, y=150, height=25)
        self.l1.place(x=450, y=150)
        self.b1.place(x=1500, y=150)

        # Bottom Frame
        self.tv = ImageTk.PhotoImage(Image.open("tv.png"), master=self.t1)
        self.fridge = ImageTk.PhotoImage(Image.open("fridge.png"), master=self.t1)
        self.washing = ImageTk.PhotoImage(Image.open("washing.png"), master=self.t1)
        self.laptop = ImageTk.PhotoImage(Image.open("laptop.png"), master=self.t1)

        self.c1 = Button(self.t1_bottom, image=self.tv, width=230, height=225, command=lambda: self.display("TV"))
        self.c2 = Button(self.t1_bottom, image=self.fridge, width=230, height=225,
                         command=lambda: self.display("Refrigerator"))
        self.c3 = Button(self.t1_bottom, image=self.washing, width=230, height=225,
                         command=lambda: self.display("Washing Machine"))
        self.c4 = Button(self.t1_bottom, image=self.laptop, width=230, height=225,
                         command=lambda: self.display("Laptop"))
        self.c11 = Label(self.t1_bottom, text="TV", bg='blue4', fg='white',font = 15,anchor = N)
        self.c22 = Label(self.t1_bottom, text="Refrigerator", bg='Blue4', fg='white',font = 15)
        self.c33 = Label(self.t1_bottom, text="Washing Machine", bg='blue4', fg='white',font = 15)
        self.c44 = Label(self.t1_bottom, text="Laptop", bg='blue4', fg='white',font = 15)

        self.c5 = Button(self.t1_bottom,text="Sort by price",width=10,command=self.sort)
        self.c5.grid(row=2,column=4,sticky=NE)
        self.c55 = Label(self.t1_bottom, text="Low to High",width=10,bg='blue4', fg='white')
        self.c55.grid(row=2, column=5, sticky=NE)

        self.c1.grid(row=0, column=0,pady = 50)
        self.c11.grid(row=1, column=0)
        self.c2.grid(row=0, column=1)
        self.c22.grid(row=1, column=1)

        self.c3.grid(row=0, column=2)
        self.c33.grid(row=1, column=2)

        self.c4.grid(row=0, column=3)
        self.c44.grid(row=1, column=3)

        self.t1.mainloop()
        
    def backlg(self):
        self.t1.destroy()
        import Login
        
    def sort(self):
        self.cursor.execute("Select * from Product order by price")
        self.prod_data = self.cursor.fetchall()
        self.ppage = Tk()
        self.ppage.config(bg="blue4")
        self.ppage.title("Product List")
        self.ppage.geometry("800x800")
        self.r = 0
        self.c = 0
        self.title_prod = Label(self.ppage, text="Product Name", width=12, bg="blue4",fg = 'khaki')
        self.title_prod.config(font = ('comic sans',20,'bold'))
        self.title_prod.grid(row=self.r, column=self.c)
        self.title_price = Label(self.ppage, text="Price", width=10, bg="blue4",fg = 'khaki')
        self.title_price.config(font = ('comic sans',20,'bold'))
        self.title_price.grid(row=self.r, column=self.c + 1)
        self.r += 1
        self.i = 0
        for row in self.prod_data:
            buttons_view = []
            buttons_cart = []
            self.lab1 = Label(self.ppage, text=row[1] + ' ' + row[2]+' '+row[0], padx=10,pady=15, bg="blue4",fg = 'white',font = ('Sans serif',15)).grid(row=self.r,
                                                                                                  column=self.c)
            self.lab2 = Label(self.ppage, text='Rs ' + str(row[5]), padx=10,pady=15, bg="blue4",fg = 'white',font = ('Sans serif',15)).grid(row=self.r,
                                                                                                column=self.c + 1)
            self.but = Button(self.ppage, text="View Product", width=10, command=lambda row=row: self.viewprod(row))
            self.but.grid(row=self.r, column=self.c + 2, padx=10)
            #self.but = Button(self.ppage, text="Add to cart", width=10, command=lambda row=row: self.cart(row))
            #self.but.grid(row=self.r, column=self.c + 3, padx=10)
            buttons_view.append(row)
            buttons_cart.append(row)
            self.r += 1
            self.i = self.i + 1
            # self.c+=1

    def display(self, entry):
        self.t1.destroy()
        self.connection = sqlite3.connect('Product.db')
        self.cursor = self.connection.cursor()
        self.entry = entry
        self.cursor.execute("Select * from Product where Category like ? or "
                            "Brand like ? or product_name like ?",
                            ('%' + self.entry + '%', '%' + self.entry + '%', '%' + self.entry + '%'))
        self.prod_data = self.cursor.fetchall()
        self.ppage = Tk()
        self.ppage.config(bg="blue4")
        self.ppage.title("Product List")
        self.ppage.geometry("1920x1080")
        self.viewcrt = Button(self.ppage,text = 'View Cart',width = 10,bg = 'blue4',fg = 'white',command = lambda: self.viewcart(1))
        self.viewcrt.grid(row = 0,column = 5)
        self.back = Button(self.ppage,text = 'Back',width = 10,bg = 'blue4',fg = 'white',command = self.back)
        self.back.grid(row = 0,column = 0)
        self.r = 1
        self.c = 1
        self.title_prod = Label(self.ppage, text="Product Name", width=12, bg="blue4",fg = 'khaki')
        self.title_prod.config(font = ('comic sans',20,'bold'))
        self.title_prod.grid(row=self.r, column=self.c)
        self.title_price = Label(self.ppage, text="Price", width=10, bg="blue4",fg = 'khaki')
        self.title_price.config(font = ('comic sans',20,'bold'))
        self.title_price.grid(row=self.r, column=self.c + 1)
        self.r += 1
        self.i = 0
        for row in self.prod_data:
            buttons_view = []
            buttons_cart = []
            self.lab1 = Label(self.ppage, text=row[1] + ' ' + row[2]+' '+row[0], padx=10,pady=15, bg="blue4",fg = 'white',font = ('Sans serif',15)).grid(row=self.r,
                                                                                                  column=self.c)
            self.lab2 = Label(self.ppage, text='Rs ' + str(row[5]), padx=10,pady=15, bg="blue4",fg = 'white',font = ('Sans serif',15)).grid(row=self.r,
                                                                                                column=self.c + 1)
            self.but = Button(self.ppage, text="View Product", width=10, command=lambda row=row: self.viewprod(row))
            self.but.grid(row=self.r, column=self.c + 2, padx=10)
            #self.but = Button(self.ppage, text="Add to cart", width=10, command=lambda row=row: self.cart(row))
            #self.but.grid(row=self.r, column=self.c + 3, padx=10)
            buttons_view.append(row)
            buttons_cart.append(row)
            self.r += 1
            self.i = self.i + 1
            # self.c+=1

    def viewprod(self, row):
        self.ppage.destroy()
        from sel_product import sel_product
        s = sel_product(row[4], self.cust_id)
        
    def back(self):
        self.ppage.destroy()
        import main_page
        main_page.MainPage(self.cust_id)
        
    def viewcart(self,flag):
        mp = 'mp'
        if(flag == 0):
            self.t1.destroy()
            import cart
            c = cart.Cart(self.cust_id,mp)
        elif(flag == 1):
            self.ppage.destroy()
            import cart
            c = cart.Cart(self.cust_id,mp)


