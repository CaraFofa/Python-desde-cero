#Listas en Py (Arrays no existen en Python)
my_list = [18, 35, 37, 26, 42]
print(len(my_list))

my_other_list = [37, 1.85, "Cristian", "Vecino", 2.49, 653333542]
print(my_other_list)
print(type(my_other_list)) #Ver tipo lista
print (my_other_list[-2]) #En otros lenguajes ERROR
print (my_other_list.count("Vecino"))

#age, long, name, surname, mid, phone = my_other_list[0], my_other_list[1], my_other_list[3] #Mala práctica
print (my_list + my_other_list)
my_list = my_list
