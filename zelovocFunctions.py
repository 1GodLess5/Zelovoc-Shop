import random
import os

import zelovocComponents


# function to get how many items are in shop
def numOfItems(itemsDictionary):
    itemsNumber = len(itemsDictionary)

    return itemsNumber

# asking for users balance
def userBalance():
    while True:
        try:
            balance = float(input("Enter your balance in €: "))
        except ValueError:
            print("You have to enter numeric value!")
            continue
        break

    return balance

#generating random items quantity from itemsDictionary
def itemsGenerator(itemsCount):
    itemsNumber = []

    for i in range(itemsCount):
        itemsNumber.append(random.randint(1, 10))

    return itemsNumber

# printing items from shop
def itemsPrint(itemsDictionary, itemsQuantity):
    counter = 0
    print("{:<17} {:<17} {:<17} {:<13}".format("PRODUCT NUMBER", "PRODUCT NAME", "PRODUCT PRICE", "AVAILABILITY(pcs)"))

    for product in itemsDictionary:
        if itemsQuantity[counter] != 0:
            print("{:<17} {:<17} {:<17} {:<13}".format(counter + 1, product, str(itemsDictionary[product]) + "€", itemsQuantity[counter]))
        else:
            print("{:<17} {:<17} {:<17} {:<13}".format(counter + 1, product, str(itemsDictionary[product]) + "€", "NOT AVAILABLE"))
        counter += 1

    print("If you wish to stop buying and want to proccess to checkout press \"0\".")


# counting price of what user buys
def itemsPrice(shoppingCart, itemsDictionary):
    listOfPrices = []

    for item in shoppingCart:
        listOfPrices.append(itemsDictionary.get(item))

    finalPrice = sum(listOfPrices)
    return finalPrice

# counting users items
def countingUserItems(shoppingCart):
    countingItems = {}

    for item in shoppingCart:
        countingItems[item] = shoppingCart.count(item)

    return countingItems

# printing out counted items
def printingCountedItems(countedItems):
    print("Your shopping cart:", end=" ")

    for item in countedItems:
        print(item + " * " + str(countedItems[item]), end=", ")

    print("")


# printing usersBalance and asking what user wants to buy
def userShopping(shoppingCart, itemsDictionary, usersBalance, itemsQuantity, itemsCount):
    wrongInput = 1

    print("\nYour balance is: " + str(usersBalance))
    # priceOfItems = itemsPrice(shoppingCart, itemsDictionary)
    countedItems = countingUserItems(shoppingCart)
    printingCountedItems(countedItems)

    while wrongInput == 1:
        dictionaryCounter = 0
        # user input cant be anything else than number
        while True:
            try:
                usersChoice = int(input("What product would you like to buy?\nUse number of product as a choice: "))
            except ValueError:
                print("Your choice doenst exist!\nEnter existing product number!")
                continue
            break

        # checking if the number exists in our dictionary, calculating the price
        if usersChoice == 0:
            endOfTheProgram(shoppingCart, itemsDictionary)
            exit("\n\n\nThanks for using my Zelovoc shop <3")
        elif usersChoice > 0 and usersChoice <= itemsCount:

        # mel bys kouknout jeste na tyhle ify a popremyslet, jestli to nejde nejak zjednodusit treba pomoci .get
        # needs to be refactored yet
            for product in itemsDictionary:
                if dictionaryCounter == usersChoice - 1:
                    if itemsQuantity[dictionaryCounter] != 0:
                        if usersBalance >= itemsDictionary[product]:
                            # items quantity descending
                            itemsQuantity[dictionaryCounter] -= 1
                            # appends name of product to the shopping cart
                            shoppingCart.append(product)
                            #lowers usersBalance based on what he bought
                            usersBalance -= itemsDictionary[product]
                            wrongInput = 0
                            break
                        else:
                            print("Your balance is too low for this product!")
                            break
                    else:
                        print("This product is no longer available, choose something else!")
                        break

                else:
                    dictionaryCounter += 1
        else:
            print("Enter a valid choice!")

    return shoppingCart, usersBalance

# function which prints the receipt and ends the shop
def endOfTheProgram(shoppingCart, itemsDictionary):
    # this command doesn't work when executed through Pycharm, but works when executing in terminal
    os.system('clear')
    print(zelovocComponents.color.BOLD + "\t\t\tSHOP RECEIPT" + zelovocComponents.color.END)

    for i in range(62):
        print("=", end="")
    print("")
    print("\t\t\tNr.: " + str(random.randint(1, 1000000)).zfill(7))
    for i in range(62):
        print("=", end="")
    print("")

    print("{:<17} {:<17} {:<17} {:<13}".format("CODE|", "QTY|", "PRODUCT NAME|", "PRICE/€"))

    for i in range(62):
        print("-", end="")
    print("")

    #quantity of products
    quantityDictionary = countingUserItems(shoppingCart)

    for product in quantityDictionary:
        # products codes
        productCode = random.randint(1, 999)
        print("{:<17} {:<17} {:<17} {:<13}".format(str(productCode).zfill(4), str(quantityDictionary[product]), product, str(itemsDictionary.get(product) * quantityDictionary[product]) + "€"))











