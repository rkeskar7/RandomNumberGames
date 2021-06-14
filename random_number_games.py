import random
starting_money = 100

#Functions
#Random coin flip

coin_options = ["Heads", "heads", "Tails", "tails"]
def heads_or_tails(money_bet, coin_side):
    global starting_money
    head_or_tail = random.randint(1, 2) #Randomly outputs a number between 0 (Heads) and 1 (Tails)

    if str(coin_side) == "heads" or str(coin_side) == "Heads": #The user chose heads
        if head_or_tail == 1: #The coin landed on heads
            #The user now wins money
            print("You have now won " + str(money_bet) + " dollars!")
            new_money = starting_money + int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
        elif head_or_tail == 2: #The coin landed on tails
            #The user now loses money
            print("You have now lost " + str(money_bet) + " dollars!")
            new_money = starting_money - int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
    elif coin_side == "tails"  or coin_side == "Tails": #The coin landed on tails
        if head_or_tail == 1: #The coin landed on heads
            #The user now loses money
            print("You have now lost " + str(money_bet) + " dollars!")
            new_money = starting_money - int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
        elif head_or_tail == 2: #The coin landed on tails
            #The user now wins money
            print("You have now won " + str(money_bet) + " dollars!")
            new_money = starting_money + int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
    play_again_Heads_or_tails = input("Thanks for playing Heads or Tails! Want to play this game again? Yes or No?: ")
    play_again_Heads_or_tails_options = ["Yes", "yes", "No", "no"]
    while not(play_again_Heads_or_tails in play_again_Heads_or_tails_options): #Invalid input
        print("Invalid option.")
        play_again_Heads_or_tails = input("Thanks for playing Heads or Tails! Want to play another game? Yes or No?: ")
    if play_again_Heads_or_tails == "Yes" or play_again_Heads_or_tails == "Yes":
        choose_play_heads_or_tails()
    elif play_again_Heads_or_tails == "No" or play_again_Heads_or_tails == "no":
        print("Thanks for playing Heads or Tails! Want to play a different game?")
        print("")
        menu()


even_odd_options = ["Even", "even", "Odd", "odd"]


def even_or_odd(money_bet, even_odd):
    global starting_money
    dice_1 =  random.randint(1, 6) #Randomly rolls a number between 1 and 6
    dice_2 = random.randint(1, 6) #Randomly rolls a number between 1 and 6

    if (dice_1 + dice_2) % 2 == 0: #If the number is even
        if even_odd == "Even" or even_odd == "even": #The user guessed even
            #The user now wins money
            print("The sum was in fact even! Good job!")
            print("You have now won " + str(money_bet) + " dollars!")
            new_money = starting_money + int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
        elif even_odd == "Odd" or even_odd == "odd": #The user guessed odd
            #The user now loses money
            print("The sum was not even!")
            new_money = starting_money - int(money_bet)
            starting_money = new_money
            print("You have now lost " + str(money_bet) + " dollars!")
            print("You now have " + str(starting_money) + " dollars!")

    else: #The number is odd
        if even_odd == "Even" or even_odd == "even": #The user guessed even
            #The user now loses money
            print("The sum was not odd!")
            print("You have now lost " + str(money_bet) + " dollars!")
            new_money = starting_money - int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
        elif even_odd == "Odd" or even_odd == "odd": #The user guessed odd
            #The user now wins money
            print("The sum was indeed odd! Great guess!")
            print("You have now won " + str(money_bet) + " dollars!")
            new_money = starting_money + int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
    play_again_ChoHan = input("Thanks for playing ChoHan (Even or Odd)! Want to play this game again? Yes or No?: ")
    play_again_ChoHan_options = ["Yes", "yes", "No", "no"]
    while not(play_again_ChoHan in play_again_ChoHan_options): #Invalid input
        print("Invalid option.")
        play_again_ChoHan = input("Thanks for playing ChoHan (Even or Odd)! Want to play this game again? Yes or No?: ")
    if play_again_ChoHan == "Yes" or play_again_ChoHan_options == "Yes":
        choose_play_ChoHan()
    elif play_again_ChoHan == "No" or play_again_ChoHan == "no":
        print("Thanks for playing ChoHan (Even or Odd)! Want to play a different game?")
        print("")
        menu()



Black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
Red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
possible_options_roulette = ["Even", "even", "Odd", "odd", "Black", "black", "Red", "red", "Low", "low", "High", "high"]
def roulette(money_bet, category):
    global starting_money
    roulette_number = random.randint(1, 36) #Randomly generated number between 1 and 36

    if category == "Even" or category == "even":
        if roulette_number % 2 == 0: #Even number
            #User wins
            print("The number was even! Awesome!")
            print("You have now won " + str(money_bet) + " dollars!")
            new_money = starting_money + int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
        else: #Odd
            #User loses
            print("The number was not even!")
            print("You have now lost " + str(money_bet) + " dollars!")
            starting_money = starting_money - int(money_bet)
            print("You now have " + str(starting_money) + " dollars!")

    elif category == "Odd" or category == "odd":
        if roulette_number % 2 == 0: #Even number
            #User loses
            print("The number was not odd!")
            print("You have now lost " + str(money_bet) + " dollars!")
            new_money = starting_money - int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
        else: #Odd
            #User wins
            print("The number was odd! Great job!")
            print("You have now won " + str(money_bet) + " dollars!")
            new_money = starting_money + int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
    elif category == "Red" or category == "red":
        if roulette_number in Black: #Black number
            #User loses
            print("The number was not Red!")
            print("You have now lost " + str(money_bet) + " dollars!")
            new_money = starting_money - int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
        elif roulette_number in Red:
            #User wins
            print("The number was Red! Nice!")
            print("You have now won " + str(money_bet) + " dollars!")
            new_money = starting_money + int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
    elif category == "Black" or category == "black":
        if roulette_number in Black: #Black number
            #User wins
            print("The number was Black! Good job!")
            print("You have now won " + str(money_bet) + " dollars!")
            new_money = starting_money + int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
        elif roulette_number in Red:
            #User loses
            print("The number was not Black!")
            print("You have now lost " + str(money_bet) + " dollars!")
            new_money = starting_money - int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
    elif category == "Low" or category == "low":
        if roulette_number >= 1 or roulette_number <= 18: #Low numbers:
            #User wins
            print("The number was Low! Good job!")
            print("You have now won " + str(money_bet) + " dollars!")
            new_money = starting_money + int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
        else:
            #User loses
            print("The number was not Low!")
            print("You have now lost " + str(money_bet) + " dollars!")
            new_money = starting_money - int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
    elif category == "High" or "high":
        if roulette_number >= 19 or roulette_number <= 36: #Low numbers:
            #User wins
            print("The number was High! Good job!")
            print("You have now won " + str(money_bet) + " dollars!")
            new_money = starting_money + int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money) + " dollars!")
        else:
            #User loses
            print("The number was High!")
            print("You have now lost " + str(money_bet) + " dollars!")
            new_money = starting_money - int(money_bet)
            starting_money = new_money
            print("You now have " + str(starting_money - int(money_bet)) + " dollars!")
    play_again_American_Roulette = input("Thanks for playing American Roulette! Want to play this game again? Yes or No?: ")
    play_again_American_Roulette_options = ["Yes", "yes", "No", "no"]
    while not(play_again_American_Roulette in play_again_American_Roulette_options): #Invalid input
        print("Invalid option.")
        play_again_American_Roulette = input("Thanks for playing American Roulette! Want to play this game again? Yes or No?: ")
    if play_again_American_Roulette == "Yes" or play_again_American_Roulette == "Yes":
        choose_play_American_Roulette()
    elif play_again_American_Roulette == "No" or play_again_American_Roulette == "no":
        print("Thanks for playing American Roulette! Want to play a different game?")
        print("")
        menu()

#User input money_bet and category
def highest_card(player_1, player_2):
    print("Selecting Player 1's card...")

    global starting_money
    player_1_card_number = random.randint(1, 13) #Randomly chooses a card (1 - Ace ; 13 - King)
    player_1_card_suit = random.randint(1, 4) #Randomy chooses a suit (1 - Hearts, 2 - Clubs, 3 - Spades, 4 - Diamonds)

    player_2_card_number = random.randint(1, 13) #Randomly chooses a card (1 - Ace ; 13 - King)
    player_2_card_suit = random.randint(1, 4) #Randomy chooses a suit (1 - Hearts, 2 - Clubs, 3 - Spades, 4 - Diamonds)

    #Special Cards
    if player_1_card_number == 1:
        card_number_1 = "Ace"
    elif player_1_card_number == 11:
        card_number_1 = "Jack"
    elif player_1_card_number == 12:
        card_number_1 = "Queen"
    elif player_1_card_number == 13:
        card_number_1 = "King"

    if player_2_card_number == 1:
        card_number_2 = "Ace"
    elif player_2_card_number == 11:
        card_number_2 = "Jack"
    elif player_2_card_number == 12:
        card_number_2 = "Queen"
    elif player_2_card_number == 13:
        card_number_2 = "King"
    #Player 1
    if player_1_card_suit == 1: #Hearts
        #Special Cards
        if player_1_card_number == 1 or player_1_card_number == 11 or player_1_card_number == 12 or player_1_card_number == 13:
            print("Player one has the " + card_number_1 + " of " + "Hearts")
        else:
            print("Player one has the " + str(player_1_card_number) + " of " + "Hearts")
    elif player_1_card_suit == 2: #Clubs
        #Special Cards
        if player_1_card_number == 1 or player_1_card_number == 11 or player_1_card_number == 12 or player_1_card_number == 13:
            print("Player one has the " + card_number_1 + " of " + "Clubs")
        else:
            print("Player one has the " + str(player_1_card_number) + " of " + "Clubs")
    elif player_1_card_suit == 3: #Spades
        #Special Cards
        if player_1_card_number == 1 or player_1_card_number == 11 or player_1_card_number == 12 or player_1_card_number == 13:
            print("Player one has the " + card_number_1 + " of " + "Spades")
        else:
            print("Player one has the " + str(player_1_card_number) + " of " + "Spades")
    elif player_1_card_suit == 4: #Diamonds
        #Special Cards
        if player_1_card_number == 1 or player_1_card_number == 11 or player_1_card_number == 12 or player_1_card_number == 13:
            print("Player one has the " + card_number_1 + " of " + "Hearts")
        else:
            print("Player one has the " + str(player_1_card_number) + " of " + "Diamonds")

    print(" ")
    print("Selecting Player 2's card...")
    #Player 2
    if player_2_card_suit == 1: #Hearts
        #Special Cards
        if player_2_card_number == 1 or player_2_card_number == 11 or player_2_card_number == 12 or player_2_card_number == 13:
            print("Player two has the " + card_number_2 + " of " + "Hearts")
        else:
            print("Player two has the " + str(player_2_card_number) + " of " + "Hearts")
    elif player_2_card_suit == 2: #CLubs
        #Special Cards
        if player_2_card_number == 1 or player_2_card_number == 11 or player_2_card_number == 12 or player_2_card_number == 13:
            print("Player two has the " + card_number_2 + " of " + "Clubs")
        else:
            print("Player two has the " + str(player_2_card_number) + " of " + "Clubs")
    elif player_2_card_suit == 3: #Spades
        #Special Cards
        if player_2_card_number == 1 or player_2_card_number == 11 or player_2_card_number == 12 or player_2_card_number == 13:
            print("Player two has the " + card_number_2 + " of " + "Spades")
        else:
            print("Player two has the " + str(player_2_card_number) + " of " + "Spades")
    elif player_2_card_suit == 4: #Diamonds
        #Special Cards
        if player_2_card_number == 1 or player_2_card_number == 11 or player_2_card_number == 12 or player_2_card_number == 13:
            print("Player two has the " + card_number_2 + " of " + "Diamonds")
        else:
            print("Player two has the " + str(player_2_card_number) + " of " + "Diamonds")

    print(" ")
    if player_1_card_number > player_2_card_number:
        print("Player one wins!")
        print("Player one has $" + str(starting_money + int(player_1)))
        print("Player two has $" + str(starting_money - int(player_2)))

    elif player_2_card_number > player_1_card_number:
        print("Player two wins!")
        print("Player one has $" + str(starting_money - int(player_1)))
        print("Player two has $" + str(starting_money + int(player_2)))
    elif player_1_card_number == player_2_card_number:
        print("It's a tie!")
        print("Both players have $" + str(starting_money))

    play_again_Highest_Card = input("Thanks for playing Who Has the Highest card! Want to play this game again? Yes or No?: ")
    play_again_Highest_Card_options = ["Yes", "yes", "No", "no"]
    while not(play_again_Highest_Card in play_again_Highest_Card_options): #Invalid input
        print("Invalid option.")
        play_again_Highest_Card = input("Thanks for playing Who Has the Highest card! Want to play this game again? Yes or No?: ")
    if play_again_Highest_Card == "Yes" or play_again_Highest_Card == "yes":
        choose_play_Highest_Card()
    elif play_again_Highest_Card == "No" or play_again_Highest_Card == "no":
        print("Thanks for playing Who Has the Highest Card! Want to play a different game?")
        print("")
        menu()






#User_interface
print("")
def menu():
    print("Welcome to the Games of Chance! Please see the menu options below!")
    print("1: Heads or Tails")
    print("2: ChoHan (Even or Odd)")
    print("3: American Roulette")
    print("4: Who Has the Highest Card?")
    print("Q: Quit")
    user_choice = input("Please Select Your Game of Choice Here: ")

    menu_options = ['1', '2', '3', '4', 'Q']
    while not(user_choice in menu_options): #Invalid menu options chosen
        print("Invalid menu option! Please re-enter")
        user_choice = input("Please Select Your Game of Choice Here: ")

    if user_choice == 'Q': #User chooses to quit
        starting_money == 100 #Reset
        print("Thanks for playing the Games of Chance! ")

    elif user_choice != 'Q':

        if int(user_choice) == 1: #Heads or Tails
            choose_play_heads_or_tails()

        elif int(user_choice) == 2: #ChoHan (Even or Odd)
            choose_play_ChoHan()

        elif int(user_choice) == 3: #American Roulette
            choose_play_American_Roulette()

        elif int(user_choice) == 4: #Who Has the Highest Card
            choose_play_Highest_Card()

def choose_play_heads_or_tails(): #Heads or Tails
    print("Welcome to Heads or Tails")
    print("You currently have $" + str(starting_money) + ".")
    #money_bet = input("Please enter the amount of money that you would like to bet (without the $): ")
    while True:
        try:
            money_bet = int(input("Please enter the amount of money that you would like to bet (without the $): "))
            while int(money_bet) < 0: #Negative number
                print("Invalid amount! Please enter a valid amount!")
                money_bet = input("Please enter the amount of money that you would like to bet (without the $): ")
            break
        except ValueError:
            print("Invalid amount! Please enter a valid amount!")



    coin_side = input("Is it Heads or Tails? Type your choice here: ")
    while not(coin_side in coin_options): #Invalid options
        print("Invalid input!")
        coin_side = input("Please enter heads or tails: ")

    heads_or_tails(money_bet, coin_side) #Calling the function

def choose_play_ChoHan(): #ChoHan (Even or Odd)
    print("Welcome to ChoHan (Even or Odd)")
    print("You currently have $" + str(starting_money) + ".")
    #money_bet = input("Please enter the amount of money that you would like to bet (without the $): ")
    while True:
        try:
            money_bet = int(input("Please enter the amount of money that you would like to bet (without the $): "))
            while int(money_bet) < 0: #Negative number
                print("Invalid amount! Please enter a valid amount!")
                money_bet = input("Please enter the amount of money that you would like to bet (without the $): ")
            break
        except ValueError:
            print("Invalid amount! Please enter a valid amount!")


    even_odd = input("Will the sum be even or odd? Enter your choice here: ")

    while (not even_odd in even_odd_options):
        print("Invalid input!")
        even_odd = input("Will the sum be even or odd? Enter your choice here: ")

    even_or_odd(money_bet, even_odd) #Calling the function

def choose_play_American_Roulette(): #American Roulette
    print("Welcome to American Roulette")
    print("You currently have $" + str(starting_money) + ".")
    while True:
        try:
            money_bet = int(input("Please enter the amount of money that you would like to bet (without the $): "))
            while int(money_bet) < 0: #Negative number
                print("Invalid amount! Please enter a valid amount!")
                money_bet = input("Please enter the amount of money that you would like to bet (without the $): ")
            break
        except ValueError:
            print("Invalid amount! Please enter a valid amount!")

    category = input("Please enter even, odd, red, black, low (numbers 1 to 18), or high (numbers 19 to 36): ")
    while not(category in possible_options_roulette): #Invalid input
        print("Invalid input!")
        category = input("Please enter even, odd, red, black, low (numbers 1 to 18), or high (numbers 19 to 36): ")

    roulette(money_bet, category)

def choose_play_Highest_Card(): #Who Has the Highest Card?
    print("Welcome to Who Has the Highest Card")
    player_1_name = input("Please enter player one's name: ")
    player_2_name = input("Please enter player two's name: ")
    print("Both players currently have $" + str(starting_money) + ".")
    while True:
        try:
            player_1 = int(input("Please enter the amount of money that Player 1 would like to bet (without the $): "))
            while int(player_1) < 0:
                print("Invalid amount! Please enter a valid amount!")
                player_1 = int(input("Please enter the amount of money that Player 1 would like to bet (without the $): "))
            break
        except ValueError:
            print("Invalid amount! Please enter a valid amount!")

    while True:
        try:
            player_2 = int(input("Please enter the amount of money that Player 2 would like to bet (without the $): "))
            while int(player_2) < 0: #Negative number
                print("Invalid amount! Please enter a valid amount!")
                player_2 = int(input("Please enter the amount of money that Player 2 would like to bet (without the $): "))
            break
        except ValueError:
            print("Invalid amount! Please enter a valid amount!")


    highest_card(player_1, player_2)
menu()
