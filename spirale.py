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

penup()         # paceļ zīmuli
goto(0,0)              
pencolor('green')        
pendown()
setheading(90)
#fib=[1,1,2,3,5,8,13,21,34,55,89]
fib=[1,1]
i=2
while i<12:
    fib.append(fib[i-1]+fib[i-2])
    i+=1
for r in fib:
    circle(-r,90)

