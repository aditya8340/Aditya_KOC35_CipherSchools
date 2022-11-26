print("welcome to my python quiz")
playing=input("Do you want to play? ")
if playing != "yes":
    quit()
else:    print("okay! Here we go ! :) ")
score = 0
answer = input("is the coding language python named after the snake? ")
if answer== "no":
        print("congratulation your answer is correct!")
        score +=  1
else:
        print("answer is incorrect!") 
answer = input("Who is the inventor of difference engine? ")
if answer== "charles babbage":
    print("congratulation your answer is correct!")  
    score +=  1
else:
          print("answer is incorrect!")     
answer = input("who is the father of computer science? ")     
if answer== "allen turing":
    print("congratulation your answer is correct!")
    score +=  1
else:
       print("answer is incorrect!")
answer = input("what is the full form of UNIVAC? ")       
if answer== "universal automatic computer":
    print("congratulation your answer is correct!")
    score +=  1
else:
     print("answer is incorrect!")
answer = input("how many elements are there in the periodic table? ")
if answer== "118":
     print("congratulation your answer is correct!")
     score +=  1
else:
      print("answer is incorrect!")
answer = input("which company was originally called cadabra? ")
if answer== "amazon":
        print("congratulation your answer is correct!")
        score +=  1
else:
         print("answer is incorrect!")   
print("you got " + str(score) + "question correct!")
print("you got " + str(score/6 *100) + "%. ")
