# encoding=UTF-8
import Tkinter
import tkFont

def callback1(ev):
    label.config(text='lef button single click',bg='#F00')
def callback2(ev):
    label.config(text='middle button double click',bg='#0F0')
def callback3(ev):
    label.config(text='right button drag',bg='#00F')

top = Tkinter.Tk()
myFont = tkFont.Font(family='Verdana', size=30)
myCFont = tkFont.Font(family='Microsoft YaHei UI', size=30)
label = Tkinter.Label(top, text='display callback', bg='#FFF', font=myFont)
button = Tkinter.Button(top, text='click me', font=myCFont)
label.pack()
button.pack()
button.bind('<Button-1>',callback1)
button.bind('<Double-2>',callback2)
button.bind('<B3-Motion>',callback3)
top.minsize(400, 300)
top.mainloop()
