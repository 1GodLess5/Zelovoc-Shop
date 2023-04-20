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
