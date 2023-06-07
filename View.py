from tkinter import *
#import main

firsr = 0
lastD = ""

def summm(fir, sec):
    print(sec)



def view():
    root = Tk()
    root.title('My App')
    root.geometry("800x600")
    T = Text(root, height = 1, width = 6).grid(row=0, column=0, padx=10, pady=10)
    T2 = Text(root, height = 1, width = 6).grid(row=0, column=1, padx=10, pady=10)
    lb1 = Label(root, width=10).grid(row=0, column=3)
    #sec = l["text"]
    btn1 = Button(text="+", command=summm(T, T2)).grid(row=1, column=0, padx=10, pady=10)
    btn2 = Button(text="-").grid(row=1, column=1, padx=10, pady=10)
    btn3 = Button(text="/").grid(row=2, column=0, padx=10, pady=10)
    btn4 = Button(text="ост").grid(row=2, column=1, padx=10, pady=10)
    btn5 = Button(text="=", width=10).grid(row=3, column=0, padx=10, pady=10)


root.mainloop()




