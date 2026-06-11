#Concrete Methon
#Abstract Method
from tkinter import *
root = Tk()
root.geometry("234x432")
root.title("Entry Widget Example")
ent = Entry(root, borderwidth=5, width=30, fg='white', bg='black')
ent.pack()
def click():
    x = ent.get()
    mylabel = Label(root, text="NIET WELCOMES " + x)
    mylabel.pack()
    ent.delete(0, END)
mybutton = Button(root, text='ENTER', command=click, width=20)
mybutton.pack()
root.mainloop()
