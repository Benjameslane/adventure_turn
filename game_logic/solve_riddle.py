from game_logic.win_game import win_game
from game_logic.lose_game import game_over

def solve_riddle():
    print(f"I have keys but open no locks. I have space but no room. You can enter, but you can't go inside. What am I?")
    answer = input(f"\nWhat is your answer?: ").lower()
    if answer == 'keyboard':
        print(f"A door magically appears where the riddle once was, opening into a grassy meadow. You have made it out!\n")
        win_game()
    else:
        print(f"It appears your awnser ws incorrect and the room fills with poison gas..Your eyes slowly begin to close..\n")
        game_over()
