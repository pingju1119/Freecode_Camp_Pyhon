"Classes and Objects"
#Class: create any data type you want,
# except strings, numbers, boolean types.
# we create a data type named student in student.py
#it means ther is a student template, then we can
#creat a student object below

from Student import Student

student1=Student("Ellie","Art",3.9,False)

student2=Student("Elliott","Music",3.9,False)
print(student1)
print(student1.name)
print(student2.name)
print(student2)

"Build a multipla choice quiz"

from Question import Question
question_prompts =[
    "what color are apples?\n(a) Red/green \n(b) white\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
#print(question_prompts)

questions=[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score =0
    for question in questions:
        answer= input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) +"/"+ str(len(questions))+" correct.")


run_test(questions)



