
    ### Loops ###

# While

my_condition = 0

while my_condition < 20: # Se repite tantas veces como se cumpla la condición
    print(my_condition)
    my_condition += 1
    if my_condition == 15:
        print ("Se detiene la ejecución")
        break
    print(my_condition)
print ("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17] # lista, vector, matriz
for element in my_list: # Se repite tantas veces como elementos tenga
    print (element)     


my_tuple = ("Cristian", "Vecino", 37, 1.8)
for element in my_tuple:
    print (element)


my_dict = { #Dentro de un diccionario podemos añadir otro diccionario, set, list
            "Nombre": "Cristian",
            "Apellido":"Mato",
            "Edad":37,
            "Lenguajes": ("Python","C","JS"),
        }
for element in my_dict: # Imprime las keys , no los values
    print (element)
