import os
import uuid  # library untuk generate random id

clearScreen = lambda: os.system("cls")  # function untuk clear console


def main():  # function untuk menjalankan main program
    clearScreen()
    print("*******************TODO LIST*******************\n")

    printTodo()

    print(
        "\nOpsi:\n1. Add todo\n2. Delete todo\n3. Edit todo\n4. Clear all todo\n5. Mark todo as done\n6. Exit program\n"
    )
    option = int(input("Input opsi [1/2/3/4/5]: "))

    if option == 1:
        addTodo()
    elif option == 2:
        deleteTodo()
    elif option == 3:
        editTodo()
    elif option == 4:
        clearAllTodo()
    elif option == 5:
        markTodoAsDone()
    elif option == 6:
        exit(1)


def printTodo():  # function untuk print semua todo yang ada di file ke console
    if os.stat("todo.txt").st_size == 0:
        print("Belum ada todo.")
    else:
        file = open("todo.txt", "r")
        for i, element in enumerate(file):
            id, todo, jam, status = element.strip().split(",")
            if status == "done":
                text = str(i + 1) + ". " + todo + " (" + jam + ")"
                print("\u0336".join(text) + "\u0336  ✅")
            else:
                print(str(i + 1) + ". " + todo + " (" + jam + ")")
        file.close()


def addTodo():  # function untuk menambahkan todo baru
    clearScreen()
    print("*******************ADD TODO*******************\n")

    id = str(uuid.uuid4())
    todo = input("Masukkan todo: ")
    jam = input("Masukkan jam: ")
    status = "not-done"
    file = open("todo.txt", "a")
    file.write(id + "," + todo + "," + jam + "," + status + "\n")
    file.close()

    main()


def deleteTodo():  # function untuk memperbarui todo
    clearScreen()
    print("*******************DELETE TODO*******************\n")

    printTodo()

    deleteIdx = int(input("\nPilih nomor urut todo yang ingin dihapus: "))

    # main logic untuk delete
    file = open("todo.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("todo.txt", "w")
    for i, line in enumerate(lines):
        if i != deleteIdx - 1:
            file.write(line)
    file.close()

    main()


def editTodo():  # function untuk memperbarui todo
    clearScreen()
    print("*******************EDIT TODO*******************\n")

    printTodo()

    editIdx = int(input("\nPilih nomor urut todo yang ingin diedit: "))

    # menampilkan value todo dan jam saat ini (sebelum diedit)
    file = open("todo.txt", "r")
    for i, element in enumerate(file):
        if i == editIdx - 1:
            id, todo, jam, status = element.strip().split(",")
            print("\nTodo: " + todo + "\nJam: " + jam)
    file.close()

    # variabel untuk menampung input user
    newId = str(uuid.uuid4())
    newTodo = input("\nMasukkan todo yang baru: ")
    newJam = input("Masukkan jam yang baru: ")

    # main logic untuk edit
    file = open("todo.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("todo.txt", "w")
    for i, line in enumerate(lines):
        if i == editIdx - 1:
            file.write(newId + "," + newTodo + "," + newJam + ",not-done\n")
        else:
            file.write(line)
    file.close()

    main()


def clearAllTodo():  # function untuk menghapus semua todo
    with open("todo.txt", "w") as file:
        pass

    main()


def markTodoAsDone():  # function untuk menandai todo sebagai selesai
    clearScreen()
    print("*******************MARK TODO AS DONE*******************\n")

    printTodo()

    markDoneIdx = int(
        input("\nPilih nomor urut todo yang ingin ditandai sebagai selesai: ")
    )

    # main logic untuk mark as done
    file = open("todo.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("todo.txt", "w")
    for i, line in enumerate(lines):
        if i == markDoneIdx - 1:
            id, todo, jam, status = line.strip().split(",")
            file.write(id + "," + todo + "," + jam + ",done\n")
        else:
            file.write(line)
    file.close()

    main()


main()
