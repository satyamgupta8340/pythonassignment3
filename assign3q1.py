# 1.Write a Python function to find the Max of three numbers.


def findmax(num1,num2,num3):
    if num1>num2 and num1>num3:
        print('The max number is ',num1)
    elif num2>num1 and num2>num3:
        print('The max number is ',num2)
    else:
        print('The max number is ',num3)

findmax(10,50,30)