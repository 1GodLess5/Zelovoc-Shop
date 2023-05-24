import zelovocFunctions

class Item:
    def __init__(self, itemsName, itemsPrice):
        self.itemsName = itemsName
        self.itemsPrice = itemsPrice

        itemsDictionary[itemsName] = itemsPrice



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
   CYAN = '\033[96m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'