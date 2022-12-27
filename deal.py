'''Deal or No Deal'''

from random import sample
import os
import math

#dictionary to keep track of cases (caseNo->caseValue)
stockCases = {
    1 : 1, 
    2 : 3, 
    3 : 5, 
    4 : 10, 
    5 : 25, 
    6 : 50, 
    7 : 75, 
    8 : 100, 
    9 : 200, 
    10 : 300,
    11 : 400,
    12 : 500,
    13 : 750,
    14 : 1000,
    15 : 5000,
    16 : 10000,
    17 : 25000,
    18 : 50000,
    19 : 75000,
    20 : 100000,
    21 : 200000,
    22 : 350000,
    23 : 500000,
    24 : 750000,
    25 : 1000000,
    }

values = list(stockCases.values())

#shuffling the values of the cases
cases = dict(zip(stockCases, sample(values, len(stockCases))))

#function to print cases in tabular form
def displayCases(caseDict):
    for key,value in caseDict.items():
        if value == "XX":
            print("XX", end = " ")
        else:
            print(f"{key:2d}", end = " ")
        if key % 5 == 0:
            print()

#function to remove chose case
def removeCase(caseDict, number):
    #values.remove(caseDict[number])
    replaceValue(values, caseDict[number])
    caseDict[number] = "XX"

#function to accept number from user
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
            if userInput > 25 or userInput < 0 or userInput in chosenCases:
                raise ValueError
        except ValueError:
            print("Please enter a valid number!")
            continue
        else:
            return userInput
            break

#function to display list in tabular form
def displayList(listName):
    for i in range(len(listName)):
        if listName[i] == 0:
            print("     XX", end = " ")
        else:
            print(f"{listName[i]:7d}", end = " ")
        if (i+1) % 5 == 0 and i != 0:
            print()
    print()

#function to replace value in a list
def replaceValue(listName, value):
    valueIndex = listName.index(value)
    listName[valueIndex] = 0

#function to calculate root mean square
def rms(listName):
    tempList = [i for i in listName if i != 0]
    sumSq = sum([i**2 for i in tempList])
    mean = sumSq / len(tempList)
    return math.sqrt(mean)


chosenCases = []    #List to keep track of cases chosen

#main function
def main():
    print("Welcome to Deal or No Deal!")
    print("Here are the cases")
    displayCases(cases)
    print("These cash amounts are hidden in these cases randomly")
    displayList(values)
    print("Your objective is to eliminate cases with lower values and try to get the best deal!")
    print("Let's begin!")
    start = input("Would you like to start playing Deal or No Deal? (Y/N): ")
    while start.lower() == 'y':
        os.system('cls')
        print("Cases: ")
        displayCases(cases)

        number = inputNumber("Choose a case number: ")
        if(number not in chosenCases):
            chosenCases.append(number)
        if cases[number] >= 50000:
            print("\nOh no! The case you chose had a value of $" + str(cases[number]) + ".\n")
        else:
            print("\nHooray! The case you chose had a value of $" + str(cases[number]) + ".\n")
        removeCase(cases, number)
        print("The remaining cases:")
        displayCases(cases)

        print("\nThe remaining values: ")
        displayList(values)

        print("Let's see what the banker has to offer.")
        offer = rms(values)
        print("The banker has offered you $" + str(offer) + " to quit the game right now!")
        
        choice = input("Would you like to accept his offer? (Y/N): ")
        if choice.lower() == 'y':
            print("Thank you for playing!")
            break
        else:
            print("Wise choice! Let's continue playing!")

main()