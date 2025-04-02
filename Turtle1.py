import turtle

turtle.Screen()
t = turtle.Pen()

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

print('The position is: ',t.pos())
print('Where are you towards North: ',t.towards(0,90))
print('The turtle x coordinate is: ',t.xcor())
print ('The turtle y coordinate is: ',t.ycor())
print('Turtle current heading: ',t.heading())
print('Turtle is away by: ',t.distance(200,0))




turtle.done()
