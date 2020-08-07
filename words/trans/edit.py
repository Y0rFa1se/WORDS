def edit():
    with open("../../jav.js", "r", encoding = "UTF-8") as j:
        jscon = j.readlines()
        with open("trans_ENG.ini", "r", encoding = "UTF-8") as te:
            en = te.read()
            jscon[0] = ("var eng = [" + en + "];\n")
        with open("trans_KOR.ini", "r", encoding = "UTF-8") as tk:
            ko = tk.read()
            jscon[1] = ("var kor = [" + ko + "];\n")
        with open("../ENG.ini", "r", encoding = "UTF-8") as e:
            le = len(e.readlines())
        jscon[2] = "var max = " + str(le) + ";\n"
    with open("../../jav.js", "w", encoding = "UTF-8") as js:
        for i in jscon:
            js.write(i)

edit()