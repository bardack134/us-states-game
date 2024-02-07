import time
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

#TODO: establecer el mapa de usa como fondo de nuestro screen
screen.bgpic("blank_states_img.gif")

#dimenciones de nuestro screen
screen.setup(width=725, height=491)



#titulo de nuestra screen
screen.title("U.S. States Game")



#ventana emergente para que el usuraio ingresae la respuesta del estado y la guardamos en una variable
user_answer=(screen.textinput("Can you name the US states?","Enter state:")).capitalize()

#usando capitalize() nos aseguramos que la primera letra este en mayuscula
# user_answer=user_answer.capitalize()

#condicional de nuestro bucle while
game_is_on=True

#activamos de nuevo la animacion ya una vez todo lo del juego esta cargado
screen.tracer(1)

#bucle while para asegurarnos que el juego siga corriendo
#verificamos si la respuesta ingresada por el usuario es correcta
while game_is_on==True:
    #La pantalla se va actualizar cada 0.1 segundos, dentro de nuestro while el codigo correra cada 0.1 segundos
    # time.sleep(0.1)
    # screen.update()
    if user_answer in states_list:
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
        
        
        
    else:
        print("incorrect")

    #volvemos a preguntar al usario por el nombre de un estado
    user_answer=(screen.textinput("Can you name the US states?","Enter state:"))

    #usando capitalize() nos aseguramos que la primera letra este en mayuscula
    user_answer=user_answer.capitalize()


#cerrar cuando se hace click
screen.exitonclick()