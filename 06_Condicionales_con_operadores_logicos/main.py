print("")
print("#"*18)
print("OPERADORES VISTOS")
print("#"*18)
print("relacionales (>, <, >=, <= , ==, !=)")
print("matemáticos (+, -, *, /, //, **, %)")
print("")

print("")
print("#"*18)
print("OPERADORES LOGICOS")
print("#"*18)
print("lógicos (and, or y not)")
print("Estos operadores se emplean fundamentalmente en las estructuras condicionales para agrupar varias condiciones simples")
print("")

condicion1=True
condicion2=False


if(condicion1==True and condicion2==True):
    print("PRIMER BANDERA")

if(condicion1==True or condicion2==True):
    print("SEGUNDA BANDERA")

if(not condicion1==False):
    print("TERCERA BANDERA")

# EJEMPLO AND
usuario=input("Usuario =>")
contraseña=input("Contraseña =>")

if(usuario=="admin" and contraseña=="12345"):
    print("login exitoso")
else:
    print("login erroneo")

# EJEMPLO OR
print("validar si un mes esta en el primer trimestre del año")
mes=input("Mes =>")
if mes=="enero" or mes=="febrero" or mes=="marzo":
    print("Corresponde al primer trimestre")

