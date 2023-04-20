import zelovocComponents
import zelovocFunctions

# initialization of key variables of the program
userBuying = 1

# asking for users balance
usersBalance = float(zelovocFunctions.userBalance())

while userBuying:
    #printing out shop
    zelovocFunctions.itemsPrint(zelovocComponents.itemsDictionary, zelovocComponents.itemsQuantity)
    #giving user choice of buying
    zelovocComponents.shoppingCart, usersBalance = zelovocFunctions.userShopping(zelovocComponents.shoppingCart, zelovocComponents.itemsDictionary, usersBalance, zelovocComponents.itemsQuantity, zelovocComponents.itemsCount)
