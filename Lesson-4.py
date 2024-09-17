#Formula from Celsius to Fahrenheit = (celsius * (9/5)) + 32

celsius = input('Temperature in Celsius = ')
celsius = int(celsius)
fahrenheit = (celsius * (9 / 5)) + 32
fahrenheit = str(fahrenheit)

print(f"Today Fahrenheit is {fahrenheit}F") #formatted string/ f string formatting

print("Today Fahrenheit is " +fahrenheit+ "F")