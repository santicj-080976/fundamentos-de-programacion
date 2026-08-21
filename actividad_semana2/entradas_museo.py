#Nombre:Carlos Sanyiago Cuellar Jimenez
#matricula: 05049845
#Fecha: 21/08/26
#precios
precio_de_menor_3años = 0
Precio_de_menor = 30
Precio_de_mayor = 45
#descuentos
Descuento_para_adulto_mayor= 0.12
Descuento_para_estudiante_y_profesor = 0.10
personas = int(input("¿Cual es la cantidad de personas? : "))
Total_de_todo = 0
for p in range (1, personas + 1):
    print(f"Persona {p}")
    edad_persona = int(input(f"dame la edad de las personas {p} : "))
    if edad_persona < 3:
        print("Menor de 3 años, entrada gratis.")
        continue

    elif edad_persona <= 17:
        precio = Precio_de_menor

    else:
        precio = Precio_de_mayor

    tipo= input("¿Que tipo de visitante eres? (adulto mayor , profesor , estudiante , otro)")
    if edad_persona >= 60 and tipo == "adulto mayor":
        descuento = precio * Descuento_para_adulto_mayor
        porcentaje = 12

    elif tipo == "profesor" or tipo == "estudiante":
        descuento = precio * Descuento_para_estudiante_y_profesor
        porcentaje = 10

    else:
        descuento = 0
        porcentaje = 0

    total = precio - descuento
    print(f"Precio : ${precio:.2f}")
    print(f"Descuento: {porcentaje:.2f}%")
    print(f"Monto del descuento: ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    Total_de_todo = Total_de_todo + total

   
   

print(f"Total general: ${Total_de_todo:.2f}")


