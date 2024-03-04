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

cliente={
    "documento":"27984521",
    "nombres":"Javier",
    "apellidos":"Cómbita Téllez",
}

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
    print("aca vamos a registrar un cliente")
elif opcionMenu=="2":
    print("aca vamos a registrar un nuevo producto")
elif opcionMenu=="3":
    print("aca vamos a listar los productos de la factura")
elif opcionMenu=="4":
    print("aca vamos a mostrar la factura")
elif opcionMenu=="5":
    print("aca vamos terminar el programa")
else:
    print("ingreste una opcion invalidad")


