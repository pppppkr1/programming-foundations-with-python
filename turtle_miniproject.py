import turtle

def triangle(turtle, number, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(0,2):
        turtle.forward(number)
        turtle.left(120)
    turtle.forward(number)
    turtle.left(60)
    turtle.end_fill()

def white_triangles(t):
    t.forward(50)
    t.left(60)
    triangle(t, 50, "white")

    t.forward(50)
    t.left(60)
    triangle(t, 100, "white")

    t.forward(50)
    t.left(60)
    triangle(t, 50, "white")

    t.left(60)
    t.forward(50)
    t.left(60)
    t.forward(100)
    t.left(60)
    triangle(t, 50, "white")

    t.left(60)
    t.forward(50)
    t.left(60)
    t.forward(150)
    t.left(120)

def draw_shape():

    window = turtle.Screen()
    window.bgcolor("white")
    
    gt = turtle.Turtle()
    gt.shape("turtle")
    gt.color("yellow")
    gt.speed(4)

    # big green triangle
    triangle(gt, 400, "green")

    # setting direction for 1st
    gt.left(60)
    gt.forward(200)

    # 1st white triangle
    gt.left(60)
    triangle(gt, 200, "white")

    # smaller white triangles
    white_triangles(gt)

    gt.backward(200)
    white_triangles(gt)

    gt.left(60)
    gt.forward(200)
    gt.right(60)
    white_triangles(gt)

    window.exitonclick()

draw_shape()
            
