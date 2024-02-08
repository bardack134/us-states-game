from turtle import Screen
from my_score import Score

from writing_states import My_turtle

import pandas

#del archivo 50_states.csv  importamos los datos usando la libreria panda
usa_states=pandas.read_csv("usa_states.csv")

#guardamos los datos de la columna en una variable
states_column=usa_states["state"]

#convertimos la serie de la columna state en una lista iterable
states_list=states_column.to_list()

#convierto el dataframe en un diccionario para poder accerder a las cordenadas del estado
states_dic=usa_states.to_dict("records")

#NOTE: borrar los sgts comentarios
print(states_dic)
print(states_list)
print(states_list.index("Alaska"))
# print(states_list[1]["x"])

print(states_dic[1]['x'])

#creando objeto de la clase Screen para poder configurar nuestra pantalla
screen = Screen()

# Desactiva la animación automática de la pantalla. mientras se carga la imagen y cosas del juego
screen.tracer(0)

#creamos objeto de la clase score en my_score.py
score=Score()

#lista vacia donde se almacenaran la respuesta de los usuarios
guessed_states=[]

#escribimos el puntaje actual de numero de estados
score.number_of_states(get_score=len(guessed_states))

#TODO: establecer el mapa de usa como fondo de nuestro screen
screen.bgpic("blank_states_img.gif")

#dimenciones de nuestro screen
screen.setup(width=725, height=591)

#titulo de nuestra screen
screen.title("U.S. States Game")

#instrucciones del juego
score.instructions()

#ventana emergente para que el usuraio ingresae la respuesta del estado y la guardamos en una variable
user_answer=(screen.textinput("Name the US states","Enter state:")).title()
#usando title() nos aseguramos que la primeras letras este en mayuscula


#activamos de nuevo la animacion ya una vez todo lo del juego esta cargado

screen.tracer(1)



#bucle while para asegurarnos que el juego siga corriendo
#verificamos si la respuesta ingresada por el usuario es correcta
while len(guessed_states)<50:
   
    
    if user_answer in states_list:
        #si la respuesta del usuario es correcta agregamos la respuesta a la lista
        guessed_states.append(user_answer)        
        
        #TODO: obtenemos la cordenada 'x' y 'y' del estado para poder poner el nombre del estado en el mapa
        
        #usando el metodo index() de las listas puedo encontrar el indice de un item 'estado' dentro de la lista
        state_index=states_list.index(user_answer)
        
        #sabiendo el indice puedo acceder a los valores 'x' y 'y' del estado, el indice del 'estado' dentro de la lista concuerda 
        #con el indice en el diccionario
        state_index_x=states_dic[state_index]['x']
        
        #igualmente obtenemos la cordenada 'y' del estado
        state_index_y=states_dic[state_index]['y']
        
        #TODO: obteniendo las cordenadas 'x' y 'y' del estado hubicamos la respuesta dentro del mapa
        #creando objeto de la clase My_turtle
        my_turtle=My_turtle(state_index_x, state_index_y, state_name=user_answer)
        
        #turtle se va a la posicion especifica del estado segun sus cordenadas x,y
        my_turtle.go_to_position()
        
        #escribimos　el nombre del estado
        my_turtle.write_state_name()
        
        #actualizamos el puntaje del user, chequiando la longitud de la lista guessed_states
        get_score=len(guessed_states)
        score.number_of_states(get_score)
        
            
    #si el usuario ingresa exit, se corta el ciclo while y termina el game    
    if user_answer == 'Exit':
        break

    #volvemos a preguntar al usario por el nombre de un estado
    user_answer=(screen.textinput("Can you name the US states?","Enter state:")).title()

    

#TODO:creamos un archivo CSV que contiene los estados que no fueron adivinados por el usuario

#lista de estados que no fueron adivinados por el usuario
unguess_states=[]

#recorrlo la lista de estados que proviene del archivo usa_states.csv
for state in states_list:
    
    #comparo si el state esta dentro de la lista de estados adivinados por el usuario 
    if state not in guessed_states:
        
        #si no se encuentra el estado lo agrego a la nueva lista de estados no adivinados
        unguess_states.append(state)
        
unguess_dataframe=pandas.DataFrame(unguess_states)

#los states que el usuario no se sabe se exportan en un nuevo archivo, para que pueda estuidiarlos
unguess_dataframe.to_csv('learn.cvs')


#cerrar cuando se hace click
screen.exitonclick()