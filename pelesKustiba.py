from tkinter import *
def motion(event):
  xx=event.x
  yy=event.y
  uzraksts.place(x=xx,y=yy,width=200, height=100)
xx=50
yy=50
logs = Tk()
logs.geometry("300x300")
uzraksts = Label(logs, text = "START(IT)")
uzraksts.config(bg='lightgreen', font=('times', 20, 'italic'))
uzraksts.place(x=xx,y=yy,width=200, height=100)
uzraksts.bind('<Motion>',motion)
mainloop()
