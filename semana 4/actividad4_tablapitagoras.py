tabla = []

for fila in range(1, 11):
    fila_actual = []
    for columna in range(1, 11):
        resultado = 0
        for i in range(columna):
            resultado = resultado + fila
        fila_actual.append(resultado)
    tabla.append(fila_actual)


def imprimir_tabla(tabla):
    for fila_actual in tabla:
        for numero in fila_actual:
            print(numero, end="\t")
        print()

def consultar (tabla, fila, columna):
    return tabla[fila  -1  ][columna -1 ]

print("TABLA DE PITÁGORAS")
print()
imprimir_tabla(tabla)
print()

fila = int(input("Ingresa fila (valor): "))
columna = int(input("Ingresa columna (valor): "))

if 1 <= fila <= 10 and 1 <= columna <= 10:
    resultado = consultar (tabla, fila, columna)
    print(f"El resultado de {fila} x {columna} es: {resultado}")
else:
    print("Error: los valores deben estar entre 1 y 10.")