#Trabajando con set estructuras no ordenadas y no admite duplicados
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario {}

my_other_set = {"Cristian", "Vecino", 37}
print(type(my_other_set))

print(len(my_other_set))
# print(my_other_set[1]) TypeError: 'set' object is not subscriptable
my_other_set.add("Azul")
print(my_other_set) #Un set no es estructura ordenada 
my_other_set.add("Azul")

print(my_other_set) #Un set no admite repetidos 
print("Cristian" in my_other_set)
print("Cris" in my_other_set)

my_other_set.remove("Cristian")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))
del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Cristian", "Vecino", 37}
my_list = list(my_set)

my_other_set ={"Python","C","JavaScript"}
print(my_other_set)

my_new_set = my_set.union(my_other_set)
print (my_new_set) #Contiene todas las propiedades "Cristian", "Vecino", 37, "Python","C","JavaScript"

print (my_new_set.union(my_new_set)) #No admite duplicados
print (my_new_set.union({"Switf","Prueba"})) #No se almacena en la variable
print(my_new_set)

