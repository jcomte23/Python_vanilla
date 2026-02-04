texto=input("ingresa un texto cualquiera=>").lower()

letras=list()
print("ingresa 3 letras a tu elección:")
letras.append(input("ingresa la primer letra a tu elección=>").lower())
letras.append(input("ingresa la segunda letra a tu elección=>").lower())
letras.append(input("ingresa la tercer letra a tu elección=>").lower())

print(f"la letra {letras[0]} aparece {texto.count(letras[0])} veces")
print(f"la letra {letras[1]} aparece {texto.count(letras[1])} veces")
print(f"la letra {letras[2]} aparece {texto.count(letras[2])} veces")

cantidad_de_palabras=texto.split()
print(f"en el el texto hay {len(cantidad_de_palabras)} palabras")

primer_letra=texto[0]
ultima_letra=texto[-1]
print(f"la primer letra es: {primer_letra}")
print(f"la ultima letra es: {ultima_letra}")
print(f"el texto invertido es: {cantidad_de_palabras[::-1]}")

if "python" in texto:
    print(f"python esta en el texto")
else:
    print(f"python no esta en el texto")