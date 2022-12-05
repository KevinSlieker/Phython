text = input("Type your text: ")
text2 = input("Type your text2: ")
temp_text = []
temp_text2 = []

for a in text:
    if not a.isalpha():
        continue
    a = a.lower()
    temp_text += a

for b in text2:
    if not b.isalpha():
        continue
    b = b.lower()
    temp_text2 += b

temp_text.sort()
temp_text2.sort()

if temp_text == temp_text2:
    print("Anagrams")
else:
    print("Not anagrams")