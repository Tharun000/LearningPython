# This program to split link and make an embed link

txt = "https://www.youtube.com/watch?v=7uE8g7vQ_jE"
x = txt.split("https://www.youtube.com/")
a = ["https://www.youtube.com/embed/"]

z = a + x


def listToString(z):
    string = ""

    for ele in z:
        string += ele

    return string


print(listToString(z))