#Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". 
# Once "done" is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, 
# detect their mistake using try and except and print an error message and skip to the next number.



    


    

while True:
    
    user_input = input(">")
    
    #try:
    conv_input = int(user_input)
        
    while user_input != "done":
        count = 0
        for numbers in conv_input:
            count += 1
            
        total_sum = 0
        for numbers in conv_input:
            total_sum += numbers
            
        average = total_sum/count
    #except:
        
        #if user_input == "done":
            #print(f"Count: {count}")
            #print(f"Sum: {total_sum}")
            #print(f"Average: {average}")
       #else: 
            #print("Please enter an integer")
        
 
             
             