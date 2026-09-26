#SISTEMA DE CONTROL DE ASISTENCIA ESCOLAR - CBTIS 118
#Proyecto (Entrega Final)
import pdb
import time

# ==========================================
# CONFIGURACIÓN Y ARCHIVOS (.TXT)
# ==========================================

# Módulo de depuración PDB
modo_debug = False

# Archivos de texto externos para guardar la información
archivos_asistencia = [
    "asistencias_alumnos.txt",
    "retardos_alumnos.txt",
    "faltas_alumnos.txt",
    "reporte_general.txt",
]


# ==========================================
# FUNCIONES AUXILIARES
# ==========================================


def pantalla_carga(usuario):
  #Pantalla de carga dinámica
  print("\nIniciando Sistema de Control de Asistencia para:", usuario)
  for i in range(11):
    porcentaje = i * 10
    barra = "█" * i
    print(f"\rCargando datos: [{barra:<10}] {porcentaje}%", end="")
    time.sleep(0.4)  # 4.4 segundos totales
  print("\n¡Sistema Listo!\n")


def pedir_fecha():
  #Solicita la fecha y la guarda exactamente en la tupla: Fecha = dia, mes, anio.
  print("--- Registro de Fecha de Operación ---")

  while True:
    try:
      dia = int(input("Ingresa el día (1-31): "))
      if 1 <= dia <= 31:
        break
      print("Día no válido.\n")
    except ValueError:
      print("Error: Ingresa un número entero.\n")

  while True:
    try:
      mes = int(input("Ingresa el mes (1-12): "))
      if 1 <= mes <= 12:
        break
      print("Mes no válido.\n")
    except ValueError:
      print("Error: Ingresa un número entero.\n")

  while True:
    try:
      anio = int(input("Ingresa el año (2000-2100): "))
      if 2000 <= anio <= 2100:
        break
      print("Año no válido.\n")
    except ValueError:
      print("Error: Ingresa un número entero.\n")

  # Tupla exigida por la rúbrica
  Fecha = (dia, mes, anio)
  print(f"\nFecha registrada: {Fecha[0]}/{Fecha[1]}/{Fecha[2]}\n")
  return Fecha


def mostrar_menu_matriz():
  #Menú principal estructurado como una Matriz (lista de listas).
  matriz_menu = [
      ["1", "Registrar Asistencia / Retardo / Falta"],
      ["2", "Consultar reportes en archivos (.txt)"],
      ["3", "Anexar nota o justificante a un alumno"],
      ["4", "Salir del sistema"],
  ]

  print("\n===== MENÚ PRINCIPAL - CONTROL ESCOLAR =====")
  for fila in matriz_menu:
    print(f"[{fila[0]}] {fila[1]}")
  print("============================================\n")


# ==========================================
# MANEJO DE ARCHIVOS (.TXT) Y EXCEPCIONES
# ==========================================


def guardar_en_archivo(archivo, matricula, nombre, tipo, Fecha):
  #Guarda los datos del alumno en el archivo .txt con manejo de excepciones.
  try:
    with open(archivo, "a", encoding="utf-8") as f:
      f.write("=== REGISTRO DE ASISTENCIA CBTIS 118 ===\n")
      f.write(f"Matrícula: {matricula}\n")
      f.write(f"Alumno: {nombre}\n")
      f.write(f"Estado: {tipo}\n")
      f.write(f"Fecha: {Fecha[0]}/{Fecha[1]}/{Fecha[2]}\n")
      f.write("----------------------------------------\n\n")
    print(f"\n[OK] Registro guardado con éxito en '{archivo}'.\n")

  except PermissionError:
    print("\nError: Sin permisos para escribir en el archivo.\n")
  except FileNotFoundError:
    print("\nError: Archivo no encontrado.\n")
  except Exception as e:
    print(f"\nOcurrió un error inesperado: {e}\n")


def consultar_archivos():
  #Lee y muestra en pantalla los archivos .txt capturando excepciones.
  print("\nArchivos disponibles:")
  for idx, arch in enumerate(archivos_asistencia, 1):
    print(f"{idx}. {arch}")
  print()

  try:
    opcion = int(input("Selecciona el número de archivo a consultar: "))
    if opcion < 1 or opcion > len(archivos_asistencia):
      print("\nOpción fuera de rango.\n")
      return

    archivo_elegido = archivos_asistencia[opcion - 1]

    with open(archivo_elegido, "r", encoding="utf-8") as f:
      contenido = f.read()
      print(f"\n--- CONTENIDO DE: {archivo_elegido} ---")
      if contenido.strip() == "":
        print("El archivo está vacío actualmente.\n")
      else:
        print(contenido)

  except FileNotFoundError:
    print(
        "\nError (FileNotFoundError): El archivo seleccionado aún no existe en"
        " disco.\n"
    )
  except PermissionError:
    print("\nError: Permiso denegado para leer el archivo.\n")
  except ValueError:
    print("\nError: Ingresa un número entero válido.\n")
  except Exception as e:
    print(f"\nError al leer archivo: {e}\n")


def anexar_justificante(Fecha):
  #Anexa observaciones o justificantes a un archivo .txt.
  print("\nArchivos disponibles:")
  for idx, arch in enumerate(archivos_asistencia, 1):
    print(f"{idx}. {arch}")

  try:
    opcion = int(input("\nSelecciona el archivo para agregar la nota: "))
    if opcion < 1 or opcion > len(archivos_asistencia):
      print("\nOpción no válida.\n")
      return

    archivo_elegido = archivos_asistencia[opcion - 1]
    nota = input("Ingresa la observación o justificante: ")

    with open(archivo_elegido, "a", encoding="utf-8") as f:
      f.write("--- NOTA / JUSTIFICANTE ---\n")
      f.write(f"Observación: {nota}\n")
      f.write(f"Fecha: {Fecha[0]}/{Fecha[1]}/{Fecha[2]}\n")
      f.write("---------------------------\n\n")

    print("\n[OK] Nota anexada correctamente.\n")

  except Exception as e:
    print(f"\nError al anexar la información: {e}\n")


# ==========================================
# REGISTRO DE ASISTENCIA Y BUCLE PRINCIPAL
# ==========================================


def registrar_asistencia(Fecha):
  #Registra asistencias, retardos o faltas asignándolos a su archivo .txt.
  print("\n--- Captura de Registro ---")
  matricula = input("Ingresa la matrícula del alumno: ").strip()
  nombre = input("Ingresa el nombre del alumno: ").strip()

  print("\nSelecciona el tipo de evento:")
  print("1. Asistencia")
  print("2. Retardo")
  print("3. Falta")

  try:
    tipo_opcion = int(input("Opción: "))
  except ValueError:
    print("\nOpción inválida.\n")
    return

  if tipo_opcion == 1:
    tipo = "Asistencia"
    archivo = "asistencias_alumnos.txt"
  elif tipo_opcion == 2:
    tipo = "Retardo"
    archivo = "retardos_alumnos.txt"
  elif tipo_opcion == 3:
    tipo = "Falta"
    archivo = "faltas_alumnos.txt"
  else:
    print("\nOpción no válida.\n")
    return

  # Punto de depuración PDB
  if modo_debug:
    pdb.set_trace()

  # Guarda en el archivo específico y en el reporte general
  guardar_en_archivo(archivo, matricula, nombre, tipo, Fecha)
  guardar_en_archivo("reporte_general.txt", matricula, nombre, tipo, Fecha)


if __name__ == "__main__":
  while True:
    # 1. Identificación de Usuario
    usuario = input("Ingresa tu nombre o nickname (Docente/Prefecto): ")

    # 2. Bienvenida Dinámica con concatenación
    bienvenida = (
        "¡Bienvenido/a "
        + usuario
        + " al Sistema de Control Escolar del CBTis 118!"
    )
    print("\n" + bienvenida)

    # 3. Pantalla de carga
    pantalla_carga(usuario)

    # 6. Tupla de Fecha
    Fecha = pedir_fecha()

    cerrar_sesion = False

    while not cerrar_sesion:
      # 4. Menú en Matriz
      mostrar_menu_matriz()

      # 5. Control de Inactividad de 10 min (600 s) mediante ciclo FOR
      tiempo_inicio = time.time()
      opcion_menu = None

      for segundo in range(600):
        if time.time() - tiempo_inicio >= 600:
          print(
              "\n\n[INACTIVIDAD DETECTADA] Han transcurrido 10 minutos sin"
              " uso."
          )
          resp = (
              input("¿Deseas continuar en el sistema? (si/no): ")
              .strip()
              .lower()
          )
          if resp == "si":
            print("\nContinuando sesión...")
            tiempo_inicio = time.time()
          else:
            print("\nCerrando sesión actual...")
            cerrar_sesion = True
            break

      if cerrar_sesion:
        break

      try:
        opcion_menu = int(input("Selecciona una opción del menú: "))
      except ValueError:
        print("\nError: Ingresa un número válido.\n")
        continue

      if opcion_menu == 1:
        registrar_asistencia(Fecha)
      elif opcion_menu == 2:
        consultar_archivos()
      elif opcion_menu == 3:
        anexar_justificante(Fecha)
      elif opcion_menu == 4:
        print("\nCerrando sesión...\n")
        cerrar_sesion = True
      else:
        print("\nOpción no válida.\n")

    respuesta = (
        input("¿Deseas reiniciar la aplicación? (si/no): ").strip().lower()
    )
    if respuesta != "si":
      print("\nGracias por utilizar el sistema. ¡Hasta luego!\n")
      break