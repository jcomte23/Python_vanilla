# ============================================
# ENUMERATE() EN PYTHON
# ============================================
# enumerate() es una función que toma un iterable (lista, tupla, string, etc.)
# y devuelve un objeto enumerate que produce tuplas de (índice, elemento)

# --------------------------------------------
# 1. USO BÁSICO DE ENUMERATE
# --------------------------------------------

frutas = ["manzana", "banana", "naranja", "uva"]

# Sin enumerate (forma tradicional)
print("Sin enumerate:")
for i in range(len(frutas)):
    print(f"Índice {i}: {frutas[i]}")

print("\n" + "="*50 + "\n")

# Con enumerate (forma pythónica y elegante)
print("Con enumerate:")
for indice, fruta in enumerate(frutas):
    # enumerate devuelve tuplas (0, "manzana"), (1, "banana"), etc.
    print(f"Índice {indice}: {fruta}")

print("\n" + "="*50 + "\n")

# --------------------------------------------
# 2. ENUMERATE CON ÍNDICE PERSONALIZADO
# --------------------------------------------
# Por defecto, enumerate empieza en 0, pero puedes cambiar el inicio

print("Enumerate comenzando en 1:")
for numero, fruta in enumerate(frutas, start=1):
    # Ahora los índices van de 1 a 4 en lugar de 0 a 3
    print(f"{numero}. {fruta}")

print("\n" + "="*50 + "\n")

# --------------------------------------------
# 3. ENUMERATE CON STRINGS
# --------------------------------------------

palabra = "Python"
print("Enumerate con strings:")
for posicion, letra in enumerate(palabra):
    # Cada carácter del string es tratado como un elemento
    print(f"Posición {posicion}: '{letra}'")

print("\n" + "="*50 + "\n")

# --------------------------------------------
# 4. ENUMERATE CON CONDICIONALES
# --------------------------------------------

numeros = [10, 25, 30, 45, 50, 15, 60]
print("Encontrar índices de números mayores a 30:")
for idx, num in enumerate(numeros):
    if num > 30:
        print(f"El número {num} está en el índice {idx}")

print("\n" + "="*50 + "\n")

# --------------------------------------------
# 5. ENUMERATE CON LISTAS DE COMPRENSIÓN
# --------------------------------------------

# Crear una lista de tuplas (índice, valor al cuadrado)
cuadrados = [(i, x**2) for i, x in enumerate([1, 2, 3, 4, 5])]
print("Lista de comprensión con enumerate:")
print(cuadrados)
# Resultado: [(0, 1), (1, 4), (2, 9), (3, 16), (4, 25)]

print("\n" + "="*50 + "\n")

# --------------------------------------------
# 6. EJEMPLO PRÁCTICO: MODIFICAR LISTA
# --------------------------------------------

precios = [100, 200, 150, 300]
print("Precios originales:", precios)

# Aplicar 10% de descuento a productos en posiciones pares
for i, precio in enumerate(precios):
    if i % 2 == 0:  # Posiciones 0, 2, 4...
        precios[i] = precio * 0.9  # 10% de descuento

print("Precios con descuento en posiciones pares:", precios)

print("\n" + "="*50 + "\n")

# --------------------------------------------
# 7. ENUMERATE CON MÚLTIPLES ITERABLES (ZIP)
# --------------------------------------------

nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]

print("Combine enumerate con zip:")
for idx, (nombre, edad) in enumerate(zip(nombres, edades)):
    # zip combina ambas listas, enumerate añade el índice
    print(f"{idx + 1}. {nombre} tiene {edad} años")

print("\n" + "="*50 + "\n")

# --------------------------------------------
# 8. ENUMERATE CON DICCIONARIOS
# --------------------------------------------

estudiante = {
    "nombre": "Carlos",
    "edad": 20,
    "carrera": "Ingeniería"
}

print("Enumerate con diccionarios:")
for idx, (clave, valor) in enumerate(estudiante.items()):
    # .items() devuelve tuplas (clave, valor)
    print(f"{idx}. {clave}: {valor}")

print("\n" + "="*50 + "\n")

# --------------------------------------------
# 9. EJEMPLO REAL: MENÚ INTERACTIVO
# --------------------------------------------

opciones = ["Ver productos", "Agregar al carrito", "Pagar", "Salir"]

print("MENÚ PRINCIPAL:")
for num, opcion in enumerate(opciones, start=1):
    print(f"  {num}. {opcion}")

# El usuario vería:
#   1. Ver productos
#   2. Agregar al carrito
#   3. Pagar
#   4. Salir

print("\n" + "="*50 + "\n")

# --------------------------------------------
# 10. VENTAJAS DE ENUMERATE
# --------------------------------------------
# ✓ Más legible que range(len())
# ✓ Más pythónico y elegante
# ✓ Menos propenso a errores de índice
# ✓ Permite acceso simultáneo a índice y valor
# ✓ Funciona con cualquier iterable