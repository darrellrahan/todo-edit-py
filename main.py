import os  # library untuk kebutuhan clear console

clearScreen = lambda: os.system("cls")

running = True

# dibuatkan while loop agar user dapat mengedit lebih dari 1 kali
while running:
    clearScreen()

    # print semua todo yang ada di file
    f = open("todo.txt", "r")
    for i, e in enumerate(f):
        id, todo, jam = e.strip().split(",")
        print(str(i + 1) + ". " + todo + " (" + jam + ")")
    f.close()

    editIdx = int(input("\nPilih nomor urut yang ingin diedit: "))

    # menampilkan value todo dan jam saat ini (sebelum diedit)
    f = open("todo.txt", "r")
    for i, e in enumerate(f):
        if i == editIdx - 1:
            id, todo, jam = e.strip().split(",")
            print("\nTodo: " + todo + "\nJam: " + jam)
    f.close()

    # variabel untuk menampung input user
    newId = 69420
    newTodo = input("\nMasukkan todo yang baru: ")
    newJam = input("Masukkan jam yang baru: ")

    # main logic untuk edit
    f = open("todo.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("todo.txt", "w")
    for i, line in enumerate(lines):
        if i == editIdx - 1:
            f.write(str(newId) + "," + newTodo + "," + newJam + "\n")
        else:
            f.write(line)
    f.close()

    # jika user memasukkan 'y', user dapat melanjutkan mengedit.
    # jika user memasukkan 'n', user selesai mengedit.
    opt = input("\n'y' untuk edit lagi 'n' untuk selesai: ")
    if opt == "y":
        running = True
    else:
        running = False

# setelah user selesai mengedit, print final todo yang ada di file
print("\nFinal Todo:")
f = open("todo.txt", "r")
for i, e in enumerate(f):
    id, todo, jam = e.strip().split(",")
    print(str(i + 1) + ". " + todo + " (" + jam + ")")
f.close()
print("\n")
