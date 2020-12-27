with open('currencyData.txt') as f:
    lines = f.readlines()
currencyDict={}
for line in lines:
    parsed=line.split("\t")
    #print(parsed)
    currencyDict[parsed[0]]=parsed[1]
#print(currencyDict)
amount=float(input("Enter the amount:\n"))
print("Enter the name of the currency you want to convert to\nAvailable option:\n")
[print(item) for item in currencyDict.keys()]
currency=input("Please enter one of the value\n")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}.")