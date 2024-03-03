<h1 align="center">Tipos de variables</h1>

<p>Las variables son uno de los bloques de creación fundamentales de los programas escritos en Python. Las variables retienen los datos en la memoria.Python maneja principalmente estos tipos de datos</p>

<ul>
    <li>Numeros</li>
    <li>Textos</li>
    <li>Booleanos</li>
</ul>

<h2>Numeros (Numbers)</h2>

<p>La mayoría de los programas manipulan números. Los equipos tratan números enteros y números decimales de forma distinta. Tenga en cuenta el código siguiente:</p>

```bash
x = 1       # integer
x = 1.0     # decimal (floating point)
```
<h2>Textos,cadenas de caracteres (Strings)</h2>
<p>Las cadenas son, junto con los números, uno de los tipos de datos más usados. Una cadena es una colección de cero o más caracteres. Las cadenas se declaran normalmente mediante comillas simples, pero también puede utilizar comillas dobles:</p>

```bash
x = 'Esto es un string'
print(x) # outputs: Esto es un string
print(type(x)) # outputs: <class 'str'>
y = "Esto tambien es un string"
```

<p>Puede agregar cadena a otras cadenas (una operación que se conoce como "concatenación") con el mismo operador + que suma dos números:</p>

```bash
x = 'Hola' + ' ' + 'mundo!'
print(x) # outputs: Hola mundo!
```

<h2>Booleanos</h2>
<p>Otro tipo de datos habitual es el tipo booleano, que contiene el valor <strong>True</strong> o <strong>False</strong>;Internamente, bool se trata como un tipo especial de entero. Técnicamente, True tiene un valor de 1 y False tiene un valor de 0.

```bash
x = True
print(type(x)) # outputs: <class 'bool'>
```

Normalmente, los valores booleanos no se usan para realizar operaciones matemáticas, sino que se usan para tomar decisiones y realizar una bifurcación. No obstante, es interesante comprender la relación entre los tipos. Muchos tipos no son más que versiones especializadas de tipos más generales. Los enteros son un subconjunto de los números de punto flotante y los valores booleanos son un subconjunto de los enteros.</p>