#Trabajando con tuple
my_tuple = tuple()
my_other_tuple = ()

my_tuple = ("Cristian", "Vecino", 37, 1.8)
print (my_tuple)
print (type(my_tuple))

#Accediendo a los datos
print(my_tuple[0])
print(my_tuple[-1])

#print(my_tuple[4]) IndexError
print(my_tuple.count("Vecino")) #Cuenta dentro de la tupla
print (my_tuple.index(37)) #Posicion (se queda con el primero)

#Probamos a modificar valor
#my_tuple[2] = 38
#print (my_tuple) #Principal diferencia con listas, TypeError: 'tuple' object does not support item assignmen
#my_tuple[2] = my_tuple.delete[2] No se pueden modificar
print (my_tuple[2:4]) #Muestra elementos entre el 2 y el 4, sin contar el 4

my_tuple = list(my_tuple) #Le asignamos list
print (type(my_tuple))
my_tuple.insert(1 , "Azul") #Podemos añadir
print(my_tuple)
my_tuple.clear() #Vaciamos
print(my_tuple)

my_tuple = ()
print(my_tuple)

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined
