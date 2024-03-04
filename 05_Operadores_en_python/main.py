# ######################
# OPERADORES ARITMÉTICOS
# ######################

numeroA = 4
numeroB = 2

# Operador de suma (+)
print(numeroA + numeroB)  # 6

# Operador de resta (-)
print(numeroA - numeroB)  # 2

# Operador de multiplicación (*)
print(numeroA * numeroB)  # 8

# Operador de división (/)
print(numeroA / numeroB)  # 2.0

# Devuelve el residuo de una división (%)
print(13 % 5)  # 3

# Exponenciación de 2 números
print(2 ** 8)  # 256

# Incrementos de a una unidad
numeroTemp1 = 2
numeroTemp1 += 1
print(numeroTemp1)  # 3

# Decrementos de a una unidad
numeroTemp2 = 5
numeroTemp2 -= 1
print(numeroTemp2)  # 4

# Incrementos de múltiples unidades
numeroTemp3 = 3
numeroTemp3 += 5
print(numeroTemp3)  # 8

# Decrementos de múltiples unidades
numeroTemp4 = 13
numeroTemp4 -= 4
print(numeroTemp4)  # 9


# #########################
# OPERADORES DE COMPARACIÓN
# #########################

NUMERO1 = 20
NUMERO2 = "20"
NUMERO3 = 30

# Comparador de igualdad
print(10 == 10)  # True
print(10 == 14)  # False
print(2 == "2")   # False
print(2 == int("2"))  # True
print(NUMERO1 == int(NUMERO2))  # True
print(NUMERO1 == NUMERO3)  # False

# Comparador de desigualdad
print(10 != 10)  # False
print(10 != 14)  # True
print(2 != "2")  # True
print(2 != int("2"))  # False

PASSWORD = "Abc123"
PASSWORD_CONFIRMATION = "ABC123"

print(PASSWORD != PASSWORD_CONFIRMATION)  # True

# Operador (mayor que)
print(f"¿{NUMERO1} es mayor que {NUMERO3}? => {NUMERO1 > NUMERO3}")  # False

# Operador (menor que)
print(f"¿{NUMERO1} es menor que {NUMERO3}? => {NUMERO1 < NUMERO3}")  # True

# Operador >= o <=
print(f"¿{NUMERO1} es mayor o igual que {NUMERO2}? => {NUMERO1 >= int(NUMERO2)}")  # True
print(f"¿{NUMERO1} es menor o igual que {NUMERO3}? => {NUMERO1 <= NUMERO3}")  # True


# #####################
# OPERADORES LÓGICOS
# #####################

# Operador AND (and)
estatura = 4.0
print(estatura >= 1.71 and type(estatura)==float)  # True
print(estatura >= 1.71 and isinstance(estatura, int))  # False

# Operador OR (or)
print(estatura >= 1.71 or isinstance(estatura, float))  # True

# Operador NOT (not)
variable = True
print(variable)  # True
print(not variable)  # False
