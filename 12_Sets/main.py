# SETS (CONJUNTOS) EN PYTHON
# Son colecciones NO ORDENADAS de elementos ÚNICOS (sin duplicados)
# Son MUTABLES (puedes agregar/eliminar elementos)
# NO permiten elementos duplicados
# Se definen con llaves {} o con set()

# ============ CREAR SETS ============

# Forma 1: Con llaves {}
numeros = {1, 2, 3, 4, 5}
frutas = {"manzana", "banana", "cereza"}

# Forma 2: Con set()
vocales = set(["a", "e", "i", "o", "u"])

# Set vacío - ⚠️ IMPORTANTE: usa set(), NO {}
vacio = set()  # ✅ Correcto
# vacio = {}   # ❌ Esto crea un DICCIONARIO vacío

# Crear set desde string (elimina duplicados)
letras = set("mississippi")
print(letras)  # {'m', 'i', 's', 'p'} - orden no garantizado

# Los duplicados se eliminan automáticamente
numeros_duplicados = {1, 2, 2, 3, 3, 3, 4}
print(numeros_duplicados)  # {1, 2, 3, 4}


# ============ CARACTERÍSTICAS IMPORTANTES ============

# 1. NO tienen orden (no puedes acceder por índice)
colores = {"rojo", "verde", "azul"}
# print(colores[0])  # ❌ TypeError: 'set' object is not subscriptable

# 2. NO permiten elementos duplicados
animales = {"perro", "gato", "perro", "loro"}
print(animales)  # {'perro', 'gato', 'loro'} - solo elementos únicos

# 3. Los elementos deben ser INMUTABLES (hashable)
# ✅ Pueden contener: números, strings, tuplas
valido = {1, "texto", (1, 2)}
# ❌ NO pueden contener: listas, diccionarios, otros sets
# invalido = {1, [2, 3]}  # TypeError: unhashable type: 'list'


# ============ AGREGAR ELEMENTOS ============

frutas = {"manzana", "banana"}

# add() - agregar un elemento
frutas.add("cereza")
print(frutas)  # {'manzana', 'banana', 'cereza'}

# Si intentas agregar un duplicado, no pasa nada (no da error)
frutas.add("manzana")
print(frutas)  # Sigue igual, no duplica

# update() - agregar múltiples elementos (desde iterable)
frutas.update(["durazno", "pera"])
# o también: frutas.update({"durazno", "pera"})
print(frutas)


# ============ ELIMINAR ELEMENTOS ============

numeros = {1, 2, 3, 4, 5}

# remove() - elimina elemento, da ERROR si no existe
numeros.remove(3)
print(numeros)  # {1, 2, 4, 5}
# numeros.remove(10)  # ❌ KeyError

# discard() - elimina elemento, NO da error si no existe
numeros.discard(4)
numeros.discard(100)  # ✅ No pasa nada
print(numeros)  # {1, 2, 5}

# pop() - elimina y devuelve un elemento ALEATORIO
elemento = numeros.pop()
print(f"Eliminado: {elemento}")
print(numeros)

# clear() - vacía todo el set
numeros.clear()
print(numeros)  # set()


# ============ VERIFICAR EXISTENCIA ============

letras = {"a", "b", "c", "d"}

if "a" in letras:
    print("'a' está en el set")

if "z" not in letras:
    print("'z' NO está en el set")


# ============ OPERACIONES DE CONJUNTOS ============

# Dos sets de ejemplo
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# UNIÓN - todos los elementos de ambos sets (sin duplicados)
union1 = A | B
union2 = A.union(B)
print(union1)  # {1, 2, 3, 4, 5, 6, 7, 8}

# INTERSECCIÓN - solo elementos que están en AMBOS
interseccion1 = A & B
interseccion2 = A.intersection(B)
print(interseccion1)  # {4, 5}

# DIFERENCIA - elementos en A pero NO en B
diferencia1 = A - B
diferencia2 = A.difference(B)
print(diferencia1)  # {1, 2, 3}

# DIFERENCIA SIMÉTRICA - elementos en A o B, pero NO en ambos
dif_simetrica1 = A ^ B
dif_simetrica2 = A.symmetric_difference(B)
print(dif_simetrica1)  # {1, 2, 3, 6, 7, 8}


# ============ MÉTODOS DE COMPARACIÓN ============

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}

# issubset() - verifica si es subconjunto
print(set1.issubset(set2))  # True (set1 está contenido en set2)

# issuperset() - verifica si es superconjunto
print(set2.issuperset(set1))  # True (set2 contiene a set1)

# isdisjoint() - verifica si NO tienen elementos en común
set4 = {6, 7, 8}
print(set1.isdisjoint(set4))  # True (no comparten elementos)

# Comparación directa
print(set1 == set3)  # True
print(set1 == set2)  # False


# ============ ITERAR SOBRE SETS ============

# ⚠️ El orden NO está garantizado y puede variar
colores = {"rojo", "verde", "azul", "amarillo"}

for color in colores:
    print(color)

# Con enumerate (pero recuerda: orden no garantizado)
for indice, color in enumerate(colores):
    print(f"{indice}: {color}")


# ============ MÉTODOS ÚTILES ============

numeros = {1, 2, 3, 4, 5}

# len() - cantidad de elementos
print(len(numeros))  # 5

# min() y max() - para sets de números
print(min(numeros))  # 1
print(max(numeros))  # 5

# sum() - suma de elementos numéricos
print(sum(numeros))  # 15

# sorted() - devuelve una LISTA ordenada (no modifica el set)
ordenados = sorted(numeros)
print(ordenados)  # [1, 2, 3, 4, 5] - es una lista


# ============ OPERACIONES IN-PLACE ============

# Modifican el set original en lugar de crear uno nuevo
A = {1, 2, 3}
B = {3, 4, 5}

# update() o |= - unión in-place
A |= B  # equivalente a: A = A | B
print(A)  # {1, 2, 3, 4, 5}

A = {1, 2, 3}
# intersection_update() o &= - intersección in-place
A &= B
print(A)  # {3}

A = {1, 2, 3}
# difference_update() o -= - diferencia in-place
A -= B
print(A)  # {1, 2}

A = {1, 2, 3}
# symmetric_difference_update() o ^= - diferencia simétrica in-place
A ^= B
print(A)  # {1, 2, 4, 5}


# ============ CASOS DE USO PRÁCTICOS ============

# 1. ELIMINAR DUPLICADOS de una lista
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5]
sin_duplicados = list(set(lista_con_duplicados))
print(sin_duplicados)  # [1, 2, 3, 4, 5] - orden puede variar

# 2. ENCONTRAR ELEMENTOS ÚNICOS entre dos listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
unicos_lista1 = set(lista1) - set(lista2)
print(unicos_lista1)  # {1, 2, 3}

# 3. VERIFICAR SI DOS LISTAS tienen elementos en común
lista_a = ["perro", "gato", "loro"]
lista_b = ["pez", "loro", "hamster"]
if set(lista_a) & set(lista_b):
    print("Tienen elementos en común")

# 4. CONTAR CARACTERES ÚNICOS
texto = "mississippi"
caracteres_unicos = set(texto)
print(f"Caracteres únicos: {len(caracteres_unicos)}")  # 4


# ============ FROZENSET (SET INMUTABLE) ============

# Es como un set normal pero NO SE PUEDE MODIFICAR
# Útil como clave de diccionario o elemento de otro set

frozen = frozenset([1, 2, 3, 4])
print(frozen)  # frozenset({1, 2, 3, 4})

# ❌ NO puedes modificarlo
# frozen.add(5)  # AttributeError
# frozen.remove(1)  # AttributeError

# ✅ Puede ser clave de diccionario
diccionario = {frozen: "valor"}

# ✅ Puede ser elemento de un set
set_de_frozensets = {frozenset([1, 2]), frozenset([3, 4])}


# ============ COMPRENSIÓN DE SETS ============

# Crear sets de forma compacta
cuadrados = {x**2 for x in range(10)}
print(cuadrados)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Con condición
pares = {x for x in range(20) if x % 2 == 0}
print(pares)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}


# ============ CUÁNDO USAR SETS ============

# Usa sets cuando:
# - Necesitas ELIMINAR DUPLICADOS
# - Necesitas verificar MEMBRESÍA rápidamente (in es muy rápido en sets)
# - Trabajas con OPERACIONES MATEMÁTICAS de conjuntos
# - NO necesitas mantener un ORDEN específico
# - NO necesitas acceso por ÍNDICE

# Ejemplo: verificar membresía
vocales_set = {"a", "e", "i", "o", "u"}
vocales_lista = ["a", "e", "i", "o", "u"]

# in es MUCHO más rápido en sets que en listas
if "a" in vocales_set:  # O(1) - tiempo constante
    print("Es vocal")

if "a" in vocales_lista:  # O(n) - tiempo lineal
    print("Es vocal")