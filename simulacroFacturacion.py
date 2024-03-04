productos=(
    {
        "nombre":"pan",
        "valor":1000
    },
    {
        "nombre":"galleta",
        "valor":800
    },
    {
        "nombre":"arina",
        "valor":1500
    }
)

documentoCliente=""
nombreCliente=""
apellidoCliente=""
factura=[]

while True:
    print("#MENU#")
    menu="""
    (1) Registar cliente  
    (2) Registrar un nuevo producto a la factura  
    (3) Listar productos actuales de la factura.   
    (4) Mostrar factura   
    (5) Apagar el programa
    """
    print(menu)

    opcionMenu=input("INGRESE LA OPCION=>")

    if opcionMenu=="1":
        if(documentoCliente=="" or nombreCliente=="" or apellidoCliente==""):
            print("Vamos a registarte")
            documentoCliente=input("ingrese el # documento=>")
            nombreCliente=input("ingrese los nombres=>")
            apellidoCliente=input("ingrese los apellidos=>")
            print("Datos registrados")
            print("DOC:",documentoCliente)
            print("NOMBRES:",nombreCliente)
            print("APELLIDOS:",apellidoCliente)
        else:
            print("Ya hay un usuario registrado")
            print("DOC:",documentoCliente)
            print("NOMBRES:",nombreCliente)
            print("APELLIDOS:",apellidoCliente)
            print("Estas seguro que quieres actualizarlo?")
            respuesta=input("(1) si (2) no =>")
            if respuesta=="1":
                documentoCliente=input("ingrese el # documento=>")
                nombreCliente=input("ingrese los nombres=>")
                apellidoCliente=input("ingrese los apellidos=>")
                print("Datos registrados")
                print("DOC:",documentoCliente)
                print("NOMBRES:",nombreCliente)
                print("APELLIDOS:",apellidoCliente)
                print("Usuario actualizado")
    elif opcionMenu=="2":
        indice=0
        for producto in productos:
            print(f"[{indice}] {producto["nombre"]} {producto["valor"]}")
            indice+=1
        productoSeleccionado=int(input("ingrese el indice del producto que quieres agregar"))
        factura.append(productos[productoSeleccionado])
    elif opcionMenu=="3":
        print("productos en factura")
        for producto in factura:
            print(f"{producto["nombre"]} {producto["valor"]}")
    elif opcionMenu=="4":
        print("FACTURA")
        print("Datos registrados")
        print("DOC:",documentoCliente)
        print("NOMBRES:",nombreCliente)
        print("APELLIDOS:",apellidoCliente)
        for producto in factura:
            print(f"{producto["nombre"]} {producto["valor"]}")
    elif opcionMenu=="5":
        print("Feliz dia")
        break
    else:
        print("#############################")
        print("ingreste una opcion invalida")
        print("#############################")


