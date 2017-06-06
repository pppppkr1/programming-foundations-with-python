import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)

    for num in range(0,18):
        for num in range(0,4):
            brad.forward(100)
            brad.right(90)
        brad.right(20)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()


draw_art()
    
