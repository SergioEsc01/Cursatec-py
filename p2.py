#Practico numero 2
#1
menores = 0
mayores = 0

while True:
    edad = int(input("Ingresa la edad (-1 para terminar): "))
    
    if edad == -1:
        break
    elif edad < 18:
        menores += 1
    else:
        mayores += 1

print("Personas menores de edad:", menores)
print("Personas mayores o iguales a 18 años:", mayores)
#2
a = float(input("Ingresa el número A: "))
b = float(input("Ingresa el número B: "))

if a > b:
    print("A es mayor que B")
elif b > a:
    print("B es mayor que A")
else:
    print("A y B son iguales")

#3
cantidad_empleados = int(input("Ingresa la cantidad de empleados: "))
total_sueldos = 0

for i in range(cantidad_empleados):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i+1}: "))
    total_sueldos += sueldo

sueldo_promedio = total_sueldos / cantidad_empleados
print("El sueldo promedio de los empleados es:", sueldo_promedio)

#4
total_importe = 0

while True:
    producto = input("Ingresa el nombre del producto (o 'Fin' para terminar): ")
    
    if producto.lower() == "fin":
        break
    precio = float(input("Ingresa el precio del producto: "))
    total_importe += precio

print("Importe total de los productos:", total_importe)






