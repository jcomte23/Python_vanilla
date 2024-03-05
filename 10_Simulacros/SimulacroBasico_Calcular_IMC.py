print()
print("="*46)
print("||Calculador de IMC(indice de masa muscular)||")
print("="*46)

nombre = input("Nombre por favor =>").title().strip()
peso = float(input("Peso en kg (Ejm:74)=>"))
estatura = round(float(input("Estatura en m (Ejm:1.80) => ")), 2)

IMC = peso/(estatura*estatura)
IMC = round(IMC, 2)
print()
if IMC < 18.5:
    print(f"{nombre} tu indice de mas muscular es de {IMC} por lo tanto estas 'bajo de peso'")
elif IMC >= 18.5 and IMC <= 24.9:
    print(f"{nombre} tu indice de mas muscular es de {IMC} por lo tanto estas 'normal'")
elif IMC >= 25 and IMC <= 29.9:
    print(f"{nombre} tu indice de mas muscular es de {IMC} por lo tanto estas con 'sobrepeso'")
elif IMC >= 30 and IMC <= 34.9:
    print(f"{nombre} IMC(indice de mas muscular es de {IMC} por lo tanto estas con 'obesidad I'")
elif IMC >= 35 and IMC <= 39.9:
    print(f"{nombre} IMC(indice de mas muscular es de {IMC} por lo tanto estas con 'obesidad II'")
elif IMC >= 40 and IMC <= 49.9:
    print(f"{nombre} IMC(indice de mas muscular es de {IMC} por lo tanto estas con 'obesidad III'")
elif IMC >= 50:
    print(f"{nombre} IMC(indice de mas muscular es de {IMC} por lo tanto estas con 'obesidad IV'")


 
    