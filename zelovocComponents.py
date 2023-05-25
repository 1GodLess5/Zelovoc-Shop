import zelovocFunctions

class Item:
    def __init__(self, itemsName, itemsPrice):
        self.itemsName = itemsName
        self.itemsPrice = itemsPrice
        

    def addToDictionary(self, itemsDictionary: dict):
        if self.itemsName not in itemsDictionary:
            itemsDictionary[self.itemsName] = self.itemsPrice

            print("New item: " + self.itemsName + " was succesfully added.")

            return itemsDictionary
        else:
            print(color.BOLD + color.RED + "This product is already in shop's sortiment!" + color.END)


# items from shop
itemsDictionary = {
    "apple" : 5,
    "orange" : 5,
    "mandarin" : 5,
    "mango" : 6,
    "pineapple" : 6,
    "banana" : 6,
    "pear" : 7,
    "nectarine" : 7,
    "plum" : 7
}

# checking number of items in our shop to generate quantity of items
itemsCount = zelovocFunctions.numOfItems(itemsDictionary)
# shop items quantity
itemsQuantity = zelovocFunctions.itemsGenerator(itemsCount)

# users shopping cart
shoppingCart = []

# formating output
class color:
   RED = '\033[91m'
   CYAN = '\033[96m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'