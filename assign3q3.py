# 3.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
def findnum(string):
    r={'u_case':0, 'l_case':0}
    for i in string:
    
        if i.isupper():
            r['u_case']+=1
        elif i.islower():
             r['l_case']+=1
        else:
            pass
    print ("Your entered String : ", string)
    print('The no of UPPER CASE ',r['u_case'])
    print('The no of lowe case ',r['l_case'])

findnum('ArmaAsssn')