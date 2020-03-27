from math import sqrt
from random import randint
from os import system
from time import sleep


def Q1():
    a, b, c = eval(input("Enter a,b,c :"))
    D = b**2 - 4*a*c
    def calcpos(a, b): return (-b + sqrt(D))/(2*a)
    def calcneg(a, b): return (-b - sqrt(D))/(2*a)
    if D > 0:
        print("The roots are ", "%2.5f" %
              calcpos(a, b), ',', "%2.5f" % calcneg(a, b))
    elif D == 0:
        print("The roots is", "%2.5f" % calcpos(a, b))
    else:
        print("The equation has no solution")
    sleep(3)


def Q3():
    a, b, c, d, e, f = eval(input("Enter a,b,c,d,e,f :"))
    D = a*d-b*c
    def x(e, d, b, f): return(e*d-b*f)/D
    def y(a, f, e, c): return(a*f-e*c)/D
    if D != 0:
        print("x is ", "%2.5f" %
              x(e, d, b, f), ', y is ', "%2.5f" % y(a, f, e, c))
    else:
        print("The equation has no solution")
    sleep(3)


def Q8():
    a, b, c = eval(input("Enter three integers :"))
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    print("The sorted numbers are ", a, b, c)
    sleep(3)


def Q15():
    Lottery = str(randint(100, 999))
    print(Lottery)
    User_Num = input("Enter your lottery pick(three digits) :")
    if Lottery == User_Num:
        print("Exact match : you win $10,000")
    elif sorted(Lottery) == sorted(User_Num):
        print("Match all digits : you win $3,000")
    elif set(Lottery).intersection(set(User_Num)):
        print("Match one digit : you win $1,000")
    else:
        print("Sorry, no match")
    sleep(3)


def Q17():
    cw = 0
    pw = 0
    du = 0
    for i in range(3):
        cmora = randint(1, 3)
        print(cmora)
        mora = int(input("scissor(1), rock(2), paper(3): "))

        group = [mora, cmora]
        if group == [2, 1] or group == [3, 2] or group == [1, 3]:
            print("player win")
            pw += 1
        elif group == [1, 2] or group == [2, 3] or group == [3, 1]:
            print("computer win")
            cw += 1
        else:
            print("It's a draw")
            du += 1
    if pw >= 2:
        print("You won")
    elif cw >= 2:
        print("you lose")
    else:
        print("Draw")
    sleep(3)


def Q24():
    list_of_number = ['Ace', '1', '2', '3', '4', '5',
                      '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    list_of_suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    print("The card you picked is ", list_of_number[randint(0, 12)],
          " of ", list_of_suit[randint(0, 3)])
    sleep(3)


Input = ''

while True:

    system("cls")
    Input = input('Question number(Q or q to quit):')

    if Input == '1':
        Q1()
    elif Input == '3':
        Q3()
    elif Input == '8':
        Q8()
    elif Input == '15':
        Q15()
    elif Input == '17':
        Q17()
    elif Input == '24':
        Q24()
    elif Input == 'q'or Input == 'Q':
        system("cls")
        break
    else:
        print('Wrong input')
        sleep(1.5)
