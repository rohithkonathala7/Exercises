data = """first line
second line
third line
fourth line
fifth line"""
splitted_data = data.split("\n")
list_a = []
list_b = []
list_c = []
for i in splitted_data:
    final = i.strip()
    list_a.append(final)
count = 1
while count<len(list_a):
    list_b = []
    list_b.append(list_a[0])
    for j in range(2):
        list_b.append(list_a[count])
        count = count + 1
    list_c.append(list_b)
print(list_c)
