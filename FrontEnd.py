from tkinter import *
import BackEnd

window = Tk()
window.title("Book Library")
window.geometry('370x200+500+200')

# ========== Appearance ===========

# labels
lbl1 = Label(window, text="Title :")
lbl1.grid(row=1, column=0)

lbl2 = Label(window, text="Author :")
lbl2.grid(row=1, column=2)

lbl3 = Label(window, text="Year :")
lbl3.grid(row=2, column=0)

lbl4 = Label(window, text="ISBN :")
lbl4.grid(row=2, column=2)

# Entries
title_text = StringVar()
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=1, column=1)

author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=1, column=3)

year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=2, column=1)

isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=2, column=3)


# Function


def clear_list():
    list1.delete(0, END)


def fill_list(books):
    for book in books:
        list1.insert(END, book)


def viewall_func():
    clear_list()
    books = BackEnd.view()
    fill_list(books)


def search_func():
    clear_list()
    books = BackEnd.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    fill_list(books)


def add_func():
    try:
        BackEnd.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        viewall_func()
    except:
        return


def delete_func():
    BackEnd.delete(selectedItem[0])
    viewall_func()


def update_func():
    BackEnd.update(selectedItem[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    viewall_func()


# Buttons
btn1 = Button(window, text="View All", width=12, command=viewall_func)
btn1.grid(row=4, column=3)

btn2 = Button(window, text="Search Entry", width=12, command=search_func)
btn2.grid(row=5, column=3)

btn3 = Button(window, text="Add Entry", width=12, command=add_func)
btn3.grid(row=6, column=3)

btn4 = Button(window, text="Delete Selected", width=12, command=delete_func)
btn4.grid(row=7, column=3)

btn5 = Button(window, text="Update Selected", width=12, command=update_func)
btn5.grid(row=8, column=3)

btn6 = Button(window, text="Close", width=12, command=window.destroy)
btn6.grid(row=9, column=3)

# list box
list1 = Listbox(window, width=30, height=6)
list1.grid(row=3, column=0, rowspan=7, columnspan=2)

scb1 = Scrollbar(window)
scb1.grid(row=3, column=2, rowspan=7)
list1.configure(yscrollcommand=scb1.set)
scb1.configure(command=list1.yview)


def setrow_func(event):
    try:
        index = list1.curselection()[0]
        global selectedItem
        selectedItem = list1.get(index)
        title_text.set(selectedItem[1])
        author_text.set(selectedItem[2])
        year_text.set(selectedItem[3])
        isbn_text.set(selectedItem[4])
    except:
        return


list1.bind("<<ListboxSelect>>", setrow_func)
viewall_func()
window.mainloop()
