#       This program mimics a magic 8 ball to answer all your questions!

#Create a repeat loop for hours of fun
while True:
  Question = input("Ask the Magic 8 Ball a question: \nTo no longer uncover the secrets type Stop. ")
#Import necessary random module and assign range 
  import random
  n = random. randint(1,5)
#Create a stopping point for the fun
  if Question == "Stop":
    break
#If number is 1 print Yes
  elif n == 1:
      answer = "Yes!\n"
#If number is 2 print No, Sorry
  elif n == 2:
    answer = "No, Sorry\n"
#If number is 3 print Not a Chance!
  elif n == 3:
    answer = "Not a chance!\n"
#If number is 4 print Perhaps?
  elif n == 4:
    answer = "Perhaps?\n"
#If number is 5 print Big Maybe
  elif n == 5:
    answer = "Big Maybe\n"
#Print the answer to user's question    
  print("\nThe answer you seek is:",answer)
