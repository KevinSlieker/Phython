print('Hallo Wereld')

foo = (1,2,3)
foo.index(0)

angle = 0
for i in range(5):
    if i % 2 == 1:
        angle += 1
else:
    angle -= 1
print(angle)

a = 2
if a >= 2:
    print(a)

def combine(width, height=10, depth=0, is_3d=False):
    return [is_3d, width, height, depth]

print(combine(height = 1, width =2)[3])

data = [True, 3.12, -2]
print(data.index(data[0]) == 0)

print('A', 'B', sep='*', end='*')
print('C')

p = 1
while p <5:
    p += 1
    print("@", end="")
    if p == 3:
        break
else:
    print("@")

def p(d):
    d = [1,2,3]
    #return d[-2]

m = [0 for i in range(3)]
p(m)
print(m)