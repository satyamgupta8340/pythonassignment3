# 5.Write a Python program to print the even numbers from a given list¶

l1=[10,8,7,6,5,4,3,2,1]
l2=[]
for i in l1:
    if i%2==0:
        l2.append(i)
print(l2)