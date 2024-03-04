listaNumeros=[]

    

# #VERSION CLASICA
# numero1=int(input("ingrese el numero 1"))
# numero2=int(input("ingrese el numero 2"))
# numero3=int(input("ingrese el numero 3"))
# numero4=int(input("ingrese el numero 4"))
# numero5=int(input("ingrese el numero 5"))

# listaNumeros.append(numero1)
# listaNumeros.append(numero2)
# listaNumeros.append(numero3)
# listaNumeros.append(numero4)
# listaNumeros.append(numero5)

# for contador in range(5):
#     numero=int(input("ingrese un numero"))
#     listaNumeros.append(numero)
    


# #VERSION CON EL CICLO FOR
# for numeroVuelta in range(5):
#     numero=int(input(f"ingrese un numero # {numeroVuelta}=>"))
#     listaNumeros.append(numero)
    
# print(listaNumeros)

# #VERSION CON EL CICLO WHILE
numeroVuelta=6
while numeroVuelta!=6:
    numero=int(input(f"ingrese un numero # {numeroVuelta}=>"))
    listaNumeros.append(numero)
    
    numeroVuelta+=1


# Ejercicios de estudiantes
listaEstudiantesRiwi=[]

ingresarOtroEstudiante="si"
while ingresarOtroEstudiante=="si":
    print("Nuevo estudiante")
    nombre=input("ingrese el nombre =>")
    apellido=input("ingrese el apellido =>")
    edad=input("ingrese la edad =>")
    direccion=input("ingrese la direccion =>")
    correo=input("ingrese su correo =>")

    estudiante={
        "nombre":nombre,
        "apellido":apellido,
        "edad":edad,
        "direccion":direccion,
        "correo":correo
    }
    
    listaEstudiantesRiwi.append(estudiante)
    respuesta=input("vas a ingresar otro estudiante? =>")
    
    if respuesta!="si":
        ingresarOtroEstudiante=False

for estudiante in listaEstudiantesRiwi:
    print(f"""
        Nombre=> {estudiante["nombre"]}
        Apellido=> {estudiante["apellido"]}
        Edad=> {estudiante["edad"]}
        Correo=> {estudiante["correo"]}
        Direccion=> {estudiante["direccion"]}
    """)