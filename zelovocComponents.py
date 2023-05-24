import zelovocFunctions

class Item:
    def __init__(self, itemName: str, itemPrice: float):
        self.itemName = itemName
        self.itemPrice = itemPrice

    def nameOfItem(self):
        return self.itemName
    
    def priceOfItem(self):
        return self.priceOfItem
    
    def addItem(self, itemsList):
        itemsList.append(self.itemName)
        return itemsList

# # items from shop
itemsNamesList = []
itemsNames = ["apple", "orange", "mandarin", "mango", "pineapple", "banana", "pear", "nectarine", "plum"]
itemsPrices = [5, 5, 5, 6, 6, 6, 7, 7, 7]
zelovocFunctions.addingNewItems(itemsNames, itemsPrices, itemsNamesList)

print(orange.nameOfItem())
# # checking number of items in our shop to generate quantity of items
# itemsCount = zelovocFunctions.numOfItems(itemsDictionary)
# # shop items quantity
# itemsQuantity = zelovocFunctions.itemsGenerator(itemsCount)

# # users shopping cart
# shoppingCart = []

# formating output
class color:
   CYAN = '\033[96m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'