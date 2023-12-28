#Cheating and taking notes
def show_menu():
    print("1.Add new note")
    print("2. Print notes")
    print("3.Salir")
def add_note(notes):
    note = input("Write here")
    notes.append(note)
def print_note(notes):
    for note in notes:
        print(note)
def main():
    notes = []
    while True:
        show_menu()
        option = input ("Choose")
        if option == "1":
            add_note(notes)
        elif option == "2":
            print_note(notes)
        elif option == "3":
            break
        else:
            print("Nope, try again")
if __name__ == "__main__":
    main()
