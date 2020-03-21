from math import acos, sin, cos, pi, sqrt, radians
from os import system

#================DISTANCE================

def distance_calc(coord1=[], coord2=[]):
    Radius = 6371.01  # constant
    parse_data = lambda coordinate : [radians(float(num)) for num in coordinate]

    if len(coord1)==0 or len(coord2)==0:
        coordinate1 = input("Enter point 1(latitude and longitude) in degrees:").split(",")
        coordinate2 = input("Enter point 2(latitude and longitude) in degrees:").split(",")
    else :
        coordinate1 = coord1
        coordinate2 = coord2

    x1, y1 = parse_data(coordinate1)
    x2, y2 = parse_data(coordinate2)

    distance = Radius * acos(sin(x1) * sin(x2) + cos(x1)
                             * cos(x2) * cos(y1 - y2))

    return distance

#==================AREA==================

def area(numA, numB, numC):
    S = (numA + numB + numC) / 2
    return sqrt(S * (S - numA) * (S - numB) * (S - numC))

# ==========Code for Question 2==========

def Q2():
    print("The distance between the two points is ",distance_calc(),"km")
    system("pause")
    
# ==========Code for Question 3==========

def Q3():
    list_of_Cities = [[35.2270, -80.8431], [32.0835, -81.0998], # Charlotte Savannah
                      [28.5336, -81.3867], [33.7569, -84.3903]] # Orlando   Atlanta

    dist_CS = distance_calc(list_of_Cities[0],list_of_Cities[1])
    dist_SO = distance_calc(list_of_Cities[1],list_of_Cities[2])
    dist_OA = distance_calc(list_of_Cities[2],list_of_Cities[3])
    dist_CA = distance_calc(list_of_Cities[0],list_of_Cities[3])
    dist_CO = distance_calc(list_of_Cities[0],list_of_Cities[2])

    Area = area(dist_CS, dist_SO, dist_CO) + area(dist_CO, dist_CA, dist_OA)

    print("The area is ", Area, "square kilometers")
    system("pause")

# ==========Code for Question 8==========

def Q8():
    coins = []
    coins_val = [50, 10, 5, 1]

    Money = int(input('Enter an amount as integer : '))
    print("Your amount",Money,"consists of")

    for val in coins_val:
        coins.append(Money // val)
        Money %= val

    print(coins[0],"fifty dollars\n",coins[1],"ten dollars\n",coins[2],
            "five dollars\n",coins[3],"one dollars")
    system("pause")

# =========Code for Question 11==========

def Q11():
    number = input("Enter an integer :")
    print("The reversed number is: ",number[::-1])
    system("pause")

# =================MAIN=================

Input = ''

while True:

    system("cls")
    Input = input('Question number(Q or q to quit):')
    
    if Input == '2':
        Q2()
    elif Input == '3':
        Q3()
    elif Input == '8':
        Q8()
    elif Input == '11':
        Q11()
    elif Input =='q'or Input == 'Q':
        break
    else:
        print('Wrong input')
