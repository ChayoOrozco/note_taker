import os
from datetime import datetime

def show_menu():
    print("1. Agregar Nota")
    print("2. Crear nuevo archivo")
    print("3. Salir")

def add_note(notes):
    note = input("Escribe aqui " + "\n" )
    notes.append(note)
    print("Guardado.")

def save_notes_to_file(notes):
    timestamp = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    filename = f"notes_{timestamp}.txt"
    filepath = os.path.join(os.getcwd(), filename)
    with open(filepath, "w") as file:
        for note in notes:
            file.write(note + "\n")
    print(f"Notes saved to {filepath}")

def main():
    notes = []
    while True:
        show_menu()
        option = input("Escribe tu eleccion: ")
        if option == "1":
            add_note(notes)
        elif option == "2":
            save_notes_to_file(notes)
        elif option == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
