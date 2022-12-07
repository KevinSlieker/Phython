from os import strerror

srcname =  "python_essentials2\\" + "4_3_1_15.txt" #input("Enter the source file name: ")
try:
    src = open(srcname, 'rt')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

my_dict = {}

try:
    for a in src.read():
        if a.isalpha() == False:
            continue
        a = a.lower()
        if a not in my_dict:
            my_dict[a] = 1
        else:
            my_dict[a]+= 1
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
for b in my_dict.items():
    print(b[0], "->", b[1])
src.close()
