print('Hallo Wereld')

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return

print(fun(fun(2)) + 1)

print(17%-16)

# try:
#     print(5/0)
#     break
# except:
#     print(1)
# except (ZeroDivisionError):
#     print(2)

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1])

list = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if list[r][c] % 2 != 0:
            print("#")

print(1%3)

list = [i for i in range(-1,-1)]
print(len(list))

value = "0"
print(int(value)/len(value))

i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")

a = 'a'
print(9**3**0**1)

foo = (1,2,3)
foo.index(2)

num = 4, 
print(type(num))

