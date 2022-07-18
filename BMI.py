weight = float(input("Weight in Kg: "))
height = float(input("Height in Cm: "))
BMI = (weight/(height/100)**2)
if BMI < 16 :
    message = "severely underweight"
elif BMI >= 16 and BMI < 17 :
    message = "moderately underweight"
elif BMI >= 17 and BMI < 18.5 :
    message = "mildly underweight"
elif BMI >= 18.5 and BMI < 25 :
    message = "normal weight"
elif BMI >=25 and BMI < 30 :
    message = "overweight"
elif BMI >= 30 and BMI < 35 :
    message = "severely overweight (Class I)"
elif BMI >= 35 and BMI < 40 :
    message = "severely overweight (Class II)"
elif BMI >= 40 :
    message = "severely overweight (Class III)"
    
print("This is your BMI: " + str(round(BMI, 2)))
print("This is considered " + str(message))
print("NB : This is not a useful tool for athletes")


