from os import strerror

srcname =  "python_essentials2\\" + "4_3_1_16.txt" #input("Enter the source file name: ")
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


sorted_my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
count = 0
for b in sorted_my_dict.items():
    print(b[0], "->", b[1])
    try:
        if count == 0:
            dst = open((srcname + ".hist"), 'wt')
            count += 1
        else:
            dst = open((srcname + ".hist"), 'at')
            count += 1
        dst.write(str(b[0] + " -> " + str(b[1]) + "\n"))
    except IOError as e:
        print("Cannot open the source file: ", strerror(e.errno))
        exit(e.errno)	  

src.close()
dst.close()