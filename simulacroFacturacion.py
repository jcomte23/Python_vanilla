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



