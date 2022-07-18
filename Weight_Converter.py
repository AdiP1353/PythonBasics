from email.mime import multipart


weight = float(input("Weight: "))
measure = input("(K)g or (L)bs: ")
multiplier = float("2.20462")
if measure.lower() == "k" :
    kg_lb = str(weight*multiplier)
    print("Weight in lbs: " + kg_lb)
elif measure.lower() == "l" :
    lb_kg = str(weight/multiplier)
    print("Weight in kgs: " + lb_kg)

