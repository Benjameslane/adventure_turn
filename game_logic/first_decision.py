from game_logic.iron_door import iron_door
from game_logic.vine_door import vine_door
from game_logic.wooden_door import wooden_door


def first_decision():
    print(f"""\nAs you stand up and check your surroundings. You notice three doors before you. 
          \n A) An Wooden Door. 
          \n B) A Vine-Covered Door
          \n C) and an Iron Door """)
    print(f'\n')
    choice = input('Which direction would you like to go?: ').strip().lower()
    if choice == 'a':
        wooden_door()
    elif choice == 'b':
        vine_door()
    elif choice == 'c':
        iron_door()
    else:
        print(f'Sorry, there is no path like that available. Pick again.')
        first_decision()