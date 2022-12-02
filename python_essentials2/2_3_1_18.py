def mysplit(strng):
    mylist = []
    temp = ""
    for ax in range(len(strng)):
        a = strng[ax]
        if a.isspace() and temp != '':
            mylist.append(temp)
            temp = ''
        if a.isspace() != True:
            temp += a
            if (' '.join(mylist)+" " +temp) == strng:
                mylist.append(temp)
    return mylist

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

