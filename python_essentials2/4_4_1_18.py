import os
os.chdir("python_essentials2")
# os.makedirs("tree/c/other_courses/cpp")
# os.chdir("tree/c/other_courses")
# os.mkdir("python")
# os.chdir("../../")
# os.makedirs("cpp/other_courses/c")
# os.chdir("cpp/other_courses")
# os.mkdir("python")
# os.makedirs("../../python/other_courses/c")
# os.chdir("../../python/other_courses")
# os.mkdir("cpp")
# print(os.getcwd())

def find(path, dir):
    try:
        os.chdir(path)
    except OSError:
        return

    current_dir = os.getcwd()
    for file in os.listdir():
        if file == dir:
            print(current_dir + "\\" + file)
        find(current_dir + "\\" + file, dir)

find("./tree", "python")
