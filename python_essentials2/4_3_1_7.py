# from sys import path
# print(path)

from os import strerror

try:
    fo = open('python_essentials2\\newtext.txt', 'wt') # A new file (newtext.txt) is created.
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
        # s = "line #" + str(i+1) + "\n"
        # for ch in s:
        #     fo.write(ch)
    fo.close()
    fo = open('python_essentials2\\newtext.txt', 'rt')
    print(fo.read())
    fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))