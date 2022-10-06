# Declaring Variables
fullName = input("Enter your FullName:")
course = input("Enter your Course Major:")
subject = input("Enter your Sr-code:")
prelimGrade = input("Enter your PrelimGrade:")
midtermGrade = input("Enter your MidtermGrade:")
semisGrade= input("Enter your SemisGrade:")
finalGrade = input("Enter your FinalGrade:")

# Simulation of Variables

print("Name:"+str(fullName))
print("Course:"+str(course))
print("Subject:"+str(subject))
print("PG:"+str(prelimGrade))
print("MG:"+str(midtermGrade))
print("FG:"+str(finalGrade))

# Computation for Grade
result1 = float(prelimGrade)*.25
result2 = float(midtermGrade)*.25
result3 = float(semisGrade)*.25
result4 = float(finalGrade)*.25
semestralGrade = (float(result1)+float(result2)+float(result3))+float(result4)
print("SG="+str(semestralGrade))

# Conditional statement
if (semestralGrade >= 0) and (semestralGrade <= 74):
    print("Remarks:FAILED")
    print("It will be okay! You still have a bright future ahead of you.")
elif (semestralGrade >= 75) and (semestralGrade <= 100):
    print("Remarks:PASSED")
    print("Congratulations on your accomplishment!")
elif (semestralGrade >= 101) or (semestralGrade <= 0):
    print("Remarks:INC")