estudiantes =[]

def agrgegar_estudiante(nombre,edad, calificaciones):
    estuante = {
            "nombre": nombre,
            "edad": edad,
            "calificaciones": calificaciones

    }
    estudiantes.append(estudiante)
    print(f"Estudiante'{nombre}' agregado correctamente.")

def eliminar_estudiante(nombre):
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            estudiante.remove(estudiante)
            print(f"Estudiante'{nombre}' eliminado.")
            return
    print(f"no se encontro al estudiante con nombre '{nombre}'.")


def calcular_promedio(nombre):
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            calificaciones = [materia["calificacion"] for materia in estudiante["calificaciones"]]
            print(f"Promedio de {nombre}: {promedio:.2f}")
            return promedio
    print(f"no se encontro al estudiante con nombre '{nombre}'.")
    return None
