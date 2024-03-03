import math

print("*"*41)
print("|       Manejo de numeros en python      |")
print("*"*41)

print()
print("Para el manejo de números, es importante distinguir entre enteros (int) y números decimales (float)")
print("La variable 'numeroB' será un entero, lo que significa que solo puede contener números enteros, sin decimales.")
print("La variable 'numeroC' permitirá valores decimales, lo que significa que puede contener números enteros y decimales.")
print("En resumen la variable 'numeroB' será un entero, mientras que 'numeroC' permitirá decimales.")
print()

numeroB = int(input("Ingresa un número entero para 'numeroB': "))
numeroC = float(input("Ingresa un número decimal para 'numeroC': "))

print()
print("Conversion de numeros")
print("Python permite convertir entre diferentes tipos de números, como enteros, flotantes y complejos.")
print()

entero = int(3.14)
flotante = float("3.14")

print()
print(f"Valor de numeroB: {numeroB}, Tipo: {type(numeroB)}")
print(f"Valor de numeroC: {numeroC}, Tipo: {type(numeroC)}")

# Otras funciones matemáticas
print(math.sqrt(25))  # Imprime la raíz cuadrada de 25
print(math.factorial(5))  # Imprime el factorial de 5

# Constantes matemáticas
print(math.pi)  # Imprime el valor de π
print(math.e)   # Imprime el valor de e



