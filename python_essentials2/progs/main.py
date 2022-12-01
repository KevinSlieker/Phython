from sys import path

path.append('c:\\Bitnami\\wampstack-8.1.9-0\\apache2\\htdocs\\educom-python\python_essentials2\\modules')

print(path)

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

