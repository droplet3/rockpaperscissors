import random

RPS = ["Rock", "Paper", "Scissors"]

def get_rps():
    gamerps = random.randint(0, 2)
    gamechoice = RPS[gamerps]
    return gamechoice.lower()


def get_userinput():
    while True:
        user_input = str.casefold(input("Rock, Paper or Scissors?: "))
        if user_input.lower() in ["rock", "paper", "scissors"]:
            return user_input.lower()
        else:
            print("Invalid Choice")
            


def main():
    user_input = get_userinput()  # Call the function to get user input
    gamechoice = get_rps()

    if gamechoice == user_input:
        print(f"User Draws! it was {gamechoice}")
    else:
        winning_combos = [("paper", "rock"), ("scissors", "paper"), ("rock", "scissors")] #tuples in a list
        if (user_input, gamechoice) in winning_combos:
            print(f"User Wins! it was {gamechoice}")
        else:
            print(f"User Loses! it was {gamechoice}")



if __name__ == "__main__":
   main()