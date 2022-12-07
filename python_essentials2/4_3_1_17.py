from os import strerror

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


srcname =  "python_essentials2\\" + "4_3_1_17.txt" #input("Enter the source file name: ") "4_3_1_17.txt"
try:
    src = open(srcname, 'rt')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

my_dict = {}

line = 1
try:
    file = src.readlines()
    src.close()
    if len(file) == 0:
        raise FileEmpty
    for a in file:
        a = a.split()
        if len(a) != 3:
            a = " ".join(a)
            raise BadLine(line, a)
        b = " ".join(a[0:-1])
        try:
            if b not in my_dict:
                my_dict[b] = float(a[-1])
            else:
                my_dict[b] += float(a[-1])
            line += 1
        except ValueError:
            a = " ".join(a)
            raise BadLine(line, a)
    sorted_my_dict = dict(sorted(my_dict.items()))
    for b in sorted_my_dict.items():
        print(b[0], "->", b[1])

except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)
except BadLine as e:
    print("Bad line #" + str(e.line_number) + " in source file: " + e.line_string)
except FileEmpty:
    print("Error: File is empty")




