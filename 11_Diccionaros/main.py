# DICCIONARIOS EN PYTHON
# Son colecciones de pares clave-valor, no ordenados (antes de Python 3.7)
# pero mantienen el orden de inserción desde Python 3.7+

# ============ CREAR DICCIONARIOS ============

# Forma 1: Con llaves {}
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Forma 2: Con dict()
carro = dict(marca="Toyota", modelo="Corolla", año=2020)

# Diccionario vacío
vacio = {}
# o también: vacio = dict()


# ============ ACCEDER A VALORES ============

print(persona["nombre"])  # Juan
# print(persona["apellido"])  # ❌ KeyError si la clave no existe

# Forma segura: usar get() - devuelve None si no existe
print(persona.get("apellido"))  # None
print(persona.get("apellido", "No disponible"))  # Valor por defecto

# ============ AGREGAR/MODIFICAR ELEMENTOS ============

persona["apellido"] = "Pérez"  # Agregar nueva clave
persona["edad"] = 31  # Modificar valor existente

print(persona)  # {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'apellido': 'Pérez'}

# ============ ELIMINAR ELEMENTOS ============

del persona["ciudad"]  # Eliminar con del

eliminado = persona.pop("apellido")  # pop() elimina y devuelve el valor
print(eliminado)  # Pérez

# persona.clear()  Vacía todo el diccionario


# ============ VERIFICAR SI EXISTE UNA CLAVE ============

if "nombre" in persona:
    print("La clave 'nombre' existe")

if "telefono" not in persona:
    print("No hay teléfono registrado")

# ============ MÉTODOS IMPORTANTES ============

estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "carrera": "Ingeniería"
}

# keys() - obtener todas las claves
claves = estudiante.keys()
print(claves)  # dict_keys(['nombre', 'edad', 'carrera'])

# values() - obtener todos los valores
valores = estudiante.values()
print(valores)  # dict_values(['Ana', 22, 'Ingeniería'])

# items() - obtener pares clave-valor como tuplas
items = estudiante.items()
print(items)  # dict_items([('nombre', 'Ana'), ('edad', 22), ('carrera', 'Ingeniería')])

# ============ ITERAR SOBRE DICCIONARIOS ============

# Iterar sobre claves (forma por defecto)
for clave in estudiante:
    print(clave)

# Iterar sobre valores
for valor in estudiante.values():
    print(valor)

# Iterar sobre claves y valores simultáneamente
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

# ============ DICCIONARIOS ANIDADOS ============

# Diccionarios dentro de diccionarios
empresa = {
    "empleado1": {
        "nombre": "Carlos",
        "puesto": "Desarrollador",
        "salario": 50000
    },
    "empleado2": {
        "nombre": "María",
        "puesto": "Diseñadora",
        "salario": 45000
    }
}

print(empresa["empleado1"]["nombre"])  # Carlos

# ============ COPIAR DICCIONARIOS ============

original = {"a": 1, "b": 2}

# ❌ Esto NO copia, solo crea una referencia
copia_mala = original
copia_mala["c"] = 3
print(original)  # {'a': 1, 'b': 2, 'c': 3} - ¡se modificó el original!

# ✅ Formas correctas de copiar
copia_buena = original.copy()
# o también: copia_buena = dict(original)


# ============ UNIR DICCIONARIOS ============

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Desde Python 3.9+
combinado = dict1 | dict2
print(combinado)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Método update() - modifica el diccionario original
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# ============ DICCIONARIOS CON VALORES POR DEFECTO ============

from collections import defaultdict

# Si accedes a una clave que no existe, crea un valor por defecto
contador = defaultdict(int)  # int() devuelve 0
contador["manzanas"] += 1
contador["naranjas"] += 3
print(contador)  # defaultdict(<class 'int'>, {'manzanas': 1, 'naranjas': 3})

# ============ COMPRENSIÓN DE DICCIONARIOS ============

# Crear diccionarios de forma compacta
cuadrados = {x: x ** 2 for x in range(1, 6)}
print(cuadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Con condición
pares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(pares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
