from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        
        self.penup()
        
        self.hideturtle()
        
        self.go_to_position()
        
        self.write_score_message()
    
        
        
    def go_to_position(self):
        self.goto(150, 210)    
        
    def write_score_message(self):
        self.write('SCORE', align='center', font=('Arial', 10, 'bold'))    
    
    def number_of_states(self, get_score):
        
        self.goto(150, 175)   
        self.clear()
        self.write(f'{get_score}/50', align='center', font=('Courier', 22, 'bold'))   
        
    def instructions(self):
        self.goto(-100, 250)   
        
        self.write("Input 'exit' to finish the game \nautomatically, a file will be generated with the unguessed USA states.", align='center', font=('Arial', 10, 'bold'))  
        

