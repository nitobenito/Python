from tkinter import *
# importē gatavu krāsu dialoglogu
from tkinter.colorchooser import *
# izmantosim globālos mainīgos
global krasa, krasa1, krasa2
krasa="#00ff00"
krasa1="#ffffff"
krasa2="#000000"

# funkcija nosaka peles atrašanās vietu un tur zīmē aplīti
def kustiba(notikums):
    x=notikums.x
    y=notikums.y
    kanva.create_oval(x, y, x+10, y+10, fill=krasa)

# funkcija mainīgajam krasa piešķir dialoglogā izvēleto krāsu    
def mainaKrasu():
    global krasa
    krasa = askcolor()[1]
    
# reakcija uz peles labo pogu - pogas un kanvas krāsas samainās
def mainaFonu(notikums):
    poga=notikums.widget
    global krasa1, krasa2
    temp=krasa1
    krasa1=krasa2
    krasa2=temp
    poga["foreground"]=krasa1
    poga["background"]=krasa2
    kanva["background"]=krasa1

# programmas logs    
logs = Tk()
logs.minsize(400,400)
kanva = Canvas(logs, bg=krasa1, height=300, width=300)
kanva.bind('<Motion>', kustiba) # kanvai pieliek reakciju uz peles kustību
kanva.pack(side="bottom")
# pogai pieliek 2 reakcijas divos dažādos veidos
# reakcija uz standart klikšķi (kreiso)
krasasPoga = Button(logs, bg=krasa2, fg=krasa1, text="Krāsa", width=6 ,command=mainaKrasu)
krasasPoga.place(x=20, y=20)
# reakcija uz labo klikšķi
krasasPoga.bind("<Button-3>", mainaFonu)
logs.mainloop()

#http://www.python-course.eu/tkinter_events_binds.php
#http://www.tutorialspoint.com/python/tk_canvas.htm
