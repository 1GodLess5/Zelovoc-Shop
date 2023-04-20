import random

# function for getting how many items are in shop
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



def itemsPrice(shoppingCart):
    numberOfProducts = numOfItems(shoppingCart)

    countingItems = {}

    for i in shoppingCart:
        countingItems[i] = shoppingCart.count(i)
    # musis vymyslet kam v programu prcnes itemsPrice(), protoze jako dictionary musi byt zaplneny, jinak hazi error :)
    # pak uz by to melo byt snad v cajku, uvidime -> tohle pisu proto, ze potrebuju udelat push na git :D
    # print("You bought: ")
    # for i in range(numberOfProducts):

    # tady budes pocitat kolik stoji nakup uzivatele pomoci jmen z dictionary itemsDictionary {}
    # print ovoce * 3
    #print celkova cena nakupu



# printing usersBalance and asking what user wants to buy
def userShopping(shoppingCart, itemsDictionary, usersBalance, itemsQuantity, itemsCount):
    wrongInput = 1

    print("\nYour balance is: " + str(usersBalance))

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
            #musim dodelat funkci pro exit z kodu pryc
            exit("\n\n\nThanks for using my Zelovoc shop <3")
        elif usersChoice > 0 and usersChoice <= itemsCount:

            for product in itemsDictionary:
                if dictionaryCounter == usersChoice - 1:
                    if itemsQuantity[dictionaryCounter] != 0:
                        if usersBalance >= itemsDictionary[product]:
                            # items quantity descending
                            itemsQuantity[dictionaryCounter] -= 1
                            # appends name of product to the shopping cart
                            shoppingCart.append(itemsDictionary)
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
