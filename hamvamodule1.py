import turtle
t = turtle.Turtle()
def hcn(chieudai,chieurong):
    t.seth(90)
    for i in range(2):
        t.forward(chieudai)
        t.left(90)
        t.forward(chieurong)
        t.left(90)
def home(truchoanh, tructung):
    x = 1
    while x < 4:
        t.penup()
        t.goto(truchoanh,tructung)
        t.pendown()
        t.fillcolor("red")
        t.begin_fill()
        hcn(80,50)
        t.end_fill()
        x += 1
        truchoanh += 50 
def win(th, tt):
    y = 1
    while y < 4:
        t.penup()
        t.goto(th,tt)
        t.pendown()
        t.fillcolor("yellow")
        t.begin_fill()
        hcn(40,20)
        t.end_fill()
        y += 1
        th += 50 
home(-200,-200)
win (-220,-200)
home(-200,-110)
win(-220,-110)