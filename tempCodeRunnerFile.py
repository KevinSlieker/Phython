name = ("Jeroen Heemskerk", "Slieker, Kevin", "de Groot, Henk", "Arje van der Geest", "'O Brien, Willem Anton Stuward", "Jan Willem Klaasen")
print(name)
print(type(name))
print(len(name))
data_base = [{"First name" : "", "Other names" : "", "Infix" : "", "Last Name" : ""}]
print(data_base)
print(type(data_base))
data_base.append({"First name" : "a", "Other names" : "b", "Infix" : "c", "Last Name" : "d"})
print(data_base)
print(name[1].split(sep=","))
print(len(name[1].split()))

for person in name:
    print(person)
    print(type(person))
    infix = ""
    if ',' not in person:
        parts = person.split()
        first_name = parts[0]
        print(first_name)
        last_name = parts[-1]
        print(last_name)