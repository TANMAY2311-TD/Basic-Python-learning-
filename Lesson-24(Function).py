'''
#in Function no need to rewrite the same block over again and again
price_1 = 500
shipping_1 = 100
discount_1 = 5
print(f'Total cost is: ${price_1 + shipping_1 - discount_1}')

price_2 = 300
shipping_2 = 80
discount_2 = 4
print(f'Total cost is: ${price_2 + shipping_2 - discount_2}')

price_3 = 750
shipping_3 = 91
discount_3 = 7
print(f'Total cost is: ${price_3 + shipping_3 - discount_3}')
'''

#main Function work
def total_cost(price, shipping, discount):
    print(f'Total cost is: ${price + shipping - discount}')

total_cost(500, 100, 5)
total_cost(100, 10, 500)  #is not possible

#using keyword argument
total_cost(price = 300, shipping = 80, discount = 4)
total_cost(discount = 7, price = 750, shipping = 91)

#another example for 'positional argument' and 'keyword argument'
def welcome(name):
    print(f'Hi! {name}')

welcome("TANMAY DAS")

#receive first and last name separately
def welcome(first_name, last_name):
    print(f'Hi! {first_name} {last_name}')

welcome("TANMAY", "DAS")

#using 'keyword argument' which is useless
welcome(first_name = "TANMAY", last_name = "DAS")
