score = 0

input("The rules of the game are simple: \n"
      "1. Answer the questions as they come \n"
      "2. If you do not know an answer, you can type 'skip' to move onto the next question \n \n"
      "When you are ready, hit the 'Enter' key...")

while True:
    try:
        question_1 = input("What is Jerry's apartment number?")
        if question_1 == "skip":
            print("Okay, we'll skip that one.")
            break;
        elif question_1 == "5a" or question_1 == "5A":
            score+=1
            print("That is correct!.  Your score is " + str(score))
            break;
        else:
            print("Nope, try again...")
    except ValueError:
        print("Provide a valid string value...")
        continue

while True:
    try:
        question_2 = input("What is George's bank card pin number?")
        if question_2 == "skip":
            print("Okay, we'll skip that one.")
            break;
        elif question_2 == "Bosco" or question_2 == "bosco" or question_2 == "BOSCO":
            score+=1
            print("That is correct!.  Your score is " + str(score))
            break;
        else:
            print("Nope, try again...")
    except ValueError:
        print("Provide a valid string value...")
        continue

while True:
    try:
        question_3 = input("Who was George's main competition when selling computers?")
        if question_3 == "skip":
            print("Okay, we'll skip that one.")
            break;
        elif question_3 == "Lloyd Braun" or question_3 == "lloyd braun" or question_3 == "LLOYD BRAUN":
            score+=1
            print("That is correct!.  Your score is " + str(score))
            break;
        else:
            print("Nope, try again...")
    except ValueError:
        print("Provide a valid string value...")
        continue

while True:
    try:
        question_4 = input("What type of bread did Jerry still from the old lady?")
        if question_4 == "skip":
            print("Okay, we'll skip that one.")
            break;
        elif question_4 == "Marble Rye" or question_4 == "marble rye" or question_4 == "MARBLE RYE":
            score+=1
            print("That is correct!.  Your score is " + str(score))
            break;
        else:
            print("Nope, try again...")
    except ValueError:
        print("Provide a valid string value...")
        continue

print("Out of four questions, you answered " + str(score) + " questions correctly.")