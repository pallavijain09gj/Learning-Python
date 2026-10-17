
#Questions for 8th class students

Questions = ["1. What is the square of 15?",
 "2. Solve 3x + 5 = 20",
 "3. What is the cube of 4?",
 "4. The sum of the angles of a triangle is?",
 "5. A shirt costs 800. If a discount of 10% is given, what is the final price?"]

Options = [["a. 225", "b. 250", "c. 275", "d. 300"],
              ["a. 5", "b. 10", "c. 15", "d. 20"],
              ["a. 64", "b. 72", "c. 80", "d. 100"],
              ["a. 90 degrees", "b. 180 degrees",
               "c. 270 degrees", "d. 360 degrees"],
              ["a. 720", "b. 750", "c. 800", "d. 850"]]

Answers = ["a", "b", "a", "b", "b"]     

Price_Money = [100,100,100,100,100]

amount = 0

for i in range(len(Questions)):
    print(Questions[i])
    for j in range(len(Options[i])):
        print(Options[i][j])
    ans = input("Enter your answer (a/b/c/d): ")
    if ans.lower() == Answers[i]:
        print("Correct answer!")
        amount += Price_Money[i]
    else:
        print("Wrong answer! The correct answer is:", Answers[i])
    print()
print("Total amount won:", amount)
