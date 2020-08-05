fname = input()
with open(fname, "r", encoding = "UTF-8") as f:
    cont = f.readlines()
    with open("trans/trans_" + fname, "w", encoding = "UTF-8") as tf:
        content = ""
        for i in cont:
            content += "\"" + i + "\","
        tf.write(content.replace("\n", "")[:-1])