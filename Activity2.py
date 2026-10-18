from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("400x300")
root.title("main")
root.config(bg = "light blue")

img = Image.open("app_img.jpg")
img = img.resize((300, 300))
img1 = ImageTk.PhotoImage(img)

l1 = Label(root, text = "Hello", image = img1)
l1.place(x = 180, y = 20)


