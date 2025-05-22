import numpy as np

matrix = np.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
])

for i in matrix:
    print(i)


def checker2():
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row,col] == 2

def put_2():
    print("Enter the desired postion to put 2: ")
    r = int(input("Enter the row"))
    c = int(input("Enter the col"))
    matrix[r,c] = 2

    for i in matrix:
        print(i)

def put_3():
    print("Enter the desired postion to put 3: ")
    r = int(input("Enter the row"))
    c = int(input("Enter the col"))
    matrix[r,c] = 3

    for i in matrix:
        print(i)


i = 1
while i <=9:
    if i in [1,3,5,7,9]:
        put_2()
        if checker2() == True:
            break
        i+=1

    else:
        put_3()
        if checker3() == True:
            break
        i+=1


if checker2() == True:
    print("Player 1 won !!")
if checker3() == True:
    print("PLayer 2 won !")
else:
    print("Draw")