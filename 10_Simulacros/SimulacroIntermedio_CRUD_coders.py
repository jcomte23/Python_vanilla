coders=[
    {
        "nombre":"Javier",
        "edad":25,
        "riwipoints":4
    },
    {
        "nombre":"lucas",
        "edad":18,
        "riwipoints":8
    },
    {
        "nombre":"pablo",
        "edad":30,
        "riwipoints":5
    },
    {
        "nombre":"judas",
        "edad":19,
        "riwipoints":0
    },
    {
        "nombre":"mateo uno",
        "edad":36,
        "riwipoints":9
    }
]

while True:
    print("""
    MENU
    (1) registrar un nuevo coder

    (2) actualizar coder

    (3) eliminar coder

    (4) listar coders

    (5) cerrar programa
    """)

    opcionMenu=input("INGRESA LA OPCION=>")
    if opcionMenu=="1":
        nombre=input("ingresa el nombre del coder=>")
        edad=int(input("ingresa la edad del coder=>"))
        riwipoints=int(input("ingresa los riwipoints del coder=>"))

        nuevoCoder={
            "nombre":nombre,
            "edad":edad,
            "riwipoints":riwipoints
        }

        coders.append(nuevoCoder)
    elif opcionMenu=="2":
        indice=0
        for coder in coders:
            #mostrar informacion de coders
            print(f"""
                id=[{indice}]
                Nombre={coder["nombre"]}
                Edad={coder["edad"]}
                Riwipoints={coder["riwipoints"]}
                """)
            indice+=1

        #pedimos los nuevos datos   
        coderParaActualizar=int(input("ingresa el id del coder que quieres actualizar=>"))
        nuevoNombre=input("ingresa el nuevo nombre del coder=>")
        nuevaEdad=int(input("ingresa la nueva edad del coder=>"))
        nuevosRiwipoints=int(input("ingresa los nuevos riwipoints del coder=>"))

        #actualizar los nuevos datos
        coders[coderParaActualizar]["nombre"]=nuevoNombre
        coders[coderParaActualizar]["edad"]=nuevaEdad
        coders[coderParaActualizar]["riwipoints"]=nuevosRiwipoints
    elif opcionMenu=="3":
        indice=0
        for coder in coders:
            print(f"id=[{indice}] - {coder["nombre"]}")
            indice+=1

        coderAeliminar=int(input("ingrese el ID del coder que quiere eliminar"))
        del coders[coderAeliminar]
    elif opcionMenu=="4":
        print("lista de coders")
        for coder in coders:
            print(f"""
                NOMBRE CODER= {coder["nombre"]}
                EDAD= {coder["edad"]}
                RIWIPOINTS= {coder["riwipoints"]}
                """)
    elif opcionMenu=="5":
        print("aca vamos a cerrar")
        break
    else:
       print("ingresastes una opcion invalidad")