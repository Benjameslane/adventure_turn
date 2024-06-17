from game_logic.first_decision import first_decision

def start_game():
    name = input('What is your Name?: ')
    print(f"""Greetings {name}! Ive got some good news and I have some bad news.\n The good news is that you have been accepted into YAC! (Young Alchemists Club).. \n The bad news is you just woke up in an Ancient dungeon and have no idea how you got here.""")
    first_decision()

if __name__ == "__main__":
    start_game()
