def stress():
    stressvalue = force/area
    stressvalue = "{:.2e}".format(stressvalue)
    print(stressvalue)
    force += 1
    

extension = 1e-4
force = 1
area = 1.08e-7   

while force <= 10:
    stress()
    