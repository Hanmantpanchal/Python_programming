#Calculate electricity bill.

units = int(input("Enter the number of units: "))

if units <= 100:     
    bill = units * 1.20
    print("Electricity bill is: ", bill)

elif units <= 200:
    bill = 100 * 1.20 + (units - 100) * 1.50
    print("Electricity bill is: ", bill)

elif units <= 300:
    bill = 100 * 1.20 + 100 * 1.50 + (units - 200) * 1.80
    print("Electricity bill is: ", bill)

else:
    bill = 100 * 1.20 + 100 * 1.50 + 100 * 1.80 + (units - 300) * 2.00
    print("Electricity bill is: ", bill)