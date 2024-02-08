from turtle import Turtle


def Instructions():
    
    turtle=Turtle()
    
    turtle.penup()
    
    turtle.hideturtle()
    
    turtle.goto(-100, 250)   
    
    turtle.write("Input 'exit' to finish the game \nautomatically, a file will be generated with the unguessed USA states.", align='center', font=('Arial', 10, 'bold'))  
        

    