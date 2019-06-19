# encoding=UTF-8
import Tkinter
import tkFont


def callback1(ev):
    message1.config(text='move to[%d,%d]' % (ev.x, ev.y), bg='#0F0')
    label.config(text='label move to[%d,%d]' % (ev.x, ev.y), bg='#00F')


top = Tkinter.Tk()
myFont = tkFont.Font(family='Verdana', size=30)
myCFont = tkFont.Font(family='Microsoft YaHei UI', size=30)
message1 = Tkinter.Message(top, text="=====display coordinate=====", font=myCFont, bg='#C0FFEE')
label = Tkinter.Message(top, text="=====display coordinate=====", font=myCFont, bg='#C0FF00')
label.pack()
message1.pack()
message1.bind('<Motion>', callback1)
label.bind('<Motion>',callback1)
top.minsize(600, 600)
top.mainloop()
