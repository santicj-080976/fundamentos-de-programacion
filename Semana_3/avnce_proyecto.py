# Sistema de Control de Asistencia Escolar

asistencias = 0
retardos = 0
faltas = 0

opcion = 0

while opcion != 5:

    print("\n===== CONTROL DE ASISTENCIA =====")
    print("1. Registrar asistencia")
    print("2. Registrar retardo")
    print("3. Registrar falta")
    print("4. Ver reporte")
    print("5. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        nombre = input("Nombre del alumno: ")
        asistencias += 1
        print("Asistencia registrada para", nombre)

    elif opcion == 2:
        nombre = input("Nombre del alumno: ")
        retardos += 1
        print("Retardo registrado para", nombre)

    elif opcion == 3:
        nombre = input("Nombre del alumno: ")
        faltas += 1
        print("Falta registrada para", nombre)

    elif opcion == 4:
        print("\n===== REPORTE GENERAL =====")
        print("Asistencias:", asistencias)
        print("Retardos:", retardos)
        print("Faltas:", faltas)

    elif opcion == 5:
        print("Sistema finalizado.")

    else:
        print("Opción no válida.")