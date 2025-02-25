from tkinter import *
from tkinter import messagebox

class Book:
    def __init__(self, name, author, page, price, total):
        self.__name = name
        self.__author = author
        self.__page = page
        self.__price = price
        self.__total = total

    def GetName(self):
        return self.__name

    def GetAuthor(self):
        return self.__author

    def GetPage(self):
        return self.__page

    def GetPrice(self):
        return self.__price

    def GetTotalcount(self):
        return self.__total

    def ReduceStock(self, count):
        if self.__total >= count:
            self.__total -= count
            return True
        return False

    def GetInfo(self):
        return (f"Name: {self.__name}, Author: {self.__author}, Page: {self.__page}, Price: {self.__price}, Total count: {self.__total}")

    def GetSum(self, count):
        #self.__total = self.__total - count
        sum = self.__price * count
        return sum

    def GetTotal(self):
        return self.__total

    def SetTotal(self, new_total):
        self.__total = new_total



book1 = Book("The mystery of the blue train", "Agatha Christie", "287", 6.99, 27)
book2 = Book("After the funeral", "Agatha Christie", "287", 6.99, 28)
book3 = Book("Curtain: Poirot's last case", "Agatha Christie", "231", 9.99, 27)
book4 = Book("Evil under the sun", "Agatha Christie", "255", 5.99, 28)
book5 = Book("Dumb witness", "Agatha Christie", "167", 5.99, 25)
book6 = Book("Appointment with death", "Agatha Christie", "207", 5.49, 23)
book7 = Book("Poirot investigates", "Agatha Christie", "431", 9.99, 27)
book8 = Book("Hallowe'en party", "Agatha Christie", "256", 9.99, 23)
book9 = Book("The Secret of Chimneys", "Agatha Christie", "310", 16.66, 30)
book10 = Book("The Sittaford Mystery", "Agatha Christie", "308", 13.68, 22)
book11 = Book("Death in the Clouds", "Agatha Christie", "304", 13.68, 26)
book12 = Book("The kite runner", "Khaled Hosseini", "447", 9.99, 29)
book13 = Book("A thousand splendid suns", "Khaled Hosseini", "455", 9.99, 21)
book14 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", "223", 15.36, 26)
book15 = Book("Harry Potter and the Chamber of Secrets", "J. K. Rowling", "251", 15.36, 24)
book16 = Book("Harry Potter and the Prisoner of Azkaban", "J. K. Rowling", "317", 15.36, 24)
book17 = Book("Harry Potter and the Goblet of Fire", "J. K. Rowling", "636", 17.28, 25)
book18 = Book("Harry Potter and the Order of the Phoenix", "J. K. Rowling", "766", 17.38, 25)
book19 = Book("Harry Potter and the Half-Blood Prince", "J. K. Rowling", "607", 17.28, 25)
book20 = Book("Harry Potter and the Deathly Hallows", "J. K. Rowling", "607", 17.28, 24)


# Kitab məlumatlarını fayla yazmaq
def log_book_operation(operation, book, count):
    with open("log.txt", "a") as file:
        file.write(f"{operation}: {book.GetName()} - Count: {count}, Price: {book.GetPrice()}, Total: {book.GetSum(count)}\n")

# Kitab əlavə edildikdə log faylına yazılacaq
def Add():
    name_book = entryname.get().strip()
    number_book = entrycount.get().strip()

    if not number_book.isdigit() or int(number_book) <= 0:
        messagebox.showwarning("Xəta", "Kitab sayı düzgün daxil edilməlidir! (Müsbət tam ədəd olmalıdır)")
        return

    number_book = int(number_book)
    for book in ls:
        if book.GetName().lower() == name_book.lower():
            if book.ReduceStock(number_book):
                # Kitab məlumatlarını fayla yaz
                log_book_operation("Added", book, number_book)

                lblist.insert(END, book.GetInfo())
                lb_name.insert(END, book.GetName())
                lb_price.insert(END, book.GetPrice())
                lb_count.insert(END, number_book)
                lb_sum.insert(END, book.GetSum(number_book))
                lstotal.append(book.GetSum(number_book))

                entryname.delete(0, END)
                entrycount.delete(0, END)
            else:
                messagebox.showwarning("Xəta", "Əlavə etmək istədiyiniz kitab sayısı mövcud stokdan çoxdur!")
            break

# Kitab silindikdə log faylına yazılacaq
def Cancel():
    selected_index = lblist.curselection()
    if selected_index:
        index = selected_index[0]
        name = lb_name.get(index)
        count_to_remove = int(lb_count.get(index))

        for book in ls:
            if book.GetName().lower() == name.lower():
                current_total = book.GetTotal()
                book.SetTotal(current_total + count_to_remove)

                # Kitab silinməsi əməliyyatını log faylında qeyd et
                log_book_operation("Removed", book, count_to_remove)

                break

        lblist.delete(index)
        lb_name.delete(index)
        lb_price.delete(index)
        lb_count.delete(index)
        lb_sum.delete(index)

        del lstotal[index]



def Next1():
    frame.place_forget()
    frame2.place(x=0, y=0)

def Back1():
    frame2.place_forget()
    frame.place(x=0, y=0)

def Next2():
    frame2.place_forget()
    frame3.place(x=0, y=0)

    lb_total.insert(END, sum(lstotal))

def Back2():
    frame3.place_forget()
    frame2.place(x=0, y=0)

    lb_total.delete(END, (0))

root = Tk()
root.title("Checkout")
root.geometry("850x850")

ls = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13, book14, book15, book16, book17, book18, book19, book20]

def log_initial_books_to_file():
    # Baza üzərindən mövcud kitabları alırıq
    for book in ls:  # ls bazadakı bütün kitabları saxlayan siyahıdır
        with open("log.txt", "a") as file:
            file.write(f"Initial: {book.GetName()} - Count: {book.GetTotalcount()}, Price: {book.GetPrice()}, Total: {book.GetTotal() * book.GetTotalcount()}\n")

# Proqram başladığında bazadakı bütün kitabları fayla yazırıq
log_initial_books_to_file()

lstotal = []


frame = Frame(bg="white",width=850,height=850)
frame.place(x=0,y=0)

lb = Listbox(frame,bg="#F5ECBA", width=60, height=20, fg="#5a572a", font=("Times New Roman", 15))
lb.insert(END, book1.GetName())
lb.insert(END, book2.GetName())
lb.insert(END, book3.GetName())
lb.insert(END, book4.GetName())
lb.insert(END, book5.GetName())
lb.insert(END, book6.GetName())
lb.insert(END, book7.GetName())
lb.insert(END, book8.GetName())
lb.insert(END, book9.GetName())
lb.insert(END, book10.GetName())
lb.insert(END, book11.GetName())
lb.insert(END, book12.GetName())
lb.insert(END, book13.GetName())
lb.insert(END, book14.GetName())
lb.insert(END, book15.GetName())
lb.insert(END, book16.GetName())
lb.insert(END, book17.GetName())
lb.insert(END, book18.GetName())
lb.insert(END, book19.GetName())
lb.insert(END, book20.GetName())
lb.place(x=0,y=250)

photo1 = PhotoImage(file="images (1).png")
lblbookphoto = Label(frame, image=photo1, width=850, height=200)
lblbookphoto.place(x=0, y=0)


lbl = Label(frame, text="List of books", width=20, background="#acc18a", foreground="white", font=("Times New Roman",15))
lbl.place(x=0,y=215)

bookname = Label(frame, text="The name of the book!", width=20, background="#7a904d", foreground="white", font=("Times New Roman",12))
bookname.place(x=0,y=755)

bookcount = Label(frame, text="Count of the book!", width=20, background="#7a904d",foreground="white", font=("Times New Roman",12))
bookcount.place(x=0,y=790)

entryname = Entry(frame, width=30, font=("Arial", 10))
entryname.place(x=215, y=755)


entrycount = Entry(frame, width=5, font=("Arial", 10))
entrycount.place(x=215, y=790)



btnadd = Button(frame,text="Add", width=9, bg="#858F1F", fg="white",  command=Add)
btnadd.place(x=265, y=790)


btnnext1 = Button(frame, text="Next", width=10, bg="#ede29b", fg="#5a572a", command=Next1)
btnnext1.place(x=700, y=700)

#Frame2==========================================================================


frame2 = Frame(bg="white",width=850,height=850)


photo2 = PhotoImage(file="images.png")
lblbookphoto2 = Label(frame2, image=photo2, width=850, height=200)
lblbookphoto2.place(x=0, y=0)

lblist = Listbox(frame2,bg="#F5ECBA", width=86, height=20, fg="#5a572a", font=("Times New Roman", 13))
lblist.place(x=0,y=250)

lbl2 = Label(frame2, text="List of selected books", width=20, background="#acc18a", foreground="white", font=("Times New Roman",15))
lbl2.place(x=0,y=215)

# entrycount2 = Entry(frame2, width=5, font=("Arial", 10))
# entrycount2.place(x=435, y=790)

btnback1 = Button(frame2, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back1)
btnback1.place(x=25, y=750)


btncancel = Button(frame2,text="Cancel", width=9, bg="#858F1F", fg="white",  command=Cancel)
btncancel.place(x=420, y=750)

btnnext2 = Button(frame2, text="Next", width=10, bg="#ede29b", fg="#5a572a", command=Next2)
btnnext2.place(x=700, y=750)


#Frame3=============================================================================


frame3 = Frame(bg="white",width=850,height=850)

lbl_3 = Label(frame3, text="Check!",width=20, height=2, background="#acc18a", foreground="white", font=("Times New Roman",25))
lbl_3.place(x=250,y=0)

lbl_name = Label(frame3, text="Book's name", width=20, background="#acc18a", foreground="white", font=("Times New Roman",15))
lbl_name.place(x=0, y=110)

lbl_price = Label(frame3, text="Price", width=5, background="#acc18a", foreground="white", font=("Times New Roman",15))
lbl_price.place(x=300, y=110)

lbl_count = Label(frame3, text="Count", width=5, background="#acc18a", foreground="white", font=("Times New Roman",15))
lbl_count.place(x=400, y=110)

lbl_sum = Label(frame3, text="Sum", width=5, background="#acc18a", foreground="white", font=("Times New Roman",15))
lbl_sum.place(x=500, y=110)

lb_name = Listbox(frame3,bg="#F5ECBA", width=86, height=20, fg="#5a572a", font=("Times New Roman", 13))
lb_name.place(x=0,y=150)

lb_price = Listbox(frame3,bg="#F5ECBA", width=86, height=20, fg="#5a572a", font=("Times New Roman", 13))
lb_price.place(x=300,y=150)

lb_count = Listbox(frame3,bg="#F5ECBA", width=86, height=20, fg="#5a572a", font=("Times New Roman", 13))
lb_count.place(x=400,y=150)

lb_sum = Listbox(frame3,bg="#F5ECBA", width=86, height=20, fg="#5a572a", font=("Times New Roman", 13))
lb_sum.place(x=500,y=150)


lb_total = Listbox(frame3,bg="#F5ECBA", width=8, height=2, fg="#5a572a", font=("Times New Roman", 13))
lb_total.place(x=365, y=680)

lbl_total = Label(frame3, text="Total", width=15, background="#acc18a", foreground="white", font=("Times New Roman",20))
lbl_total.place(x=290, y=620)

btnback2 = Button(frame3, text="Back", width=10, bg="#ede29b", fg="#5a572a", command=Back2)
btnback2.place(x=25, y=750)



root.mainloop()
