# Programa de gestión de estudiantes con validaciones y menú
# Autor: ChatGPT (GPT-5)

def mostrar_menu():
    """La funcion es para mostrar unmenu interactivo para el cliente"""
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Agregar materia y calificación")
    print("4. Mostrar todos los estudiantes")
    print("5. Mostrar promedio de un estudiante")
    print("6. Salir")

def agregar_estudiante(estudiantes):
    """Se agregan estudiantes solo con nombre y edad """
    nombre = input("Ingrese el nombre del estudiante: ").strip().title()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    if nombre in estudiantes:
        print("Ese estudiante ya existe.")
        return
    try:
        edad = int(input("Ingrese la edad del estudiante: "))
        if edad <= 0:
            print("La edad debe ser un número positivo.")
            return
    except ValueError:
        print("Ingrese un número válido para la edad.")
        return

    estudiantes[nombre] = {"edad": edad, "materias": {}}
    print(f" Estudiante '{nombre}' agregado correctamente.")

def eliminar_estudiante(estudiantes):
    """Elimina alumnos y toda la informacion que tenga como nombre, edad, materias y calificaciones"""
    nombre = input("Ingrese el nombre del estudiante a eliminar: ").strip().title()
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f" Estudiante '{nombre}' eliminado correctamente.")
    else:
        print("Estudiante no encontrado.")

def agregar_materia(estudiantes):
    """Se agregan materias pidiendo el nombre del estudiante y guardando la informacion en el estudiante pedido, asi como calificaciones tambien en el caso que algo este mal o que haya algun dato erroneo despliega un mensaje de error"""
    nombre = input("Ingrese el nombre del estudiante: ").strip().title()
    if nombre not in estudiantes:
        print("Ese estudiante no existe.")
        return

    materia = input("Ingrese el nombre de la materia: ").strip().title()
    if materia == "":
        print("El nombre de la materia no puede estar vacío.")
        return
    try:
        calificacion = float(input("Ingrese la calificación (0-100): "))
        if not (0 <= calificacion <= 100):
            print("La calificación debe estar entre 0 y 100.")
            return
    except ValueError:
        print("Ingrese un número válido para la calificación.")
        return

    estudiantes[nombre]["materias"][materia] = calificacion
    print(f" Materia '{materia}' agregada con calificación {calificacion} a {nombre}.")

def mostrar_estudiantes(estudiantes):
    """Te da la informacion de los alumnos agrgados junto con sus materias y calificaciones"""
    if not estudiantes:
        print(" No hay estudiantes registrados.")
        return
    print("\n===== LISTA DE ESTUDIANTES =====")
    for nombre, datos in estudiantes.items():
        print(f"\n {nombre} - Edad: {datos['edad']}")
        if datos["materias"]:
            for materia, nota in datos["materias"].items():
                print(f" {materia}: {nota}")
        else:
            print("  Sin materias registradas.")

def promedio_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ").strip().title()
    if nombre not in estudiantes:
        print("Ese estudiante no existe.")
        return

    materias = estudiantes[nombre]["materias"]
    if not materias:
        print(" Ese estudiante no tiene materias registradas.")
        return

    promedio = sum(materias.values()) / len(materias)
    print(f" Promedio de {nombre}: {promedio:.2f}")

# Programa principal
def main(): 
    """funcionamiento para el menu por opciones numericas"""
    estudiantes = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            eliminar_estudiante(estudiantes)
        elif opcion == "3":
            agregar_materia(estudiantes)
        elif opcion == "4":
            mostrar_estudiantes(estudiantes)
        elif opcion == "5":
            promedio_estudiante(estudiantes)
        elif opcion == "6":
            print(" Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

