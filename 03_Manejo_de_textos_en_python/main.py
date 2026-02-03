# print("*"*30)
# print("|       Manejo de textos     |")
# print("*"*30)
# print()
# # El input por defecto trae todo en strings por lo tanto es innecesario enmascararlo en str()
# variable1=input("variable 1: ")
# variable2=str(input("variable 2: "))
# print(variable1,type(variable1))
# print(variable2,type(variable2))

# # Formas de imprimir los strings en python, TODAS SON VALIDAS Y TU DECIDES CUAL USAR
# print(variable1,variable2)
# print(variable1+variable2)
# print("variable1: {} variable2: {}".format(variable1,variable2))
# print(f"{variable1} {variable2}")

print("*" * 30)
print("|       Manejo de Textos      |")
print("*" * 30)

print()
variable1 = input("Ingrese el valor de la variable 1: ")
variable2 = input("Ingrese el valor de la variable 2: ")

print("\nResultados:")
print(f"Valor de variable1: {variable1}, Tipo: {type(variable1)}")
print(f"Valor de variable2: {variable2}, Tipo: {type(variable2)}")

# Formas de imprimir texto en Python, todas son válidas y tú decides cuál usar
print("\nFormas de imprimir texto en Python:")
print(f"Concatenación: {variable1} {variable2}")
print(f"Usando operador '+': {variable1 + variable2}")
print("Usando 'format()': variable1: {} variable2: {}".format(variable1, variable2))
print(f"Usando f-strings: {variable1} {variable2}")

# Sacar los fragmentos de texto de un string (slicing)
print()
# noinspection SpellCheckingInspection
texto = "ABCDEFGHIJKLMNOP"
print(texto)

# Un solo índice: obtiene un carácter
fragmento = texto[2]
print(fragmento)  # C

# Desde el inicio hasta el índice 5 (sin incluir)
fragmento = texto[:5]
print(fragmento)  # ABCDE

# Desde el índice 2 hasta el 5 (sin incluir)
fragmento = texto[2:5]
print(fragmento)  # CDE

# Desde el inicio hasta el final, saltando de 2 en 2
fragmento = texto[::2]
print(fragmento)  # ACEGIKMO

# Invertir el texto (de atrás hacia adelante)
fragmento = texto[::-1]
print(fragmento)  # PONMLKJIHGFEDCBA

# Desde el índice 2 hasta el 10, saltando de 2 en 2
fragmento = texto[2:10:2]
print(fragmento)  # CEGI
