
import bruteForce.apiTest as apiTest
#import exportFiles.exportFiles as eF
import os
import sys
import toolsOutput.testingIntegration as toolsIntegration

def main():

    print("Welcome to API Endpoint Discovery!\n"
        "This program is made and distributed by BDO Advisory.\n"
        "\n"
        "To start using the program, type in -h to bring up the help page if you're unsure about the commands")

    flag = False

    while flag != True:
        try:
            usrInput = input("Please enter your command here(type -h for the list of commands):  ").lower() #user input
            print("")
            #help page
            if usrInput == "-h":
                print("----------------------------------------------------------------------------------------------------------------------\n"
                "Welcome to the API Discovery Help Page! Here are the list of commands:\n"
                "-b         Brute Force Method using a specified wordlist and url\n"
                "-o         Output to a readable csv/excel/pdf file. (Can only be done after using the other methods of enumeration\n"
                "-t         Using tools (Subfinder,Nuclei etc) to recursively find and test the web links/api links found (if any)\n"
                "-q         To quit the program\n"
                "----------------------------------------------------------------------------------------------------------------------\n")
                
            #function 1: brute force
            elif usrInput == "-b":
                print("you chose the brute force method!")
                apiTest.apiTest()
            #function 2: output to csv & pdf file  
            #elif usrInput == "-o":
            #    print("Outputted to CSV & PDF File. This file can be found under the export files file as output.csv and output.pdf")
            #    eF.main()
            #function 4: 

            #function (x): quit 
            elif usrInput == "-t":
                print("You chose to use the tools!")
                toolsIntegration.main()
                
            elif usrInput == "-q":
                print("Ending Program!")
                sys.exit()
            else:
                print("Please use the specified options! Thanks")
        #error handling
        except KeyboardInterrupt:
            print("\nThe program has stopped unexpectedly! Please check your inputs and ensure that your inputs are valid(unless you ctrl c then thats fine).")
            flag = True
    return None

#run main function if main function is found 
if __name__ == "__main__":
    main()

