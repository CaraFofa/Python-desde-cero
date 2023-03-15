#Trabajando con diccionarios
my_dict = dict() 
my_other_dict = {} #Forma corta tipo de dato

print(type(my_dict))
print(type(my_other_dict))

# Clave:Valor
my_other_dict = {"Nombre":"Cristian", "Apellido":"Mato", "Edad":37, 1:"Python"} #Datos separados por comas es un dict, pares de valores
print (my_other_dict)

my_dict = { #Dentro de un diccionario podemos añadir otro diccionario, set, list
            "Nombre": "Cristian",
            "Apellido":"Mato",
            "Edad":37,
            "Lenguajes": ("Python","C","JS"),
            1: 1.85
        }

print (my_dict)
print (my_other_dict)
print (len(my_other_dict))
print (len(my_dict))

print (my_dict["Nombre"]) 

my_dict["Nombre"] = "Pedro" #Modificamos 
print (my_dict["Nombre"])
my_dict["Calle"] = "Prince" #Añadimos nuevo valor
print (my_dict["Calle"])

del my_dict["Calle"] #Eliminamos 1 elemento (algo eliminado no se puede recuperar, es tiempo de ejecución)
print (my_dict)

print ("Nombre" in my_dict) #Encuentra valores
print ("Pedro" in my_dict) #No encuentra valor

print (my_dict.items()) #Objetos
print (my_dict.keys()) #Claves
print (my_dict.values()) #Valores
#print (my_dict.fromkeys("Nombre"))

my_new_dict = my_dict.fromkeys(("Nombre", "Piso")) #Diccionario vacío
print (my_new_dict)

my_new_dict["Nombre"] = "CrisFromKeys"
my_new_dict["Piso"] = "Prince"
print (my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print (my_new_dict)
