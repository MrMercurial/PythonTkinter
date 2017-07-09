#coding:utf-8
import sys
from Tkinter import *

reload(sys)
sys.setdefaultencoding('utf8')

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.quictButton=Button(self,text="quit",commond=self.quit())
        self.quictButton.grid()

app=Application()
app.master.title="test02"
app.mainloop()