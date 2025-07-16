from os import system
if system("clear") != 0:
    system("cls")

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

# print("\nEjercicio 1:")
# CONTADOR = 10
# while CONTADOR >=1:
#     print (CONTADOR)
#     CONTADOR -=1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

# print("\nEjercicio 2:")
# CONTADOR = 1
# TOTAL = 0
# while CONTADOR <=20:
#     if CONTADOR % 2 == 0:
#         #print (f"numero = { CONTADOR}")
#         TOTAL+= CONTADOR
#     CONTADOR += 1
# print (TOTAL)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

# print("\nEjercicio 3:")
# NUMERO = -1
# #BUCLE PARA CONTROLAR EL NUMERO QUE INGRESA EL USUARIO
# while NUMERO <=0:
#     try:
#         NUMERO = int(input("Introduce un numero entero positivo:"))
#     except ValueError:
#         print ("No has introducido un numero")
# #BUCLE PARA CALCULAR EL FACTORIAL
# TOTAL = 1
# while NUMERO>=1:
#     TOTAL*=NUMERO
#     NUMERO-=1

# print (TOTAL)

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

# print("\nEjercicio 4:")
# VALIDA = False
# while VALIDA is not True:
#     PASS = input ("Introduce una contraseña de al menos 8 caracteres:")
#     if len(PASS) >= 8:
#         VALIDA = True
# print (f"La contraseña introducida es: {PASS}")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")
# #BUCLE PARA CONTROLAR EL NUMERO QUE INGRESA EL USUARIO
# NUMERO = -1
# while NUMERO <=0:
#     try:
#         NUMERO = int(input("Introduce un numero entero positivo:"))
#     except ValueError:
#         print ("No has introducido un numero")

# #BUCLE PARA PINTAR TABLA DE MULTIPLICAR
# print (f"Vamos a dibujar la tabla de multipplicar de {NUMERO}")
# CONTADOR = 1
# while CONTADOR <= 10:
#     print (f"{NUMERO} * {CONTADOR} =",NUMERO * CONTADOR)
#     CONTADOR += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
# #BUCLE PARA CONTROLAR EL NUMERO QUE INGRESA EL USUARIO
NUMERO = -1
while NUMERO <=0:
    try:
        NUMERO = int(input("introduce un numero entero positivo:"))
    except ValueError:
        print ("no has introducido un numero")
print (f"Vamos a pintar los numeros primos entre 1 y {NUMERO}")
#BUCLE PARA PINTAR LOS NUMEROS PRIMOS
#MITAD = int(NUMERO / 2)
print (f"NUMERO: {NUMERO}")
#print (MITAD)
while NUMERO >= 1:
    #print (f"VAMOS A ANALIZAR EL NUMERO: {NUMERO}")
    CONTADOR = 2
    ES_PRIMO = True
    while CONTADOR <= int(NUMERO/2) and ES_PRIMO:
        if NUMERO % CONTADOR == 0:
            ES_PRIMO = False
        CONTADOR +=1
    if ES_PRIMO:
        print (F"El numero {NUMERO} es primo")
    else:
        print (F"El numero {NUMERO} no es primo")
    NUMERO -= 1