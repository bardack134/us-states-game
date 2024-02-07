from turtle import Turtle

class My_turtle(Turtle):
    def __init__(self, state_index_x, state_index_y, state_name):
        super().__init__()
        self.penup()
        
        self.hideturtle()
        self.cor_x=state_index_x
        self.cor_y=state_index_y
        
        self.state_name=state_name
        
        
    def go_to_position(self):
        self.goto(self.cor_x, self.cor_y)    
        
    def write_state_name(self):
        self.write(self.state_name, align='center', font=('Arial', 10, 'bold'))