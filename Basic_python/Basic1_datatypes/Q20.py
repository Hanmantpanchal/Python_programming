#Convert temperature from Celsius to Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#Convert temperature from Fahrenheit to Celsius.

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius:", celsius)

#Convert temperature from Celsius to Kelvin.

celsius = float(input("Enter temperature in Celsius: "))
kelvin = celsius + 273.15
print("Temperature in Kelvin:", kelvin)

#Convert temperature from Kelvin to Celsius.

kelvin = float(input("Enter temperature in Kelvin: "))
celsius = kelvin - 273.15
print("Temperature in Celsius:", celsius)

#Convert temperature from Celsius to Rankine.

celsius = float(input("Enter temperature in Celsius: "))
rankine = (celsius + 273.15) * 9/5
print("Temperature in Rankine:", rankine)
