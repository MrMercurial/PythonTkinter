#coding:utf-8
import sys
from Tkinter import *

reload(sys)
sys.setdefaultencoding('utf8')

root=Tk()
root.title("ToDoList")
# frame=Frame(root,width=800,height=600).pack()
lable=Label(root,text="Hello World!")
lable1=Label(root,text="Please waite!",compound="left",bitmap="hourglass")
lable.pack()
lable1.pack()
e=StringVar()
entry=Entry(root,text="please enter your name",textvariable=e,show="*")
e.set("input your text here")
# entry['show']="a"
entry.pack()
# menue=Menu(frame)
# menue.add(Menubutton,"Start")

root.mainloop()