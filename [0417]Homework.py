#from __future__ import print_function
def Q9():
    loan = 10000
    years_of_loan = 0
    for i in range(10):
        years_of_loan = years_of_loan + (i <= 3)*loan
        loan *= 1.05
        print("The", str(i+1).rjust(2), "years cost is:", "%2.1f" % loan)
    print("Total cost of study loans during 4 years:", years_of_loan)


def Q11():
    score = 0
    name = ""
    total_student = int(input("Enter the number of student: "))
    for _ in range(total_student):
        name_tmp = input("Enter the student's name: ")
        score_tmp = int(input("Enter the student's score: "))
        if score_tmp > score:
            score = score_tmp
            name = name_tmp
    print("Top score:\n", name, "'s score is", score)


def Q19():
    layers = int(input("Enter layers: "))
    for i in range(layers):
        print(' '.rjust(3)*(layers - i), end='')
        [print(str(i-j+1).rjust(3), end='') for j in range(i+1)]
        [print(str(j+2).rjust(3), end='') for j in range(i)]
        print()


def Q20():
    layers = int(input("Please enter a positive integer: "))
    print("Pattern A")
    for i in range(layers):
        [print(str(j+1).rjust(3), end='') for j in range(i+1)]
        print()
    print("Pattern B")
    for i in range(layers):
        [print(str(j+1).rjust(3), end='') for j in range(layers-i)]
        print()
    print("Pattern C")
    for i in range(layers):
        print(' '.rjust(3)*(layers - i - 1), end='')
        [print(str(i-j+1).rjust(3), end='') for j in range(i+1)]
        print()
    print("Pattern D")
    for i in range(layers):
        print(' '.rjust(3) * i, end='')
        [print(str(j+1).rjust(3), end='') for j in range(layers - i)]
        print()

from os import system
while True:
    try:
        system("cls")
        Input = input('Question number(Q or q to quit):')

        if Input == '9':
            Q9()
            system("pause")
        elif Input == '11':
            Q11()
            system("pause")
        elif Input == '19':
            Q19()
            system("pause")
        elif Input == '20':
            Q20()
            system("pause")
        elif Input == 'q'or Input == 'Q':
            break
        else:
            print('Wrong input')
            system("pause")
    except KeyboardInterrupt:
        print('\nbye')
        break
