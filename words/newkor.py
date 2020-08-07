num = int(input("lines : "))

with open("ENG.ini", "r", encoding = "UTF-8") as f:
    cont = f.readlines()
    cont = cont[(num - 1):]
    with open("KOR.ini", "a", encoding = "UTF-8") as ka:
        for i in cont:
            print(i.replace("\n", ""))
            print(">>>" ,end = " ")
            kor = input()
            if (kor == "break"):
                break
            ka.write("\n" + kor)