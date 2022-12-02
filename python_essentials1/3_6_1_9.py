my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

temp_my_list = []


for i in range(len(my_list)):
    if i in my_list:
        temp_my_list.append(i)

my_list = temp_my_list    
print("The list with unique elements only:")
print(my_list)