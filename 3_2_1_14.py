blocks = int(input("Enter the number of blocks: "))

last_row = 0
height = 0

while blocks > last_row:
    last_row+= 1
    blocks -= last_row
    height += 1

print("The height of the pyramid:", height)