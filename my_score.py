from turtle import Turtle

class Score():
    def __init__(self):
        
        self.turtle=Turtle()
        self.turtle.penup()
        
        self.turtle.hideturtle()
        
        self.go_to_position()
        
        self.write_score_message()
        
    def go_to_position(self):
        self.turtle.goto(150, 210)    
        
    def write_score_message(self):
        self.turtle.write('SCORE', align='center', font=('Arial', 10, 'bold'))    
    
    def number_of_states(self):
        self.turtle=Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.goto(150, 110)   
        self.write('0/50', align='center', font=('Arial', 16, 'bold'))   