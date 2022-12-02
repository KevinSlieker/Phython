text = input("Enter your message: ")
shift_size = input("Enter non-negative integer Shift size: ")
while shift_size.isdigit() == False:
    shift_size = input("Shift size must be an integer number: ")
shift_size = int(shift_size)
while shift_size <1 or shift_size > 25:
    shift_size = input("Enter integer Shift size from 1 to 25: ")
    while shift_size.isdigit() == False:
        shift_size = input("Shift size must be an non-negative integer number: ")
    shift_size = int(shift_size)
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    code = ord(char) + shift_size
    if char.isupper() and code > ord('Z'):
        code = ord('A') + (code - ord('Z')-1)
    if char.islower() and code > ord('z'):
        code = ord('a') + (code - ord('z')-1)
    cipher += chr(code)

print(cipher)