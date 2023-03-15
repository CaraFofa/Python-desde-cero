# Trabajando con strings
my_string = "Mi string"
my_other_string = "Mi otro string"

print (len(my_string))
print (len(my_other_string))
print (my_string + " y " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print (my_new_line_string)
my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)
my_string_escape = "\\Este es un string escapado"
print (my_string_escape)

# Formateo
name, surname, age = "Cristian", "Mato", 37
print ("Mi nombre es {} {} y mi edad es {} con format".format (name, surname, age)) 
print ("Mi nombre es %s %s y mi edad es %d con tanto por ciento" %(name, surname, age))
print ("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #Concatenación Complejo 
print (f"Mi nombre es {name} {surname} y mi edad es {age}") #Inferencia de datos

# Desempaquetado de carácteres
language = "Python"
a, b, c, d, e, f, h, i = "language"
print (language)

# Division
language_slice = language[1:3]
print(language_slice) #Muestra únicamente cáracteres 1 y 3

# Reverse
reversed_slice = language[::-1] #Voltea a lo mostrado
print(reversed_slice)

#Funciones
print(language.capitalize()) #Primera Mayus
print(language.count("y"))
print(language.upper().isupper()) #Combinado UP?
print(language.lower())
print(language.startswith("Py")) #Pregunta start
print("Py" == "py")
