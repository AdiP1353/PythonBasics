player_name = input("Enter player name: ")
ready = input("Are you ready (Y/N) ? ")
if ready == "Y" :
    print("Let's go!")
elif ready == "N" :
    del player_name
    player_name = input("Enter player name: ")          