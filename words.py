def newkor():
    num = int(input("lines : "))

    with open("words/ENG.ini", "r", encoding="UTF-8") as f:
        cont = f.readlines()
        cont = cont[(num - 1):]
        with open("words/KOR.ini", "a", encoding="UTF-8") as ka:
            for i in cont:
                print(i.replace("\n", ""))
                print(">>>", end=" ")
                kor = input()
                if (kor == "break"):
                    break
                ka.write("\n" + kor)

def trans():
    with open("words/ENG.ini", "r", encoding="UTF-8") as f:
        cont = f.readlines()
        with open("words/trans/trans_" + "ENG.ini", "w", encoding="UTF-8") as tf:
            content = ""
            for i in cont:
                content += "\"" + i + "\","
            tf.write(content.replace("\n", "")[:-1])

    with open("words/KOR.ini", "r", encoding="UTF-8") as f:
        cont = f.readlines()
        with open("words/trans/trans_" + "KOR.ini", "w", encoding="UTF-8") as tf:
            content = ""
            for i in cont:
                content += "\"" + i + "\","
            tf.write(content.replace("\n", "")[:-1])

def edit():
    with open("jav.js", "r", encoding = "UTF-8") as j:
        jscon = j.readlines()
        with open("words/trans/trans_ENG.ini", "r", encoding = "UTF-8") as te:
            en = te.read()
            jscon[0] = ("var eng = [" + en + "];\n")
        with open("words/trans/trans_KOR.ini", "r", encoding = "UTF-8") as tk:
            ko = tk.read()
            jscon[1] = ("var kor = [" + ko + "];\n")
        with open("words/ENG.ini", "r", encoding = "UTF-8") as e:
            le = len(e.readlines())
        jscon[2] = "var max = " + str(le) + ";\n"
    with open("jav.js", "w", encoding = "UTF-8") as js:
        for i in jscon:
            js.write(i)

while True:
    cmd = input("(help)>>> ")
    if (cmd == "help"):
        print("newkor(한국어 입력), trans(trans로 변환), edit(자바스크립트 수정)")
    elif (cmd == "newkor"):
        newkor()
    elif (cmd == "trans"):
        trans()
    elif (cmd == "edit"):
        edit()
    elif (cmd == "exit"):
        break
    else:
        print("unknown command")

exit()