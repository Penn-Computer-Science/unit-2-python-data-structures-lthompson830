grades = {"Greg" : ["80%", "79%", "88%"], "Steve" : ["95%", "100%", "89%"], "Van" : ["0%", "20%", "15%"]}
while quit != ("yes"):
    print("Welcome to the Gradebook")
    quit = input("Would you like to quit? ")
    menu = input("Would you like to add a student or see the grade summery? (student / grade / check) ")
    if menu == ("student"):
        addname = input("What is the student's name? ")
        grade1 = input("What is the studen's first grade? ")
        grade2 = input("What is the student's second grade? ")
        grade3 = input("What is the student's third grade? ")
        grades[addname] = [grade1, grade2, grade3]

    if menu == ("grade"):
        change = input("Which student would you like to change? ")
        if change == ("Greg" or "greg"):
            ggrade1 = input("What is Greg's first grade? ")
            ggrade2 = input("What is Greg's second grade? ")
            ggrade3 = input("What is Greg's third grade? ")
            grades["Greg"] = [ggrade1, ggrade2, ggrade3]
        
    if menu == ("check"):
        print(grades)