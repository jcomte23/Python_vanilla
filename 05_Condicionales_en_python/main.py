# ###################
# CONDICIONALES EN PYTHON
# ###################

# Condición básica (IF)
if 8 > 5:
    print("8 es mayor que 5")  # 8 es mayor que 5

# Condición normal (IF - ELSE)
helado = 'limon'
if helado == 'chocolate':
    print('Sí es un helado de chocolate')
else:
    print('No es un helado de chocolate')  # No es un helado de chocolate

# Condición avanzada (IF - ELIF - ELSE)
puntaje = -4
if puntaje == 0:
    print("El puntaje es neutro")
elif puntaje < 0:
    print(f"El puntaje es negativo {puntaje}")  # El puntaje es negativo -4
elif puntaje > 0:
    print(f"El puntaje es positivo {puntaje}")
else:
    print("El puntaje no está dentro de los parámetros")
