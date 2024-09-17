grocery_list = ['Rice','Egg','Salt','Sugar','Onion']

print(grocery_list)
print(grocery_list[0:-2])
print(grocery_list[:4])

grocery_list[3] = 'Oil'

print(grocery_list)

price = [75, 13, 40, 110, 90]
max = price[0]
for value in price:
    if value > max:
        max = value

print(max)