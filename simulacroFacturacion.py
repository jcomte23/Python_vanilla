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
            else:
                print("#############################")
                print("ingreste una opcion invalida")
                print("#############################")
    elif opcionMenu=="2":
        print("aca vamos a registrar un nuevo producto")
    elif opcionMenu=="3":
        print("aca vamos a listar los productos de la factura")
    elif opcionMenu=="4":
        print("aca vamos a mostrar la factura")
    elif opcionMenu=="5":
        print("Feliz dia")
        break
    else:
        print("#############################")
        print("ingreste una opcion invalida")
        print("#############################")


