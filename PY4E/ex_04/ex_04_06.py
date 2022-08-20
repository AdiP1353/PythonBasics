#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime 
# and create a function called computepay which takes two parameters (hours and rate).


def computepay(hrs, payperhour):
    
    multiplier = 1.5
    h = float(hrs)
    
    if h < 40:
        gross_pay = h * payperhour
        print(gross_pay)
    else:
        rem = float(h - 40)
        gross_pay = (40 * payperhour) + (rem * multiplier * payperhour)   
        print(gross_pay)
        
        
computepay(45, 10.50)