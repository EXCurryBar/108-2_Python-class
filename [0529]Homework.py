import os
import sys
from numpy import mean
from random import randint, choice


def readShit(filename):
    if not os.path.isfile(filename):
        print("File", filename, "does not exist")
        sys.exit()
    infile = open(filename, "r", encoding='UTF-8')
    text = infile.read()
    return text


def writeShit(filename, shit):
    with open(filename, 'w', encoding='UTF-8') as infile:
        infile.write(shit)


def Q3():
    score = [int(num) for num in readShit(input("Enter a filename: ")).split()]
    print("There are", len(score), "scores\nThe total is",
          sum(score), "\nThe average is", "%.3f" % mean(score))


def Q4():
    text = input('Enter a filename: ')
    writeShit(text, " ".join(str(x)for x in [randint(0, 999) for _ in range(100)]))
    num_lst = sorted([int(n) for n in readShit(text).split()])
    for i in range(len(num_lst)):
        if (i+1) % 10 != 0:
            print(str(num_lst[i]).rjust(5), end='')
        else:
            print(str(num_lst[i]).rjust(5))


def Q5():
    text = input('Enter a filename: ')
    old = input('Enter the old string to be replaced: ')
    new = input('Enter the new string to replace the old string: ')
    writeShit(text, readShit(text).replace(old, new))


def Q16():
    lst = [['Full', 7500000, 13000000], ['Associate',6000000, 11000000], ['Assistant', 5000000, 8000000]]
    s = ''
    for i in range(1000):
        work = choice(lst)
        s += "Firstname"+str(i+1).ljust(4)+" Lastname"+str(i+1).ljust(4) + \
            ' '+work[0].rjust(9)+' '+str(randint(work[1], work[2])/100)+'\n'
    writeShit('Salary.txt', s)


while True:
    try:
        os.system("cls")
        Input = input('Question number(Q or q to quit):')

        if Input == '3':
            Q3()
            os.system("pause")
        elif Input == '4':
            Q4()
            os.system("pause")
        elif Input == '5':
            Q5()
            os.system("pause")
        elif Input == '16':
            Q16()
            os.system("pause")
        elif Input == 'q'or Input == 'Q':
            break
        else:
            print('Wrong input')
            os.system("pause")
    except KeyboardInterrupt:
        print('\nbye')
        break
