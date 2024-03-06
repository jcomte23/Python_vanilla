pacientes=[
    {
        "nombre":"kronos",
        "raza":"criollo",
        "edad":2,
        "identificacionDueño":"3935353",
        "estado":False
    },
    {
        "nombre":"lucas",
        "raza":"criollo",
        "edad":2,
        "identificacionDueño":"3935353",
        "estado":True
    },
    {
        "nombre":"mateo",
        "raza":"criollo",
        "edad":2,
        "identificacionDueño":"3935353",
        "estado":False
    },
]

while True:
    print("Veterinaria Daly")
    print("""
MENU
(1) registrar un nuevo paciente

(2) actualizar un  paciente

(3) listar pacientes activos

(4) listar pacientes inactivos
        
(5) listar todos los pacientes

(6) cerrar programa
    """)

    opcionMenu=input("INGRESA LA OPCION=>")
    if opcionMenu=="1":
        nombre=input("ingresa el nombre del paciente=>")
        raza=int(input("ingresa la raza del paciente=>"))
        edad=int(input("ingresa la edad del paciente=>"))
        identificacion=int(input("ingresa el # de identificacion del dueño del paciente=>"))
        estado=int(input("ingresa el estado del paciente, 'True' si esta en la vetarinaria o 'False' si ya salio de la veterinaria"))

        nuevoPaciente={
            "nombre":nombre,
            "raza":raza,
            "edad":2,
            "identificacionDueño":identificacion,
            "estado":False
        },

        pacientes.append(nuevoPaciente)
    elif opcionMenu=="2":
        indice=0
        print("PACIENTES")
        for paciente in pacientes: 
            #mostrar informacion de pacientes
            print(f"""
                id=[{indice}]
                Nombre={paciente["nombre"]}
                Raza={paciente["raza"]}
                Edad={paciente["edad"]}
                Identificacion Dueño={paciente["identificacionDueño"]}
                Estado={paciente["estado"]}
                """)
            indice+=1

        #pedimos los nuevos datos   
        pacienteParaActualizar=int(input("ingresa el id del paciente que quieres actualizar=>"))
        nuevoNombre=input("ingresa el nombre del paciente=>")
        nuevaRaza=int(input("ingresa la raza del paciente=>"))
        nuevaEdad=int(input("ingresa la edad del paciente=>"))
        nuevaIdentificacion=int(input("ingresa el # de identificacion del dueño del paciente=>"))
        nuevoEstado=int(input("ingresa el estado del paciente, 'True' si esta en la vetarinaria o 'False' si ya salio de la veterinaria"))

        #actualizar los nuevos datos
        pacientes[pacienteParaActualizar]["nombre"]=nuevoNombre
        pacientes[pacienteParaActualizar]["raza"]=nuevaRaza
        pacientes[pacienteParaActualizar]["edad"]=nuevaEdad
        pacientes[pacienteParaActualizar]["identificacionDueño"]=nuevaIdentificacion
        pacientes[pacienteParaActualizar]["estado"]=nuevoEstado
    elif opcionMenu=="3":
        indice=0
        print("PACIENTES ACTIVOS")
        for paciente in pacientes:
            if paciente["estado"]==True:
                print(f"""
                    id=[{indice}]
                    Nombre={paciente["nombre"]}
                    Raza={paciente["raza"]}
                    Edad={paciente["edad"]}
                    Identificacion Dueño={paciente["identificacionDueño"]}
                    Estado={paciente["estado"]}
                    """)
                indice+=1
    elif opcionMenu=="4":
            indice=0
            print("PACIENTES INACTIVOS")
            for paciente in pacientes:
                if paciente["estado"]==False:
                    print(f"""
                        id=[{indice}]
                        Nombre={paciente["nombre"]}
                        Raza={paciente["raza"]}
                        Edad={paciente["edad"]}
                        Identificacion Dueño={paciente["identificacionDueño"]}
                        Estado={paciente["estado"]}
                        """)
                    indice+=1
    elif opcionMenu=="5":
        indice=0
        print("PACIENTES")
        for paciente in pacientes:
            if paciente["estado"]==False:
                print(f"""
                    id=[{indice}]
                    Nombre={paciente["nombre"]}
                    Raza={paciente["raza"]}
                    Edad={paciente["edad"]}
                    Identificacion Dueño={paciente["identificacionDueño"]}
                    Estado={paciente["estado"]}
                    """)
                indice+=1
    elif opcionMenu=="6":
        print("adios")
        break
    else:
       print("ingresastes una opcion invalida")