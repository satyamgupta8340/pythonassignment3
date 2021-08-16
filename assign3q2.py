# 2.Write a Python function to multiply all the numbers in a list¶

def multiplynum(num):  
    r= 1
    for i in num:
        r=r*i  
    return r  
print(multiplynum)
multiplynum([2,2,2,4])