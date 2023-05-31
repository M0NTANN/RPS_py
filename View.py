from tkinter import *


root = Tk()
root.title('My App') #заголовок
root.geometry("600x400")
lbl1 = Label(root, text='Привет')
lbl1.grid(column=0, row=0)
lbl1.pack()
root.mainloop()