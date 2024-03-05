usuario = []
# Nombre - precio - categoria
productos = [
    ["arroz lb", 4000, "comestibles"],
    ["azucar lb", 4500, "comestibles"],
    ["platano lb", 1000, "vegetales"],
    ["pollo lb", 6000, "carnes"],
    ["res lb", 7500, "carnes"],
    ["banano lb", 2000, "frutas"],
    ["pera lb", 3000, "frutas"],
    ["jabon en polvo lb", 4200, "limpieza"],
    ["tomate lb", 1500, "vegetales"],
    ["papa lb", 4000, "vegetales"]
]

carrito = []


print()
print("==" * 25)
print("||              Carrito de compras              ||")
print("==" * 25)
try:
    while True:
        print("-" * 50)
        print("                      MENU                      ")
        print("-" * 50)
        print()
        print("[1] Registrar usuario o actualizar datos usuario")
        print("[2] Agregar producto al carrito de compras")
        print("[3] Listar el carrito de compras")
        print("[4] Actualizar carrito de compras")
        print("[5] Eliminar producto en carrito de compras")
        print("[6] Finalizar programa")
        opcion = int(input("->"))
        if opcion == 1:
            print("-" * 50)
            if not usuario:
                nombre = input("Ingrese su nombre(s) =>")
                apellido = input("Ingrese su apellido(s) =>")
                documento = input("Ingrese su numero de documento=>")

                usuario.append(nombre)
                usuario.append(apellido)
                usuario.append(documento)

                print("Usuario registrado correctamente")
            else:
                print("El usuario ya esta registrado, si lo deseas puedes editarlo")
                print()
                nombre = input("Ingrese su nombre(s) =>")
                apellido = input("Ingrese su apellido(s) =>")
                documento = input("Ingrese su numero de documento=>")

                usuario[0] = nombre
                usuario[1] = apellido
                usuario[2] = documento

                print("Usuario actualizado correctamente")
        elif opcion == 2:
            print("-" * 50)
            print("Productos disponibles")
            print("-" * 50)
            cont = 0
            for i in productos:
                print(f"[{cont + 1}] {i[0]} - ({i[1]})")
                cont += 1
            producto = int(input("Ingrese el id del producto que quieres agregar =>"))
            producto = (producto - 1)
            print(f"    ¿Cuantas cantidades de '{productos[producto][0]}' quieres?")
            cantidad = int(input("(Ejm:7)-> "))
            producto_carrito = []
            producto_carrito.append(productos[producto][0])
            producto_carrito.append(productos[producto][1])
            producto_carrito.append(cantidad)
            producto_carrito.append((productos[producto][1] * cantidad))
            producto_carrito.append(productos[producto][2])
            carrito.append(producto_carrito)
            print()
            print("PRODUCTO AGREGADO AL CARRITO")
            print()
        elif opcion == 3:
            print("-" * 50)
            if not carrito:
                print("El carrito esta vacio")
            else:
                print("-" * 35)
                print("carrito actual")
                print("-" * 35)
                subtotal = 0
                for i in carrito:
                    print(f"{i[0]}({i[1]}) * {i[2]} = {i[3]}")
                    subtotal += i[3]
                print("-" * 35)
                iva = subtotal * 0.19
                total = (subtotal + iva)

                print("SUBTOTAL =", subtotal)
                print("IVA 19% =", iva)
                print("TOTAL =", total)
                print("-" * 35)
        elif opcion == 4:
            print("-" * 50)
            if not carrito:
                print("El carrito esta vacio")
            else:
                print("Carrito")
                cont = 0
                for i in carrito:
                    print(f"[{cont + 1}] {i[0]}({i[1]}) * {i[2]} = {i[3]}")
                    cont += 1
                producto = int(input("Ingrese el id del producto que quieres actualizar =>"))
                producto = (producto - 1)
                cantidad_nueva = int(input(f"    ¿Cuantas cantidades de '{carrito[producto][0]}' quieres? =>"))
                carrito[producto][2] = cantidad_nueva
                carrito[producto][3] = (carrito[producto][3] * cantidad_nueva)
                print()
                print("PRODUCTO ACTUALIZADO CORRECTAMENTE")
                print()
        elif opcion == 5:
            print("-" * 50)
            if not carrito:
                print("El carrito esta vacio")
            else:
                print("Carrito")
                cont = 0
                for i in carrito:
                    print(f"[{cont + 1}] {i[0]}({i[1]}) * {i[2]} = {i[3]}")
                    cont += 1
                producto = int(input("Ingrese el id del producto que quieres eliminar =>"))
                producto = (producto - 1)
                del carrito[producto]
                print()
                print("PRODUCTO ELIMINADO CORRECTAMENTE")
                print()
        elif opcion == 6:
            print("Fue un gusto atenderte")
            exit()
        else:
            print("la opcion no esta dentro del menu")
except ValueError:
    print("Ingresaste un valor invalido")
