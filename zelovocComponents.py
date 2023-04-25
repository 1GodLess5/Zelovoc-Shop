import zelovocFunctions

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
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'