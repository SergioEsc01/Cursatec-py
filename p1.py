#Practica n°1
# 1. Declarar variables
variable_int = 42
variable_float = 3.14
variable_string = "Hola, soy una cadena"
variable_bool = True
variable_none = None

# 2. Mostrar contenido y tipo de dato
print("Contenido de las variables y sus tipos:")
print("Variable int:", variable_int, "Tipo:", type(variable_int))
print("Variable float:", variable_float, "Tipo:", type(variable_float))
print("Variable string:", variable_string, "Tipo:", type(variable_string))
print("Variable bool:", variable_bool, "Tipo:", type(variable_bool))
print("Variable None:", variable_none, "Tipo:", type(variable_none))

# 3. Mostrar "Hola Mundo"
print("Hola Mundo")

# 4. Ingresar nombre y mostrar saludo
nombre = input("Ingresa tu nombre: ")
print("Hola", nombre + ",", "¿cómo estás?")

# 5. Ingresar números y mostrar tipos de dato
entrada = input("Ingresa algo: ")
if entrada.isdigit():
    numero = int(entrada)
    print("Tipo de dato:", type(numero))
else:
    print("Tipo de dato:", type(entrada))

# 6. Operadores aritméticos, relaciones y lógicos
a = 10
b = 5
c = 10

print("Resultado de operaciones:")
print("a + b =", a + b)
print("a * b =", a * b)
print("a > b:", a > b)
print("a <= b:", a <= b)
print("a == c:", a == c)
print("b != c:", b != c)
print("a > b and b < c:", a > b and b < c)
print("a > b or b > c:", a > b or b > c)
print("not variable_bool:", not variable_bool)