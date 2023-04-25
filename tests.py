import zelovocComponents
import os
import random

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

