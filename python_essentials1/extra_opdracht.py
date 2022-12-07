name = ("Jeroen Heemskerk", "Slieker, Kevin", "de Groot, Henk", "Arje van der Geest", "'O Brien, Willem Anton Stuward", "Jan Willem Klaasen")
infix_array = ["van", "der", "'O"]  # other infixes to add
data_base = {}
for person in name:
    first_name = ""
    last_name = ""
    infix = ""
    other_names = ""
    if ',' not in person:
        parts = person.split()
        first_name = parts[0]
        last_name = parts[-1]
        for between in parts[1:-1]:
            if between in infix_array:
                infix += " " + between
            else:
                other_names += " " + between
    else:
        parts = person.split(",")
        before_com = parts[0]
        after_com = parts[1]
        before = before_com.split()
        after = after_com.split()
        first_name = after[0]
        last_name = before[-1]
        if len(before) > 1:
            for i in before[0:-1]:
                infix += " " + i
        if len(after) > 1:
            for o in after[1:]:
                other_names += " " + o

    data_base.append({"First name" : first_name, "Other names" : other_names.strip(), "Infix" : infix.strip(), "Last Name" : last_name})
print(data_base)


# for person in data_base:
#     if person["First name"] == "Jeroen":
#         print(person)
