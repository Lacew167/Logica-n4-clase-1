nombres=("Mariana","Camila","Maria","Anastasia", "Jenny",)
print(nombres)
print("Ingresa la posicion que deseas conocer")
posi=int(input())
if posi>=0 and posi<=len(nombres):
    print(nombres[posi-1])
else:
    print(f"indice fuera de rango, el tamano es {len(nombres)}")
    