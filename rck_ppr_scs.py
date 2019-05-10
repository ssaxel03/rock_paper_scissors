def main():

    import time
    import random
    import os

    optionContinue = True

    while optionContinue:

        invalidInput = True

        print("1. Play")
        print("2. Exit")
        while invalidInput:
            try:
                option = int(input("Option: "))
                if option != 1 and option != 2:
                    invalidInput = True
                else:
                    invalidInput = False
            except ValueError:
                print("Invalid input")
                invalidInput = True
            except:
                print("Unknown error")
                invalidInput = True
        if option == 1:
            os.system("cls")
            print("1.Rock")
            print("2.Paper")
            print("3.Scissors")
            invalidInput_1 = True
            while invalidInput_1:
                try:
                    play = int(input("Option: "))
                    if play != 1 and play != 2 and play != 3:
                        print("Invalid input")
                        invalidInput_1 = True
                    else:
                        invalidInput_1 = False
                except ValueError:
                    print("Invalid input")
                    invalidInput_1 = True
                except:
                    print("Unknown error")
                    invalidInput_1 = True

            os.system("cls")

            time.sleep(1)
            print("Rock...")
            time.sleep(1)
            print("Paper...")
            time.sleep(1)
            print("Scissors...")
            time.sleep(1)
            opponentPlay = random.randint(1, 3)

            if play == 1:
                if opponentPlay == 1:
                    print("Draw")
                elif opponentPlay == 2:
                    print("Loss")
                else:
                    print("Win")
            if play == 2:
                if opponentPlay == 1:
                    print("Win")
                elif opponentPlay == 2:
                    print("Draw")
                else:
                    print("Loss")
            if play == 3:
                if opponentPlay == 1:
                    print("Loss")
                elif opponentPlay == 2:
                    print("Win")
                else:
                    print()

            input("")
            os.system("cls")

        elif option == 2:            
            break     

if __name__ == "__main__":
    main() 
        
            