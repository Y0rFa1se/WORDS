with open("ENG.ini", "r", encoding = "UTF-8") as f:
    cont = f.readlines()
    with open("trans/trans_" + "ENG.ini", "w", encoding = "UTF-8") as tf:
        content = ""
        for i in cont:
            content += "\"" + i + "\","
        tf.write(content.replace("\n", "")[:-1])

with open("KOR.ini", "r", encoding = "UTF-8") as f:
    cont = f.readlines()
    with open("trans/trans_" + "KOR.ini", "w", encoding = "UTF-8") as tf:
        content = ""
        for i in cont:
            content += "\"" + i + "\","
        tf.write(content.replace("\n", "")[:-1])