import json
import os

# Guardar tareas.json en la misma carpeta que gestor.py
RUTA_CARPETA = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_TAREAS = os.path.join(RUTA_CARPETA, "tareas.json")

# Cargar tareas desde archivo
def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r") as f:
            return json.load(f)
    return []

# Guardar tareas en archivo
def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w") as f:
        json.dump(tareas, f, indent=4)

# Mostrar tareas
def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("\nTareas pendientes:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

# Menú principal
def main():
    tareas = cargar_tareas()
    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nueva_tarea = input("Ingrese la tarea: ")
            tareas.append(nueva_tarea)
            guardar_tareas(tareas)
            print("✅ Tarea agregada.")
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            listar_tareas(tareas)
            num = input("Ingrese el número de la tarea a eliminar: ")
            if num.isdigit() and 0 < int(num) <= len(tareas):
                tareas.pop(int(num) - 1)
                guardar_tareas(tareas)
                print("🗑️ Tarea eliminada.")
            else:
                print("❌ Número inválido.")
        elif opcion == "4":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
