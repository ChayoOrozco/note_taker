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
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"notes_{timestamp}.txt"
    with open(filename, "w") as file:
        for note in notes:
            file.write(note + "\n")
    print(f"Notes saved to {filename}")

def main():
    notes = []
    while True:
        show_menu()
        option = input("Choose an option: ")
        if option == "1":
            add_note(notes)
        elif option == "3":
            save_notes_to_file(notes)
        elif option == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
