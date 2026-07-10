#Calculate profit or loss.

sp = int(input("Enter selling price: "))
cp = int(input("Enter cost price: "))

amount = sp - cp

if amount > 0:
    print("Profit is", amount)
elif amount < 0:
    print("Loss is", amount)
else:
    print("No profit, no loss")