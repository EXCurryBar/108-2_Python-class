from random import randint
def Q3():
    nums = sorted([int(num) for num in input("Enter the integers between 1 and 100: ").split(' ')])
    nums.append(None)
    count = 1
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            count+=1
            continue
        print(nums[i],'occurs',count,'times')
        count = 1


def Q5():
    nums = [int(num) for num in input("Enter the number: ").split(' ')]
    nums.append(None)
    res_lst = []
    for i in range(len(nums)-1):
        if nums[i] in res_lst:
            continue
        res_lst.append(nums[i])
    print("The distinct number are", res_lst)


def Q7():
    nums = sorted([randint(0,9) for _ in range(1000)])
    nums.append(None)
    count = 1
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            count+=1
            continue
        print(nums[i],'number',count)
        count = 1


def Q8():
    indexOfSmallestElement = lambda lst :print("The index of the smallest element is", lst.index(min(lst)))
    indexOfGreatestElement = lambda lst :print("The index of the greatest element is", lst.index(max(lst)))
    nums = [int(num) for num in input("Enter list element seperated by spaces from one line: ").split(' ')]
    indexOfSmallestElement(nums)
    indexOfGreatestElement(nums)


def Q13():
    nums = [int(num) for num in input("Enter ten number: ").split(' ')]
    nums.append(None)
    def eliminateDuplicates(lst):
        res_lst = []
        for i in range(len(nums)-1):
            if nums[i] in res_lst:
                continue
            res_lst.append(nums[i])
        return res_lst
    print("The distinct numbers are", eliminateDuplicates(nums))


from os import system
while True:
    try:
        system("cls")
        Input = input('Question number(Q or q to quit):')

        if Input == '3':
            Q3()
            system("pause")
        elif Input == '5':
            Q5()
            system("pause")
        elif Input == '7':
            Q7()
            system("pause")
        elif Input == '8':
            Q8()
            system("pause")
        elif Input == '13':
            Q13()
            system("pause")
        elif Input == 'q'or Input == 'Q':
            break
        else:
            print('Wrong input')
            system("pause")
    except KeyboardInterrupt:
        print('\nbye')
        break
