print("*"*41)
print("|       Manejo de Listas en python      |")
print("*"*41)
print("En Python, una lista es una estructura de datos muy versátil que se utiliza para almacenar una colección ordenada de elementos.")
print("")


print("*"*23)
print("|       CREACION      |")
print("*"*23)
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mezclada = [1, "dos", 3.0, True]
print(lista_vacia)
print(lista_numeros)
print(lista_mezclada)

print("")
print("*"*23)
print("|       ACCEDER      |")
print("*"*23)
lista = ["a", "b", "c", "d", "e"]
primer_elemento = lista[0]     # "a"
ultimo_elemento = lista[-1]    # "e"
sublista = lista[1:4]   # ["b", "c", "d"]
print(lista)
print(primer_elemento)
print(ultimo_elemento)
print(sublista)

print("")
print("*"*23)
print("|       Alterar      |")
print("*"*23)
lista = [1, 2, 3, 4, 5]
lista[2] = 10   # Cambiar el tercer elemento a 10
lista = [1, 2, 3]
lista.append(4)     # Agrega 4 al final de la lista
lista.extend([5, 6])  # Extiende la lista con los elementos de otra lista
lista.insert(2, 10)  # Inserta el valor 10 en el índice 2
lista.remove(3)     # Elimina la primera ocurrencia del valor 3
elemento_eliminado = lista.pop()  # Elimina y devuelve el último elemento


# Ejemplo manejo de listas
print("")
miembrosDeLaFamilia=[
    "tatarabuelo"
]
miembrosDeLaFamiliaExpulsado=[]




miembrosDeLaFamilia.append("abuelo")
miembrosDeLaFamilia.insert(1,"abuela")
miembrosDeLaFamilia.append("papa")
miembrosDeLaFamilia.append("mama")
miembrosDeLaFamilia.append("yo")
print("ANTES:",miembrosDeLaFamilia)
del miembrosDeLaFamilia[2]
miembrosDeLaFamilia.remove("abuelo")
miembrosDeLaFamiliaExpulsado.append(miembrosDeLaFamilia.pop(2))
print("DESPUES:",miembrosDeLaFamilia)
miembrosDeLaFamilia.rev()
print("familia ordenada alfabeticamente:",miembrosDeLaFamilia)
print("cantidad de miembros: ",len(miembrosDeLaFamilia))
print("miembros expulsado: ",miembrosDeLaFamiliaExpulsado)


for miembro in miembrosDeLaFamilia:
    print("#->", miembro.upper())

print("")

tuplaMesclada=("javier",234,"javier","hola mundo")
print(type(tuplaMesclada))
print(tuplaMesclada.count("Javier"))

tuplaMesclada=list(tuplaMesclada)
print(tuplaMesclada)



