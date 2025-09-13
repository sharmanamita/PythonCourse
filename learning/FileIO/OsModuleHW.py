import os


while True:
    print("Menu", "1.Create Directory", "2.Create file", "3.Delete file",
          "4.Delete Directory", "5.Rename File", "6.Rename Directory", "7.Show Contents", "8.Quit", sep="\n")
    choice = int(input("Select above:"))

    if choice == 1:
        dname = input("Directory name:")
        os.mkdir("./"+dname)
    elif choice == 2:
        fname = input("File name:")
        dname = input("Directory name:")
        path = "./"+dname+"/"+fname
        f = open(path, 'w')
        f.close()
        os.chdir("./"+dname)
        print(os.listdir())
    elif choice == 3:
        fname = input("File name:")
        dname = input("Directory name:")
        os.remove("./" + dname + "/" + fname)
    elif choice == 4:
        dname = input("Directory name:")
        os.rmdir("./" + dname)
    elif choice == 5:
        fname = input("Old File name:")
        dname = input("Directory name:")
        newname = input("New file name")
        os.rename("./" + dname + "/" + fname, "./" + dname + "/" + newname)
    elif choice == 6:
        dname = input("Old Directory name:")
        newname = input("New Directory name:")
        os.rename("./" + dname, "./" + newname,)
    elif choice == 7:
        # os.chdir("../")
        print(os.listdir("D:\\Python\\FileIO"))
    elif choice == 8:
        break