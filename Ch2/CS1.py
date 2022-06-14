'''
Welcome to your first project. As a creator, you always like to imagine the
final product in advance. Here I want you to develop a company catalog.
Assume that this company sells three different dry fruits-Apricot, Dates, and
Almond. The seller can sell individual items or a combination of these items.
A gift pack is a special combination that contains all three items. Here are
some special considerations:
If a customer purchases individual items, he does not
receive any discount.
If a customer purchases a combo pack with two unique
items, he gets a 10% discount.
If the customer purchases a gift pack, he gets a 25%
discount.
For illustration purposes, I choose an Indian retailer (Spencer). I also
show the price of an item in Indian Rupees. 
'''
from cmath import e


print("Please Enter Product Details, press f to end for fianl output.")
menu = {
    "Dates" : 400,
    "Apricot" : 300,
    "Almond" : 500,
    "Combo-1" : 630, 
    "Combo-2" : 810,
    "Combo-3": 720,
    "GiftBox" : 900
}
item = [ ]
price = [ ]
itemNumber = 0
discount = 0
flag = False
print("Slect Only From Menu")
print("Dates : 400,Apricot : 300,Almond : 500,Combo-1 : 630, Combo-2 : 810,Combo-3: 720,GiftBox : 900")
while True:
    data=input(f"{itemNumber} : ")
    try:
        if data != 'f':
            if data == 'Combo-1':
                if discount != 25:
                    discount = 10
            if data == "Combo-2":
                if discount != 25:
                    discount = 10
            if data == "Combo-3":
                if discount != 25:
                    discount = 10
            if data == 'GiftBox':
                    discount = 25
            if data in menu:
                item.append(data)
                price.append(menu[data])
                itemNumber += 1
            else:
                print("Invalid Entry!!")
        else:
            break
    except:
        print("Only Valid Charecters are Allowed.")
    
if discount >= 10:
    item.append('Discount')
    price.append(discount)
    Total = sum(price[0:len(price) - 1])
    Total = Total * (discount/100)
else:
    Total = sum(price)
    
print("-----------------------------------------------------")
print("Spencer Retailer\n136, Garia Station Road,\nKolkata : 700084")
print("-----------------------------------------------------")
print("Products(s)\t\tPrice (per pack)")
for i in range(len(item)):
        print(f"{item[i]}\t\t\t{price[i]}")
print("-----------------------------------------------------")
print(f"Total\t\t\t{Total}")
print("*****************************************************")
print("For free delivery, contact 123-456-789")
print("*****************************************************")