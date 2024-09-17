number_list = [1, 2, 3, 2, 7, 2, 10, 7]
unique = []
for number in number_list:
    if number not in unique:
        unique.append(number)

print(unique)