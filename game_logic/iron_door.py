from game_logic.lose_game import game_over
from game_logic.win_game import win_game

def iron_door():
    print(f'As you approach the Iron Door, you notice that The iron door is sealed with an ornate lock that seems almost impossible to pick at first glance. You notice two possible options to proceed. ')
    choice = input(f"""\nA) Attempt to Pick the Lock
            \nB) Search for a key nearby""").strip().lower()
    if choice == 'a':
        print('The lock proves to be too complex. As you fumble with the mechanisms, you accidentally trigger a trap. A sudden rush of sleeping gas fills the corridor, and you lose consciousness')
        game_over()
    elif choice == 'b':
        print (f'You explore the area around the door and find a loose brick in the wall. Behind it is a hidden compartment containing an old, rusty key. You insert the key into the lock, and the door creaks open, revealing a dark corridor lit by faint torches.')
        win_game()
    else:
        print(f'Sorry, there is no option like that available. Pick again.')
        iron_door()
    
    