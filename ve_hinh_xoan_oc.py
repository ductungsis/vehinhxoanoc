import turtle

d = 200
buoc_di = 0
# print(turtle.distance())

turtle.speed(10)

while (turtle.distance(0, 0) <d):
    buoc_di += 0.1
    turtle.forward(buoc_di)
    turtle.left(20)
    
turtle.done()    