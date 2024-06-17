from game_logic.lose_game import game_over
from game_logic.win_game import win_game

def vine_door():
    print(f"\nYou push open the vine-covered door and enter a lush garden with a bubbling fountain in the center. Do you drink from the fountain or explore the garden?")
    choice = input(f"\nA) Drink from the fountain\nB) Explore the garden\n").strip().lower()
    if choice == 'a':
        print(f'The water is refreshing, but suddenly you feel dizzy and collapse. It was poisoned!')
        game_over()
    elif choice == 'b':
        print(f'You find a hidden path behind a large bush that leads to a hidden exit. You have successfully escaped!')
        win_game()
    else:
        print(f'Sorry, there is no option like that available. Pick again.')
        vine_door()
