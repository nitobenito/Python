# jāimportē turtle bibliotēka
import turtle             
my_window = turtle.Screen()     #jāizveido atsevišks turtle grafikas logs
my_window.bgcolor("blue")       # logu var nokrāsot
my_pen = turtle.Turtle()        # var radīt savu bruņurupuci
my_pen.shape("turtle")          # un tam noformēt bildi 
my_pen.pensize(20)              # un tam noformēt līnijas resnumu
my_pen.forward(40)              # un to sūtīt uz priekšu 40 punktus
my_pen.left(90)                 # un likt tam pagriezties par 90 grādiem
my_pen.forward(40)              # un tad atkal uz priekšu
my_pen.color("white")           # brunurupuci var nokrāsot
turtle.left(90)                 # var izmantot arī standtarta bruņurupuci   
turtle.color("green")           # nokrāsot zaļu
turtle.backward(40)             # un sūtīt to atpakaļgaitā

