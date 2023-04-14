import csv

with open(file="record_magnum.csv", mode="r", encoding="UTF8") as f:
    csv_read = csv.reader(f)

    list_of_number = [row for row in csv_read if len(row[0]) == 4]

    int_list_of_number = [int(item[0]) for item in list_of_number]

# print(int_list_of_number)

counts = {}
for num in int_list_of_number:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

for i in range(0, 10000):
    if i not in counts:
        counts[i] = 0
 
sorted_dict = {k: counts[k] for k in sorted(counts.keys())}
# print(sorted_dict)

appeared_once = []
never_exist = []
appeared_more_than_once = []
for key, value in sorted_dict.items():
    if value == 1:
        appeared_once.append(key)
    elif value == 0:
        never_exist.append(key)
    elif value >= 2:
        appeared_more_than_once.append(key)

# print("never exist list = {}".format(never_exist))
# print("exist once list = {}".format(appeared_once))
# print("exist more than once list = {}".format(appeared_more_than_once))

todays = [391, 8495, 7126, 4589, 4048, 8249, 6837, 4080, 6141, 5093, 3317, 7349, 2948, 9776, 914, 1186, 7646, 5280, 7055, 77, 8934, 7581, 4684]

appeared_again = [item for item in todays if item in sorted_dict.keys() and sorted_dict[item] >= 1]
not_appeared = [item for item in todays if item in sorted_dict.keys() and sorted_dict[item] == 0]

print("appeared again : {}".format(appeared_again))
print("new number list : {}".format(not_appeared))

for item in appeared_again:
    print("{} = {}".format(item, sorted_dict[item]))

# for item in todays:
#     if item in sorted_dict.keys():
#         new_appeared = []
# print(counts)
# for num, count in counts.items():
#     print(f"{num}: {count}")

print(len(counts))

