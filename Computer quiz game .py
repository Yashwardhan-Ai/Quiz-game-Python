print("Welcome to my computer quiz game !")

playing = input("Do you want to play my game ?")
print(playing)
score=0
if playing.lower() != "yes":
    quit()
else : 
    print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Wrong answer!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Wrong answer!")
    
answer = input("What does Ram stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Wrong answer!")

answer = input("What does Rom stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score+=1
else:
    print("Wrong answer!")
if score >= 3 :
    print ("You got " + str(score) + " questions correct , that's fantastic!")
elif score == 2:
    print("You got " + str(score) + " questions correct, that ain't bad at all homie !")
else:
    print("You got "+ str(score) + " questions correct, hey better luck next time , give it a try again" )
    
print("That is " + str((score / 4) * 100)+ "%")