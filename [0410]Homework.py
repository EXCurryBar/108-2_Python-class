from os import system

# ===================Code for Question 26=======================


def Q26():
    str1 = input("Enter a three digits integer :")
    if(str1 == str1[::-1]):
        print(str1, "is palindrome")
    else:
        print(str1, "is not palindrome")

# ===================Code for Question 27=======================


def Q27():
    def function(x, y): return 100*x - 200*y
    x, y = eval(input("Enter a point's x and y coordinates :"))
    if(function(x, y) > 0):
        print("The point is not in the triangle")
    elif(function(x, y) < 0):
        print("The point is in the triangle")
    else:
        print("The point is on the function")

# ===================Code for Question 33=======================


def Q33():
    dec = int(input("Enter a decimal value(0~15) :"))
    print("The hexadecimal value is", hex(dec)[2].capitalize())

# ===================Code for Question 34=======================


def Q34():
    Hex = input("Enter a hexadecimal value(0~F) :")
    if(Hex >= '0'and Hex <= '9' and len(Hex) == 1):
        print("The decimal value is", Hex)
    elif(Hex >= 'A' and Hex <= 'F'):
        print("The decimal value is", 10 + ord(Hex)-ord('A'))
    else:
        print("Wrong input")


while True:
    try:
        system("cls")
        Input = input('Question number(Q or q to quit):')

        if Input == '26':
            Q26()
            system("pause")
        elif Input == '27':
            Q27()
            system("pause")
        elif Input == '33':
            Q33()
            system("pause")
        elif Input == '34':
            Q34()
            system("pause")
        elif Input == 'q'or Input == 'Q':
            break
        else:
            print('Wrong input')
            system("pause")
    except KeyboardInterrupt:
        print('bye')
        break
