'''
Author: Jacob Pawlak
Author email: jacob.pawlak@uky.edu, ijprat01@louisville.edu
Version: 1.0.0
Start Date: December 18th, 2015


This is a program that will take atendance, grade quizzes, and maybe more.
You can imagine this as a simple database managment system, all files will
have to be in the same folder as this .py file or the program will not load
the files.
'''

####

'''
Notes, Critiques, Bug reports:

please put any notes or problems you have run into in this box 

'''
#get_menu_choice
def get_menu_choice():

    print()
    print("Main Menu")
    print("1. Load Class")
    print("2. Display Class")
    print("3. Save Class")
    print("4. Make A New Class")
    print("5. Make A New Quiz with Key")
    print("6. Grade a quiz")
    #print("7. ")
    print("0. Exit")

    choice = input("Choose an item from the menu: ")
    valids = ['1', '2', '3', '4', '5', '6', '0']
    while(choice not in valids):
        print("That choice is not on the menu, please try again")
        choice = input("Choose an item from the menu: ")

    return choice

#load_class

def load_class():

    print()
    print("Load a class into the program")
    opened = False
    while(not opened):
        try:
            fileName = input("Enter the file name (same as the class name without the .txt): ")
            fileName += ".txt"
            newFile = open(fileName, 'r')
            opened = True
        except IOError:
            print("Error opening file, please try again.")

    classList = []

    for line in newFile:

        line = line.rstrip()
        line = line.split(',')
        classList.append(line)

    newFile.close()

    print("Class Loaded")
    input("Press ENTER")
    

    return classList

#display_class

def display_class(classList):
    
    #maximum column size is 20
    print()
    print("Name                Year                Class               Grade               ")

    for item in classList:
        name = item[0]
        year = item[1]
        clas = item[2]
        grade = item[3]
        if(len(name) < 20):
            name += (" " * (20-len(name)))
        elif(len(name) > 20):
            name = name[0:20]
        if(len(year) < 20):
            year += (" " * (20-len(year)))
        elif(len(year) > 20):
            year = year[0:20]
        if(len(clas) < 20):
            clas += (" " * (20-len(clas)))
        elif(len(clas) > 20):
            clas = clas[0:20]
        if(len(grade) < 20):
            grade += (" " * (20-len(grade)))
        elif(len(grade) > 20):
            grade = grade[0:20]
        print(name + year + clas + grade + "\n")

    return

#save_class

def save_class(classList):

    print()
    print("Save a class")
    fileName = input("Enter the file name (same as the class name without the .txt): ")
    fileName += ".txt"
    newFile = open(fileName, 'w')
    for student in classList:
        newFile.write(student[0] + ',' + student[1] + ',' + student[2] + ',' + student[3] + "\n")

    newFile.close()

    print("Class Saved")
    input("Press ENTER")
    
    return

#make_new_class

def make_new_class():

    print()
    print("Making a new class")
    numStudents = int(input("How many students are in the new class? "))
    fileName = input("What is the new class called (used for file name, without .txt)? ")
    fileName += ".txt"
    newFile = open(fileName, 'w')
    print()
    
    for i in range(numStudents):
        name = input("Student's full name: ")
        year = input("Student's year (k-8): ")
        clas = input("What class is this student in? ")
        grade = float(input("Student's current grade (0 if new entry): "))
        newFile.write(name + ',' + year + ',' + clas + ',' + str(grade) + "\n")
        print()
        
    newFile.close()
    print("New Class Created and Saved")
    input("Press ENTER")

    return

#make_new_quiz

def make_new_quiz():

    print()
    print("Make A New Quiz/Key")
    quizName = input("Name of the quiz (ex. quiz1): ")
    quizKey = quizName + "key.txt"
    quizName += ".txt"
    
    quizFile = open(quizName, 'w')
    keyFile = open(quizKey, 'w')
    print()

    numQuestions = int(input("How many questions on this quiz? "))

    valids = ["mc", "tf"]

    for i in range(numQuestions):
        qType = input("What type of question ('mc' for MultiChoice, 'tf' for TrueFalse)? ")

        while qType not in valids:
            print("Please use 'mc' or 'tf'")
            qType = input("What type of question ('mc' for MultiChoice, 'tf' for TrueFalse)? ")

        if(qType == "mc"):
            question = input("What is the question? ")
            ans1 = input("Choice a: ")
            ans2 = input("Choice b: ")
            ans3 = input("Choice c: ")
            ans4 = input("Choice d: ")
            ansValid = ['a', 'b', 'c', 'd']
            correct = input("Which answer is correct (a,b,c,d)? ")
            while correct not in ansValid:
                print("Please pick from (a,b,c,d)")
                correct = input("Which answer is correct (a,b,c,d)? ")
            quizFile.write(str(i+1) + ". " + question + "\n\t" + "a) " + ans1 + "\n\t" + "b) " + ans2 + "\n\t" + "c) " + ans3 + "\n\t" + "d) " + ans4 + "\n\n")
            keyFile.write(correct + "\n")
            
            
        elif(qType == "tf"):
            question = input("What is the question? ")
            ansValid = ["true", "false"]
            correct = input("True or False? ")
            correct = correct.lower()
            while correct not in ansValid:
                print("Please pick True or False")
                correct = input("True or False? ")
                correct = correct.lower()
            quizFile.write(str(i+1) + ". " + question + "\n\tTrue or False?" + "\n\n")
            keyFile.write(correct + "\n")
        print()

    quizFile.close()
    keyFile.close()
    print("Quiz and Key Created")
    input("Press ENTER")
    
    return

#grade_quiz

def grade_quiz():

    print()
    print("Grade A Quiz")
    fileName = input("Enter the name of the key you are grading against (same as the quiz name + 'key')? ")
    fileName += ".txt"
    keyFile = open(fileName, 'r')
    studentQuiz = input("Enter the student's quiz file, or 'DONE' to stop. ")
    studentQuiz += ".txt"
    print()
    
    while(studentQuiz != "DONE"):
        studentFile = open(studentQuiz, 'r')
        numWrong = 0
        for line in keyFile:
            if (keyFile[line] != studentFile[line]):
                numWrong += 1
        print("Student missed", numWrong, "answers")
        studentQuiz = input("Enter the next student's quiz file, or 'DONE' to stop.")
        studentQuiz += ".txt"

        
    return

#main

def main():

    classList = []
    
    print("Welcome to the Tighe classroom software")
    
    menuChoice = get_menu_choice()
    
    while(menuChoice != '0'):

        if(menuChoice == '1'):
            classList = load_class()
            
        elif(menuChoice == '2'):
            display_class(classList)
            
        elif(menuChoice == '3'):
            save_class(classList)
            
        elif(menuChoice == '4'):
            make_new_class()

        elif(menuChoice == '5'):
            make_new_quiz()

        elif(menuChoice == '6'):
            grade_quiz()
            
        menuChoice = get_menu_choice()
        
    input("Press ENTER")
main()
