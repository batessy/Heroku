#-------------------------------------------------------------------------------
# Name:        Heroku- highest factors determiners
# Purpose:
#
# Author:      Callum
#
# Created:     27/05/2016
# Copyright:   (c) Callum 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#psuedo code:
#input of amount, stored in variable
#highest factor divided first
#variable stores remaining money populated by old variable minus factor
#repeat from highest factor to lowest factor
import math
import pickle

MoneyInput = (input("Enter the amount you want to break down"))
#isinstance(MoneyInput(int, long))
InitialValue = MoneyInput # stores the initial value entered before any changes to variable are made
Twenties = int(MoneyInput // 20) # divides the amount of money by highest factor in this case twenty and stores the number of times it can be divided by in a variable
MoneyInput = MoneyInput % 20 # makes changes to variable so the money taken by the number of twenties is deducted whilst returning a remainder
Tens = int(MoneyInput // 10)
MoneyInput = MoneyInput % 10
Fives = int(MoneyInput // 5)
MoneyInput = MoneyInput % 5
TwoPounds = int(MoneyInput // 2)
MoneyInput = MoneyInput % 2
Pounds = int(MoneyInput // 1)
MoneyInput = MoneyInput % 1
FiftyPences = int(MoneyInput // 0.50)
MoneyInput = MoneyInput % 0.50
TwentyPences = int(MoneyInput // 0.20)
MoneyInput = MoneyInput % 0.20
TenPences = int(MoneyInput // 0.10)
MoneyInput = MoneyInput % 0.10
FivePences = int(MoneyInput // 0.05)
MoneyInput = MoneyInput % 0.05
TwoPences = int(MoneyInput // 0.02)
MoneyInput = MoneyInput % 0.02
OnePences = int(MoneyInput // 0.01)
MoneyInput = MoneyInput % 0.01




print("your value of {0} can be broken down into:".format(InitialValue)) #displays the message onto the screen for the user to read

if Twenties >=2:
    print("{0} Twenty pound notes".format(Twenties))#displays how many twenty pound notes, '{0}' allows for population by variable
else: print("{0} Twenty pound note".format(Twenties))
if Tens >=2:                                    #performs quick check to see if the variables value is <=2 and displays correct plural/singular inflection
    print("{0} Ten pound notes".format(Tens))
else: print("{0} Ten pound note".format(Tens))
if Fives >=2:
    print("{0} Five pound notes".format(Fives))
else:print("{0} Five pound note".format(Fives))
if TwoPounds >=2:
    print("{0} Two pound coins".format(TwoPounds))
else: print("{0} Two pound coin".format(TwoPounds))
if Pounds >=2:
    print("{0} Pound coins".format(Pounds))
else: print("{0} Pound coin".format(Pounds))
if FiftyPences >=2:
    print("{0} Fifty pences".format(FiftyPences))
else: print("{0} Fifty pence".format(FiftyPences))
if TwentyPences >=2:
    print("{0} Twenty pences".format(TwentyPences))
else: print("{0} Twenty pence".format(TwentyPences))
if TenPences >=2:
    print("{0} Ten pences".format(TenPences))
else: print("{0} Ten pence".format(TenPences))
if FivePences >=2:
 print("{0} Five pences".format(FivePences))
else: print("{0} Five pences".format(FivePences))
if TwoPences >=2:
    print("{0} Two pences".format(TwoPences))
else: print("{0} Two pence".format(TwoPences))
if OnePences >=2:
    print("{0} One pences".format(OnePences))
else:print("{0} One pence".format(OnePences))