import sys
from tkinter import *
root = Tk()
# First command line arg is image path
img = PhotoImage(file='./test.png')
red = 255
green = 0
blue = 0
x = 0
y = 10
# uzliek zilus punktus vertikāli, sarkanus horizontāli
for x in range(0,100):
    img.put("#%02x%02x%02x" % (red, green, blue), (y, x))
    img.put("#0000ff", (x, y))
# nosaka punkta (50,50) krāsu
top_left_pixel = img.get(50, 50)  
print(top_left_pixel)
# attēlu ieleik Label elementā
img_label = Label(root, image=img)
img_label.pack()
root.mainloop()

#http://www.devdungeon.com/content/gui-programming-python#popups
#http://epydoc.sourceforge.net/stdlib/Tkinter.PhotoImage-class.html
