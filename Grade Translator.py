#       This program converts your numeric grade into a your letter grade.

#Create a loop for program to keep initializing
#Prompt user to enter a numeric grade
while True:
  grade_num = int(input("Please enter numeric a grade [0-10]: "))

#Create a grade for an 'A'
  if grade_num == 9 or grade_num == 10:
    grade = "A"

#Create a 'B' for a grade of 8
  elif grade_num == 8:
    grade = "B"    

#Create a 'C' for a grade of 7
  elif grade_num == 7:
    grade = "C"

#Create a 'D' for a grade of 6
  elif grade_num == 6:
    grade = "D"

#Create a range for lower grades to 'F'
  elif grade_num in range(1,6):
    grade = "F"

#Create a 'Nonexistent' entry for a 0  
  elif grade_num == 0:
    grade = "Nonexistent"

#Create 'Invalid Entry' for everything else
  else:
    print("Invalid Entry! You fail for not following the rules.\n")
    continue

#Print the conversion for user
  print("For the grade you entered ",grade_num,"the corresponding letter grade is ",grade)

#Ask user if they would like to continue with conversions
#Create necessary response to values entered
  answer = input("\nWould you like to convert another grade? [y/n] ")
  if answer == "n":
    break
  elif answer == "y":
    continue
  else:
    print("Invalid entry!\n")
