from create import get_option
from display import displayData
import os

os.system('clear')
print("Welcome to our data management CLI!\n")
while 1:
    print("What would you like to do?")
    print("Enter Data:          1")
    print("Display Data:        2")
    print("Quit Program:        0")
    option = input('>>')
    os.system('clear')

    if option == '1':
        print("Please select an option:")
        print("Studnet:         1")
        print("Lecturer:        2")
        print("General Staff:   3")
        print("Back:            0")
        option_2 = input('>>')
        os.system('clear')
        if '1' <= option_2 and option_2 <= '3':
            get_option(option_2)
    elif option == '2':
        print("What would you like to see?")
        print("Studnets:        1")
        print("Lecturers:       2")
        print("General Staff:   3")
        print("All Entries:     4")
        print("Back:            0")
        option_3 = input('>>')
        os.system('clear')
        if '1' <= option_3 and option_3 <= '4':
            displayData(option_3)
    elif option == '0':
        print("GoodBaye!")
        break
    else:
        print("Invalid Input!\bTry Again!")
