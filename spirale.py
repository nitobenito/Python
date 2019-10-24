from turtle import *
speed(100)
pencolor('red')
pensize(3)
circle(100)     # uzzīmē 360 grādu loku ar radisuu 100
circle(50,180)  # uzzīmē 180 grādu loku ar radisu 50
circle(-50,180) # mīnus - zīmēt pretēji pulksteņa rādītājam
penup()         # paceļ zīmuli
goto(-250,-100) # aiziet uz citu vietu nezīmējot
pendown()       # nolaiž zīmuli
setheading(90)  # pagriežas par 90 grādiem
x=-50           # ciklā zīmē 5 puslokus
for i in range(5):
    circle(x,180)  
    x=-x 
