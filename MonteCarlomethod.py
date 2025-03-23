import turtle as t; import random as rn; import math as m
t.bgcolor("black"); t.speed(0); t.color("white"); t.penup(); t.ht()
t.goto(150, -150); t.pendown()
t.goto(150, 150); t.goto(-150, 150); t.goto(-150, -150); t.goto(150, -150)
tw = t.Turtle()
tw.penup(); tw.ht(); tw.goto(-150, 200); tw.color("white")
tw.write("hello!", font = ("arial", 15, "bold"))
t.color("red"); i = 0
while True:
    x = 300 * m.cos(i) - 150; y = 300 * m.sin(i) - 150
    t.goto(x, y)
    i += 0.01
    if -150 <= x <= -149 <= y <= 150: break
cnt_in = 0; cnt_total = 0; pi = 0
while True:
    t.penup()
    tw.write(pi, font = ("arial", 15, "bold"))
    x = rn.randint(-150, 150); y = rn.randint(-150, 150)
    cnt_total += 1
    if m.sqrt((x + 150) ** 2 + (y + 150) ** 2) <= 300:
        cnt_in += 1
        t.goto(x, y); t.pendown(); t.color("green"); t.circle(1)
    else:
        t.goto(x, y); t.pendown(); t.color("yellow"); t.circle(1)
    pi = 4 * (cnt_in / cnt_total)
    tw.clear()


