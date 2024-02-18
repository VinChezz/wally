from tkinter import *

root = Tk()
root.geometry('750x650')
root.title('Kyryl')
root.iconbitmap('coffee_hot_cafe_icon_261343.ico')

text = Label(text='gamma editor', font='Verdana 20')
text.pack()
img = PhotoImage(file='Wally (3).png')
lb = Label(image=img)
lb.pack()

def scale(val):
    img['gamma']=val
scale=Scale(from_=1, to=10, length=700, orient=HORIZONTAL, command=scale)
scale.pack()
root.mainloop()