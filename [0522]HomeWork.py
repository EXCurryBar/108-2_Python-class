from os import system
import os.path
import sys

keyWords = {"and", "as", "assert", "break", "class",
            "continue", "def", "del", "elif", "else",
            "except", "False", "finally", "for", "from",
            "global", "if", "import", "in", "is", "lambda",
            "None", "nonlocal", "not", "or", "pass", "raise",
            "return", "True", "try", "while", "with", "yield"}


def readShit(filename):
    if not os.path.isfile(filename):
        print("File", filename, "does not exist")
        sys.exit()
    infile = open(filename, "r", encoding='UTF-8')
    text = infile.read().split()
    return text


def Q1():
    text = readShit(input("Enter a Python source code filename: "))
    print("The Key words are")
    [print(word,end=' ') for word in text if word in keyWords]


def Q2():
    Num = [int(num) for num in input("Enter the numbers: ").split(' ')]
    count = [[x, Num.count(x)]for x in set(Num)]
    Max = 0
    occ_lst = []
    for s in count:
        if s[1] > Max:
            Max = s[1]
            occ_lst.clear()
            occ_lst.append(s[0])
        elif s[1] == Max:
            occ_lst.append(s[0])
    print("The number with the most occurrence are", end=' ')
    [print(i, end=' ') for i in occ_lst]


def Q3():
    occ_lst = [word for word in readShit(input("Enter a Python source code filename: ")) if word in keyWords]
    print([[x, occ_lst.count(x)]for x in set(occ_lst)])


def Q8():
    [print(x, end=' ')for x in sorted(set(readShit(input("Enter a txt file: "))))]


while True:
    try:
        system("cls")
        Input = input('Question number(Q or q to quit):')

        if Input == '3':
            Q3()
            system("pause")
        elif Input == '1':
            Q1()
            system("pause")
        elif Input == '2':
            Q2()
            system("pause")
        elif Input == '8':
            Q8()
            system("pause")
        elif Input == 'q'or Input == 'Q':
            break
        else:
            print('Wrong input')
            system("pause")
    except KeyboardInterrupt:
        print('\nbye')
        break
