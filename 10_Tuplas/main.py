# TUPLAS EN PYTHON
# Son colecciones INMUTABLES (no se pueden modificar después de crearlas)
# Se usan para datos que no deben cambiar, son más rápidas que las listas
# Se definen con paréntesis ()

# ============ CREAR TUPLAS ============

# Forma 1: Con paréntesis
coordenadas = (10, 20)
persona = ("Juan", 30, "Madrid")

# Forma 2: Sin paréntesis (también funciona)
numeros = 1, 2, 3, 4, 5

# Tupla de un solo elemento - NECESITA UNA COMA
una_tupla = (42,)  # ✅ Correcto
# no_es_tupla = (42)  # ❌ Esto es solo un número entre paréntesis

# Tupla vacía
vacia = ()
# o también: vacia = tuple()

# Convertir lista a tupla
lista = [1, 2, 3]
tupla_desde_lista = tuple(lista)


# ============ ACCEDER A ELEMENTOS ============

frutas = ("manzana", "banana", "cereza", "durazno")

# Por índice (igual que listas)
print(frutas[0])   # manzana
print(frutas[-1])  # durazno (último elemento)

# Slicing (rebanadas)
print(frutas[1:3])   # ('banana', 'cereza')
print(frutas[:2])    # ('manzana', 'banana')
print(frutas[2:])    # ('cereza', 'durazno')


# ============ INMUTABILIDAD ============

colores = ("rojo", "verde", "azul")

# ❌ NO puedes modificar elementos
# colores[0] = "amarillo"  # TypeError: 'tuple' object does not support item assignment

# ❌ NO puedes agregar elementos
# colores.append("negro")  # AttributeError: 'tuple' object has no attribute 'append'

# ❌ NO puedes eliminar elementos
# del colores[0]  # TypeError


# ============ OPERACIONES BÁSICAS ============

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenar tuplas (crea una NUEVA tupla)
t3 = t1 + t2
print(t3)  # (1, 2, 3, 4, 5, 6)

# Repetir tuplas
t4 = t1 * 3
print(t4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Longitud
print(len(t1))  # 3


# ============ VERIFICAR EXISTENCIA ============

numeros = (10, 20, 30, 40, 50)

if 30 in numeros:
    print("30 está en la tupla")

if 100 not in numeros:
    print("100 NO está en la tupla")


# ============ MÉTODOS DE TUPLAS ============

valores = (1, 2, 3, 2, 4, 2, 5)

# count() - cuenta cuántas veces aparece un valor
print(valores.count(2))  # 3

# index() - devuelve el índice de la primera aparición
print(valores.index(4))  # 4
# print(valores.index(10))  # ❌ ValueError si no existe


# ============ DESEMPAQUETADO DE TUPLAS ============

# Asignar valores de una tupla a variables
coordenadas = (100, 200)
x, y = coordenadas
print(x)  # 100
print(y)  # 200

# Con más elementos
persona = ("Ana", 25, "Ingeniera")
nombre, edad, profesion = persona
print(f"{nombre} tiene {edad} años")

# Desempaquetado con * (captura el resto)
numeros = (1, 2, 3, 4, 5)
primero, segundo, *resto = numeros
print(primero)  # 1
print(segundo)  # 2
print(resto)    # [3, 4, 5] - ¡se convierte en lista!

primero, *medio, ultimo = numeros
print(medio)  # [2, 3, 4]


# ============ ITERAR SOBRE TUPLAS ============

dias = ("lunes", "martes", "miércoles", "jueves", "viernes")

# Forma 1: sobre elementos
for dia in dias:
    print(dia)

# Forma 2: con índice usando enumerate()
for indice, dia in enumerate(dias):
    print(f"{indice}: {dia}")


# ============ TUPLAS ANIDADAS ============

# Tuplas dentro de tuplas
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matriz[0])      # (1, 2, 3)
print(matriz[1][2])   # 6


# ============ COMPARACIÓN DE TUPLAS ============

# Se comparan elemento por elemento, de izquierda a derecha
print((1, 2, 3) < (1, 2, 4))   # True
print((1, 2) < (1, 2, 0))      # True (la más corta es menor)
print(("a", "b") < ("a", "c")) # True


# ============ TUPLAS VS LISTAS ============

# VENTAJAS de las tuplas:
# 1. Son más RÁPIDAS que las listas
# 2. PROTEGEN los datos (inmutables)
# 3. Pueden usarse como CLAVES en diccionarios (las listas no)
# 4. Ocupan MENOS MEMORIA

diccionario_con_tuplas = {
    (0, 0): "origen",
    (1, 0): "punto A",
    (0, 1): "punto B"
}
print(diccionario_con_tuplas[(0, 0)])  # origen

# Las listas NO pueden ser claves:
# diccionario = {[1, 2]: "valor"}  # ❌ TypeError: unhashable type: 'list'


# ============ CUÁNDO USAR TUPLAS ============

# Usa tuplas para:
# - Coordenadas: (x, y, z)
punto_3d = (10, 20, 30)

# - Datos que no deben cambiar
fecha_nacimiento = (15, 8, 1990)  # día, mes, año

# - Retornar múltiples valores de una función
def calcular_estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

minimo, maximo, promedio = calcular_estadisticas([1, 2, 3, 4, 5])

# - Claves de diccionarios
ubicaciones = {
    (40.7128, -74.0060): "Nueva York",
    (51.5074, -0.1278): "Londres"
}


# ============ TUPLA NOMBRADA (namedtuple) ============

from collections import namedtuple

# Crea una clase de tupla con nombres para cada campo
Punto = namedtuple('Punto', ['x', 'y'])
p = Punto(10, 20)

print(p.x)      # 10 - acceso por nombre
print(p[0])     # 10 - acceso por índice (también funciona)
print(p)        # Punto(x=10, y=20)

# Útil para hacer el código más legible
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])
juan = Persona('Juan', 30, 'Madrid')
print(f"{juan.nombre} vive en {juan.ciudad}")


# ============ CONVERSIONES ============

# Tupla a lista
mi_tupla = (1, 2, 3)
mi_lista = list(mi_tupla)
print(mi_lista)  # [1, 2, 3]

# Lista a tupla
mi_lista = [4, 5, 6]
mi_tupla = tuple(mi_lista)
print(mi_tupla)  # (4, 5, 6)

# String a tupla
texto = "Python"
tupla_letras = tuple(texto)
print(tupla_letras)  # ('P', 'y', 't', 'h', 'o', 'n')