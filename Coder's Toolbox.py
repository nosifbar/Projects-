#Programming Project #3
#Coder's Toolbox
#Programming Fundamentals 1
#Spring Semester 2019
#Team Members - Arsh Maredia, Nosif Ali, Saifin Sherwa, Joel Varghese  --> Group 3 

#                                                                   ***Project Overview***
#   This is an update to the ultimate number conversion program that is a toolbox or a kit for any programmer or coder. This program allows the user to input any type of a number which could either be in binary(2),
#   or Hex(16), or Octal(8), or Decimal(10). Then, the program will perform the calculations and display the other conversion values. The update in the program allows the user to add/subtract two binary or two
#   hexadecimal or two octal or two decimal values. This is a program that is definitely worth investing in as it is a perfect kit for a programmer or a coder who works a lot with programs that require number
#   conversions as they will be able to input their values in this program and get fast results rather than putting their time on doing the calculations manually.

print("******CODER'S TOOLBOX******") #Program Title 

print("\n\nWhich type of number system do you want to convert?")

while(True):
    n=input("\nMAIN MENU\nd.Convert a Decimal value\nb.Convert a Binary value\nh.Convert a Hexadecimal value\no.Convert an Octal value\nD.Decimal Addition/Subtraction\nB.Binary Addition/Subtraction\nH.Hexadecimal Addition/Subtraction\nO.Octal Addition/Subtraction\nq.Quit\n\nPlease make a selection: ") #Program asking the user for an input.
    if(n=='d'): #User Input
        while(True):
            text = input("\nEnter the Decimal value for conversion or type 'back' to go back to main menu or type 'q' to quit the program: ")

            try: #Program Output: when the user inputs 'd' to convert a decimal value to other number systems. 
                decimal = int(text)
                print("\nThe equivalent Hexadecimal value is: ", hex(decimal))
                print("The equivalent Octal value is: ", oct(decimal))
                print("The equivalent Binary value is: ", bin(decimal))
                
            except ValueError:        #'ValueError' occurs if the user inputs anything except a decimal value. 
                if(text == 'back'):   #'back' allows users to go back to the main menu. 
                    break
                elif(text == 'q'):    #Typing 'q' will quit the program. 
                    print('\n')
                    quit()
                else:
                    print("\n##Value Error: Invalid Decimal value.##\n")

        
    elif(n=='b'):  #User Input
        while(True):
            text = input("\nEnter the Binary value for conversion or type 'back' to go back to main menu or type 'q' to quit the program: ")
            
            try: #Program Output: when the user inputs 'b' to convert a binary value to other number systems. 
                decimal = 0
                for digit in text: #Converts decimal to binary. 
                    if(digit=='0' or digit=='1'):
                        decimal = decimal*2 + int(digit)
                    else:
                        decimal = int("h")

                print("\nThe equivalent Decimal value is: ", (decimal))
                print("The equivalent Octal value is: ", oct(decimal))
                print("The equivalent Hexadecimal value is: ", hex(decimal))
                
            except ValueError: #'ValueError occurs if the user inputs anything except a binary value. 
                if(text == 'back'):
                    break
                elif(text == 'q'):
                    print('\n')
                    quit()
                else:
                    print("\n##Value Error: Invalid Binary value.##\n")

                
    elif(n=='h'): #User Input
        while(True):
            text = input("\nEnter the Hexadecimal value for conversion or type 'back' to go back to main menu or type 'q' to quit the program: ")
            
            try: #Program Output: when the user inputs 'h' to convert a hexadecimal value to other number systems. 
                decimal = int(text, 16)
                print("\nThe equivalent Decimal value is: ", str(decimal))
                print("The equivalent Binary value is: ", bin(decimal))
                print("The equivalent Octal value is: ", oct(decimal))

            except ValueError: #'ValueError' occurs if the user inputs anything expect a hexadecimal value. 
                if(text == 'back'):
                    break
                elif(text == 'q'):
                    print('\n')
                    quit()
                else:
                    print("\n##Value Error: Invalid Hexadecimal value.##\n")
                    

    elif(n=='o'): #User Input
        while(True):
            text = input("\nEnter the Octal value for conversion or type 'back' to go back to main menu or type 'q' to quit the program: ")

            try: #Program Output: when the user inputs 'o' to convert an octal value to other number systems.
                decimal = int(text, 8)
                print("\nThe equivalent Decimal value is: ", str(decimal))
                print("The equivalent Binary value is: ", bin(decimal))
                print("The equivalent Hexadecimal value is: ", hex(decimal))
                
            except ValueError: #'ValueError' occurs if the user inputs anything expect an octal value. 
                    if(text == 'back'):
                        break
                    elif(text == 'q'):
                        print('\n')
                        quit()
                    else:
                        print("\n##Value Error: Invalid Octal value.##\n")

    elif(n=='D'): #User Input

        while(True):
            text = '' #input
            print("\nEnter the two Decimal values for conversion or type 'back' to go back to main menu or type 'q' to quit the program: ")
            
            try: #Program Output: when the user inputs 'D' to combine two Decimal values. 
                text = input("Input a decimal Number: ")
                decimal_1 = int(text, 10)
                text = input("Input a second decimal Number: ")
                decimal_2 = int(text, 10)

                #decimal_1 = int(decimal_1, 10)
                #decimal_2 = int(decimal_2, 10)

                print(decimal_1)
                print(decimal_2)
                decimal_sum = decimal_1 + decimal_2
                print(decimal_sum)
                print(int(decimal_sum))

                
            except ValueError: #'ValueError' occurs if the user inputs anything expect a decimal value. 
                if(text == 'back'):
                    break
                elif(text == 'q'):
                    print('\n')
                    quit()
                else:
                    print("\n##Value Error: Invalid Decimal value.##\n")

    
    elif(n=='B'): #User Input

        while(True):
            text = '' #input
            print("\nEnter the two Binary values for conversion or type 'back' to go back to main menu or type 'q' to quit the program: ")
            
            try: #Program Output: when the user inputs 'B' to combine two Binary values. 
                text = input("Input a Binary Number: ")
                binary_1 = int(text, 2)
                text = input("Input a second Binary Number: ")
                binary_2 = int(text, 2)

                #binary_1 = int(binary_1, 2)
                #binary_2 = int(binary_2, 2)

                print(binary_1)
                print(binary_2)
                binary_sum = binary_1 + binary_2
                print(binary_sum)
                print(int(binary_sum))

                
            except ValueError: #'ValueError' occurs if the user inputs anything expect a binary value. 
                if(text == 'back'):
                    break
                elif(text == 'q'):
                    print('\n')
                    quit()
                else:
                    print("\n##Value Error: Invalid Binary value.##\n")


    elif(n=='H'): #User Input

        while(True):
            text = '' #input
            print("\nEnter the two Hexadecimal values for conversion or type 'back' to go back to main menu or type 'q' to quit the program: ")
            
            try: #Program Output: when the user inputs 'H' to combine two Hexadecimal values. 
                text = input("Input a Hexadecimal Number: ")
                hexadecimal_1 = int(text, 16)
                text = input("Input a second Hexadecimal Number: ")
                hexadecimal_2 = int(text, 16)

                #hexadecimal_1 = int(hexadecimal_1, 16)
                #hexadecimal_2 = int(hexadecimal_2, 16)

                print(hexadecimal_1)
                print(hexadecimal_2)
                hexadecimal_sum = hexadecimal_1 + hexadecimal_2
                print(hexadecimal_sum)
                print(int(hexadecimal_sum))

                
            except ValueError: #'ValueError' occurs if the user inputs anything expect a hexadecimal value. 
                if(text == 'back'):
                    break
                elif(text == 'q'):
                    print('\n')
                    quit()
                else:
                    print("\n##Value Error: Invalid Hexadecimal value.##\n")


    elif(n=='O'): #User Input

        while(True):
            text = '' #input
            print("\nEnter the two Octal values for conversion or type 'back' to go back to main menu or type 'q' to quit the program: ")
            
            try: #Program Output: when the user inputs 'O' to combine two Octal values. 
                text = input("Input a Octal Number: ")
                octal_1 = int(text, 8)
                text = input("Input a second Octal Number: ")
                octal_2 = int(text, 8)

                #octal_1 = int(octal_1, 8)
                #octal_2 = int(octal_2, 8)

                print(octal_1)
                print(octal_2)
                octal_sum = octal_1 + octal_2
                print(octal_sum)
                print(int(octal_sum))

                
            except ValueError: #'ValueError' occurs if the user inputs anything expect a octal value. 
                if(text == 'back'):
                    break
                elif(text == 'q'):
                    print('\n')
                    quit()
                else:
                    print("\n##Value Error: Invalid Octal value.##\n")
                

    elif(n=='q'): #If the user types 'q' the program ends.
        print("Thankyou for using this conversion tool.")
        break
    
    else:
        print("\nError: Invalid input\n") #If the user inputs any value expect for the value in the main menu selection, then the program displays the message 'Error: Invalid input'.
