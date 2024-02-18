from tkinter import *

root = Tk()
root.geometry('750x555')
root.title('Kyryl')
root.iconbitmap('coffee_hot_cafe_icon_261343.ico')

img = PhotoImage(file='Wally (3).png')
lb = Label(image=img)
lb.pack()

def set_gamma(val):
    img['gamma']=val
scale=Scale(from_=1, to=10, length=700, orient=HORIZONTAL, command=set_gamma)
scale.pack()
root.mainloop()