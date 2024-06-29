semana=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
nombres=["Maria","Fabiana","Paola", "Vanessa", "Nathaly", "Raulymar"]
estados=["Carabobo", "Amazonas", "Lara", "Portuguesa", "Monagas", "Margarita", "Falcon", "Guarico", "Tachira", "Trujillo"]
valDolar=[38.60, 38.20, 39.20, 40.60, 42.20, 40.00]

def imprimir_for(arreglo):
    for value in arreglo:
        print (value)

def imprimir_for_i(arreglo):
    for i in range (len(arreglo)):
        print(arreglo[i])

def mostrar(arreglo):
    i=0
    while i <len(arreglo):
        print(arreglo[i])
        i=i+1

def registrarw(arreglo):
    i=0
    while i<len(arreglo):
        print(f"Ingresa el dato de la posicion {i+1}")
        dato=input()
        arreglo[i]=dato
        i=i+1

def cargar(arreglo, msj):
    for i in range(len(arreglo)):
        print (f" {msj}a guardar en la posicion {i+1}")
        dato=input()
        arreglo [i]=dato

def det_mayor(arreglo):
    mayor=0
    for i in range(len(arreglo)):
        if arreglo[i]>mayor:
            mayor=arreglo[i]
        return mayor
#mostrar nombres
nombres=[""]*5
estados=["","","","","","",]

print (nombres)
print (estados)
cargar(nombres, "ingresar el nombre")
print()
cargar(estados,"nombre del estado")
mostrar(nombres)
print("Estados de Venezuela")
imprimir_for_i(estados)
precios=[0]*7
cargar(precios, "ingresa el precio")
mostrar (precios)
print()
precio_mayor=det_mayor(precios)
print(f"El precio mayor es {precio_mayor}")
print()