from game_logic.solve_riddle import solve_riddle

def wooden_door():
    print(f"\n The wooden door creaks open to reveal a dimly lit room with a riddle on the wall. Do you solve the riddle or look for another way out?")
    print(f"\n A) Solve Riddle \n B) Find another way out")
    choice = input(f"What do you choose?: ").strip().lower()
    if choice == 'a':
        solve_riddle()
    elif choice == 'b':
        print(f'Sorry, there is no other way')
        wooden_door()
