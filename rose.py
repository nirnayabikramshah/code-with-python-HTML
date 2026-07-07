import turtle as t

screen =t.Screen()
screen.bgcolor("Yellow")  
t.color("Red")      
for i in range(150):

    t.forward(i * 1.2)
    t.left(58)          
    t.width(i / 50 + 1)

t.done()
