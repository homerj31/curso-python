import sys
import os
sys.path.append(os.path.abspath('modulos'))

import limpieza_pantalla as lp
lp.limpiar_pantalla()

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# print ("introduce el primero numero:")
# numero1 = int(input())
# print ("introduce el segundo numero:")
# numero2 = int(input())

# if numero1 > numero2:
#     print (f"El pimer numero {numero1} es mayor que el segundo numero {numero2}")
# elif numero1 < numero2:
#     print (f"El segunndo numero {numero2} es mayor que el primer numero {numero1}")
# else:
#     print (f"El primer numero {numero1} es igual que el segundo numero {numero2}")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# print ("introduce el primero numero:")
# numero1 = int(input())
# print ("introduce el segundo numero:")
# numero2 = int(input())
# print ("introduce la operacion deseada:")
# print ("+ - * /")
# operacion = input()
# if operacion == '+':
#     resultado = numero1 + numero2
# elif operacion == '-':
#     resultado = numero1 - numero2
# elif operacion == '*':
#     resultado = numero1 * numero2
# elif operacion == '/':
#     if numero2 == 0:
#         print ("No se puede dividir entre cero")
#     else:
#         resultado = numero1 / numero2
        
# if 'resultado' in locals(): #Comprueba si la variable resultado existe.
#     print(f"El resultado es: {resultado}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# print ("introduce el año que quieres comprobar:")
# ano = int(input())
# if ano % 4 == 0:
#     if ano % 100 == 0:
#         if ano % 400 == 0:
#             print (f"el año {ano} es bisiesto")
#         else:
#             print (f"el año {ano} no es bisiesto")
#     else:
#         print (f"el año {ano} no es bisiesto")
# else:
#     print (f"el año {ano} no es bisiesto")

# anio = int(input("Introduce un año: "))

# if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
#     print(f"{anio} es un año bisiesto.")
# else:
#     print(f"{anio} no es un año bisiesto.")



# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Dinme tu edad: "))
if edad >=0 and edad <=2:
    print ("Eres un bebe")
elif edad >=3 and edad <=12:
    print ("Eres un niño")
elif edad >=13 and edad <=17:
    print ("Eres un adolescente")
elif edad >=18 and edad <=64:
    print ("Eres un adulto")
elif edad >=65:
    print ("Eres un adulto mayor")