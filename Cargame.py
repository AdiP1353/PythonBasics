started = False
while True :
    command = str(input("> ").lower())
    if command == "help":
        print("""
start - to start the car
stop - to stop the car 
quit - to exit
        """)
    elif command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "quit":
        break
    elif command == "starwars":
        print(""" 
            /_|   |_\
           //||   ||\\
          // ||   || \\
         //  ||___||  \\
        /     |   |     \    _
       /    __|   |__    \  /_\
      / .--~  |   |  ~--. \|   |
     /.~ __\  |   |  /   ~.|   |
    .~  `=='\ |   | /   _.-'.  |
   /  /      \|   |/ .-~    _.-'
  |           +---+  \  _.-~  |
  `=----.____/  #  \____.----='
   [::::::::|  (_)  |::::::::]
  .=----~~~~~\     /~~~~~----=.
  |          /`---'\          |
   \  \     /       \     /  /
    `.     /         \     .'
      `.  /._________.\  .'
   LS   `--._________.--'     Modified Corellian YT-1300 Transport (4)
     """)
    else:
        print("I don't understand...")