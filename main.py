def show_menu():
    print("1. Add new note")
    print("2. Print notes")
    print("3. Save notes to file")
    print("4. Salir")

def add_note(notes):
    note = input("Write here: ")
    notes.append(note)

def print_note(notes):
    for note in notes:
        print(note)

def save_notes_to_file(notes):
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(note + "\n")
    print("Notes saved to notes.txt")

def main():
    notes = []
    while True:
        show_menu()
        option = input("Choose: ")
        if option == "1":
            add_note(notes)
        elif option == "2":
            print_note(notes)
        elif option == "3":
            save_notes_to_file(notes)
        elif option == "4":
            break
        else:
            print("Nope, try again")

if __name__ == "__main__":
    main()
