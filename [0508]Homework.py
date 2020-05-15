import random


def Sum(num): return sum([int(digit) for digit in num])


def Q2():
    number = input('Enter a number: ')
    print('The sum of digits for', number, 'is', Sum(number))


def Q4():
    print(input('Enter a integer: ')[::-1])


def Q5():
    num1, num2, num3 = input('Enter three number: ').split(',')
    def displaySortedNumbers(
        num1, num2, num3): return sorted([num1, num2, num3])
    print('The sorted numbers are: ', end='')
    [print(n, end=' ') for n in displaySortedNumbers(num1, num2, num3)]


def isPrime(n, k=128):
    for _ in range(k):
        a = random.randrange(1, n)
        if pow(a, n-1, n) != 1:
            return False
    return True


def Q24():
    prime_list = [2, 3]
    lim = 30800
    for i in range(5, lim, 2):
        if isPrime(i) and str(i) == str(i)[::-1]:
            prime_list.append(i)
    for i in range(len(prime_list)):
        if i % 10 == 0:
            print()
        print(str(prime_list[i]).rjust(8), end='')


def Q29():
    number = input('Enter a credit card number as long integer: ')
    oddSum = 0
    evenSum = 0
    for i in range(0, len(number)):
        if(i % 2 == 0):
            if((int(number[i])*2)//10 > 0):
                oddSum += int(number[i])*2-9
            else:
                oddSum += int(number[i])*2
        else:
            evenSum += int(number[i])
    if((oddSum+evenSum) % 10 == 0):
        print('The credit card %s is valid' % ''.join(map(str, number)))
    else:
        print('The credit card %s is invalid' % ''.join(map(str, number)))

from os import system
while True:
    try:
        system("cls")
        Input = input('Question number(Q or q to quit):')

        if Input == '2':
            Q2()
            system("pause")
        elif Input == '4':
            Q4()
            system("pause")
        elif Input == '5':
            Q5()
            system("pause")
        elif Input == '24':
            Q24()
            system("pause")
        elif Input == '29':
            Q29()
            system("pause")
        elif Input == 'q'or Input == 'Q':
            break
        else:
            print('Wrong input')
            system("pause")
    except KeyboardInterrupt:
        print('\nbye')
        break

