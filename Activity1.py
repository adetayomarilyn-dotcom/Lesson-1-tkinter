from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = Label(top, text = "This is the top level")
    l2.pack()
    top.mainloop()
l = Label(root, text = "This is root window")
button = Button(root, text = "Click me to open an additional window", command= topwin)
l.pack()
button.pack()
root.mainloop()
