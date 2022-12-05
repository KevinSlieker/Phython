text = input("Type your text: ")
temp_text = []


for a in text:
    if not a.isalpha():
        continue
    a = a.lower()
    temp_text += a

for n in range((len(temp_text)//2)):
    if temp_text[n] != temp_text[-n-1]:
        check = False
        break
    check = True

if check == True:
    print("It's a palindrome")
if check == False:
    print("It's not a palindrome")
        