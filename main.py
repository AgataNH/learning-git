number_list = []
new_number_list = []
i = 0
for i in range(0, 101):
    if i % 5 == 0:
        number_list.append(i)
        new_number_list.append(i*i)
        i = i + 1
    else:
        continue
print(number_list)
print(new_number_list)
