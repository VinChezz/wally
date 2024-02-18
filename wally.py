from tkinter import *

root = Tk()
root.geometry('750x485')
root.title('Kyryl')
root.iconbitmap('coffee_hot_cafe_icon_261343.ico')

img = PhotoImage(file='Wally (3).png')
lb = Label(image=img)
lb.pack()
root.mainloop()