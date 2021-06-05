# \\ ----- First define global functions ----- //
def boolQuestion(question):
    validated = False
    counter = 0
    while validated == False:
        res = input(question)
        if res == "yes" or res=="y" or res=="":
            res = 'yes'
            validated = True
        elif res == "no" or res=="n":
            res = 'no'
            validated = True
        elif counter == 1:
            print('\nI said, please answer yes or no to the following question: ')
            counter = 2
        elif counter == 2:
            print('\nYou will drive me crazy... PLEASE ANSWER YES OR NO TO THE FOLLOWING QUESTION: ')
        else: 
            print('\nNope, you must answer yes or no to the following question: ')
            counter = 1
    return res

# \\ ----- Main script ----- //
import tkinter as tk
from tkinter import filedialog
import os
import difflib

root = tk.Tk()
root.withdraw()

# dir = str(input("Enter the path to the folder you want to analyze: "))
dir = filedialog.askdirectory()
percent = int(input("Enter the % of similarity for the file names detection:"))
list = os.listdir(dir)
for i in list:
    for i2 in list:
        iName, iExt = os.path.splitext(i)
        iName2, iExt2 = os.path.splitext(i2)
        sequence = difflib.SequenceMatcher(isjunk=None, a=iName, b=iName2)
        difference = sequence.ratio()*100
        difference = round(difference, 1)
        if (difference > percent) and iName != iName2:
            print('Two similar file names : "' + i + '" and "' + i2 + '".')
            delete = boolQuestion("Do you want to delete " + i + "? (yes/no)")
            if delete == "yes": 
                os.remove(dir + '/' + i)
                list.remove(i)
                print(i + 'deleted' + '\n')
            elif delete == "no": 
                delete2 = boolQuestion("Do you want to delete " + i2 + "? (yes/no)")
                if delete2 == "yes": 
                    os.remove(dir + '/' + i2)
                    list.remove(i2)
                    print(i2 + 'deleted' + '\n')
                elif delete2 == "no": print('You chose to keep ' + i + ' and ' + i2 + '\n')
input('Every files checked, press enter to exit')