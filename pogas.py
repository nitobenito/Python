from tkinter import *
from tkinter import messagebox
from random import randint
global pn
pn=3
def pogasDarbs(notikums):
    # poga tagad ir tieši tā poga uz kuras uzklikškināts
    poga = notikums.widget
    n=poga.cget("text")
    skaitli.append(n)
    messagebox.showinfo("Logs",poga.cget("text"))
   
logs=Tk()
pogas=[]
skaitli=[]
pskaitli=[]
for pogasNr in range(pn):
    skaitlis=randint(1,300)
    pskaitli.append(skaitlis)
    jaunaPoga=Button(logs, text=skaitlis, height = 1, width = 3)
    jaunaPoga.place(x=pogasNr*40,y=5)
    jaunaPoga.bind('<Button-1>',pogasDarbs)
    pogas.append(jaunaPoga)
mainloop()
