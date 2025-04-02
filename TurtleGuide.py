import turtle

s = turtle.Screen()
s.bgcolor('green')
s.title("Python Guide")

t = turtle.Pen()

t.shapesize(10,5,1)
t.color("blue","red")

t.shape("arrow")
t.speed(2)

t.begin_fill()
t.fd(300)
t.lt(120)
t.stamp()
t.fd(300)
t.lt(120)
t.stamp()
t.fd(300)
t.lt(120)
t.end_fill()

turtle.done()
