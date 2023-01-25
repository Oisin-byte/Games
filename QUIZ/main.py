print('Welcome to AskPython Quiz')
answer=input('Are you ready to play the quiz ? (yes/no) ')
score=0
total_questions=3

if answer.lower()=='yes':
    answer=input('Question 1: What is your Favorite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
        print(' Your current score is ', score)
    else:
        print('Wrong Answer :(')
    

    answer=input('Question 2: Do you follow any author on github?')
    if answer.lower()=='yes':
        score += 1
        print('correct')
        print(' Your current score is ', score)
    else:
        print('Wrong Answer :(')

    answer=input('Question3: What is the name of your favorite website for coding tutorials')
    if answer.lower()=='askpython':
        score += 1
        print('Correct')
        print(' Your current score is ', score)
    else:
        print('Wrong answer :(')
    
print('Thank you for playing Oisíns Quiz, you attempted', score, 'questions correclty')
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')