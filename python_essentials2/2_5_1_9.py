digit_of_life = input("Type your text: ")
temp_digit_of_life = 0


for a in digit_of_life:
    a = int(a)
    temp_digit_of_life += a

digit_of_life = temp_digit_of_life


while digit_of_life >= 10:
    temp_digit_of_life = 0
    digit_of_life = str(digit_of_life)
    for a in digit_of_life:
        a = int(a)
        temp_digit_of_life += a
    digit_of_life = temp_digit_of_life

print(digit_of_life)