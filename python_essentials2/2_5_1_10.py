text = input("Type your text: ")
text2 = input("Type your text2: ")

for a in text:
    found = text2.find(a)
    if found != -1:
        check = True
        continue
    else:
        check = False
        print("No")
        break

if check == True:
    print("yes")
    