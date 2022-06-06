data = """device1   vlan1
device2   vlan2
device3   vlan1
device2   vlan3
device1   vlan4
device2   vlan1
device3   vlan6"""
splitted_data = data.split("\n")
dictionary = {}
list_a = []
for i in splitted_data:
    final = i.strip().split(" ")
    list_a.append([final[0],final[-1]])
for i in range(len(list_a)):
    if list_a[i][0] in dictionary.keys():
        continue
    list_b = []
    for j in range(len(list_a)):
        if(list_a[i][0] == list_a[j][0]):
            list_b.append(list_a[j][1])
            dictionary[list_a[i][0]] = list_b
print(dictionary)
