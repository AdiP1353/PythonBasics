#guessing game , magic number is 9
guess = input("Guess: ")
number = 9
no_guess = 0
i = 0
while i == 0:
    while no_guess <= 2:
        if no_guess == 2 and int(guess) != number:
            print("You failed, please try again!")
        if int(guess) != number:
            no_guess += 1
            guess = input("Guess: ")
        elif int(guess) == number:
            no_guess = 0
            print("You win!")
            i += 1
       
    
    
