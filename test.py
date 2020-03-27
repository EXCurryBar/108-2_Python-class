def Question():
    Question_List = [[1, 3, 5, 7, 9, 11, 13, 14, 17, 19, 21, 23, 25, 27, 29, 31],
                     [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31],
                     [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31],
                     [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31],
                     [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]]
    result = 0
    for Question_Num in range(len(Question_List)):
        print("Does your birthday in the list?\n", Question_List[Question_Num])
        ans = '?'
        while (ans != 'y' or ans != 'n'):
            ans = input("y/n :")
            if ans == 'y':
                result += 2**Question_Num
                break
            elif ans == 'n':
                break
            else:
                print('wrong input!')

    return result


print(Question())
