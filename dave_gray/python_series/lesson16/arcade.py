import sys
from rps import rps
from guess_number import guess_number

def play_game(name='PlayerOne'):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f'\n{name}, welcome back to the Arcade menu')
            
        playerchoice = input(
            "\nPlease choose a game:\n1. Rock, Paper, Scissors\n2. Guess the Number\n\n Or press \"x\" to exit the arcade\n\n")
        
        if playerchoice not in ["1","2","x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            
        welcome_back = True
        
        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_number = guess_number(name)
            guess_number()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")
            
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Provides a personalised game experience."
    )
            
    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )
    
    args = parser.parse_args()
    
    print(f"\nWelcome to the arcade, {args.name}! 🤖")
    
    play_game(args.name)        