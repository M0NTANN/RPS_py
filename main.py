from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
# import SmallInteger
import xmlrpc.client

sum = 0

#with xmlrpc.client.ServerProxy("http://localhost:8000/") as SmallInteger:
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
messX = lambda: input("Enter x: ")
messY = lambda: input("Enter y: ")



root = Tk()
root.title('My App')
root.geometry("800x600")
T = Entry()
T.grid(row=0, column=0, padx=10, pady=10)
T2 = Entry()
T2.grid(row=0, column=1, padx=10, pady=10)
lb1 = Label(root, width=10).grid(row=0, column=3)
# sec = l["text"]
def summm(event):
    try:
        if T.get() and T2.get():
            r = proxy.sum(T.get(), T2.get())
            print(f"{r}")
            T.delete(0, END)
            T.insert(0, r)
        else:
            showinfo(title="Ошибка", message="Вы ввели не число")
    except:
        showinfo(title="Ошибка", message="Сервер отдыхает")


def subb(event):
    try:
        if T.get() and T2.get():
            r = proxy.sub(T.get(), T2.get())
            print(f"{r}")
            T.delete(0, END)
            T.insert(0, r)
        else:
            showinfo(title="Ошибка", message="Вы ввели не число")
    except:
        showinfo(title="Ошибка", message="Сервер отдыхает")

def mull(event):
    try:
        if T.get() and T2.get():
            r = proxy.mul(T.get(), T2.get())
            print(f"{r}")
            T.delete(0, END)
            T.insert(0, r)
        else:
            showinfo(title="Ошибка", message="Вы ввели не число")
    except:
        showinfo(title="Ошибка", message="Сервер отдыхает")

def divv(event):
    try:
        if T.get() and T2.get():
            r = proxy.div(T.get(), T2.get())
            print(f"{r}")
            T.delete(0, END)
            T.insert(0, r)
        else:
            showinfo(title="Ошибка", message="Вы ввели не число")
    except:
        showinfo(title="Ошибка", message="Сервер отдыхает")


btn1 = Button(text="+")
btn1.grid(row=1, column=0, padx=10, pady=10)
btn1.bind("<ButtonPress>", summm)

btn2 = Button(text="-")
btn2.grid(row=1, column=1, padx=10, pady=10)
btn2.bind("<ButtonPress>", subb)

btn3 = Button(text="/")
btn3.grid(row=2, column=0, padx=10, pady=10)
btn3.bind("<ButtonPress>", mull)

btn4 = Button(text="ост")
btn4.grid(row=2, column=1, padx=10, pady=10)
btn4.bind("<ButtonPress>", divv)

#btn5 = Button(text="=", width=10)
#btn5.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()



