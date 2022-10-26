class Sale:
    def __init__(self, name, date, membershipType, deposit, salePrice):
        self.name = name
        self.date = date
        self.membershipType = membershipType
        self.deposit = deposit
        self.salePrice = salePrice

name = input('Enter name of client: ')
date = input('Enter date in form MM/DD/YR: ')

letter = input('Full/Premium? Type F or P: ')
if(letter == 'F'):
    membershipType = "Full"
elif(letter == 'P'):
    membershipType = "Premium"
else:
    membershipType = "ERROR"

deposit = input('Deposit Today: $')
answer = input('Was it a full down? Y or N: ')
if(answer == 'N' or answer == 'n'):
    depositDate = input('When will the full deposit hit MM/DD/YR: ')

salePrice = input('Price of Sale: $')

newSale = Sale(name, date, membershipType, deposit, salePrice)

f = open("SalesList.txt", "a")
f.write(newSale.name + " " + newSale.date + " " + newSale.membershipType + " Deposit: $" + newSale.deposit + " Sale Price: Zac$" + newSale.salePrice + "\n")
f.close()

print("Sale was recorded in SalesList.txt")

