for character in 'Python':   #example: string
    print(character)

for item in ['Rice','Water','Salt']:  #example: list
    print(item)

for number in [ 0, 1, 2, 3, 4, 5]:  #example: list of numbers
    print(number)

for number in range(10):   #example: range
    print(number)

for number in range(5, 10):  #example: starting range
    print(number)

for number in range(5, 10, 2):  #example: starting range + steps of range
    print(number)

bills = [10, 40, 50]   #example: total bills and print formatted string
total = 0
for bill in bills:
    total += bill

print('=',total)
print(f'Total bill is: ${total}')
