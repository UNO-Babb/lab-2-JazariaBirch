#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["Very likely.", "Not Possible." ,"Dont count on it.","It is certain.", " It is decidedly so.",
             "My reply is no." , "My sources say no.", "Outlook not so good.", "Outlook good."
              ,"Reply hazy, try again.","Yes.","No.","Fortune is on your side", "Try again Tomorrow"
              "As i see it, yes.", "Go for it."]
  #Answer question randomly with one of the options from your earlier list.
  question = input("Ask a yes or No Question:")
  
  length = len(answers)
  r= random.random() * length

  r = int(r)

  print(r)
  response = answers[r]
  print(response)



if __name__ == '__main__':
  main()
