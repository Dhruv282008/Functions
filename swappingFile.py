def swapFileData():
    name = input("Enter Your Name  : ")
    print("Hi "+name+" Let's play a DATA SWAPPING GAME")
    file1 = input("Enter the file1 to be swapped  : ")
    file2 = input("Enter the file2 to be swapped : ")
    with open(file1, "r")as a:
        file1data = a.read()
    with open(file2, "r")as b:
        file2data = b.read()

    with open(file1, "w")as a:
        a.write(file2data)
    with open(file2, "w")as b:
        b.write(file1data)

swapFileData()