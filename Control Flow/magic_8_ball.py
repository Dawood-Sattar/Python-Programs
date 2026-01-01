# In Python, modules are .py files containing Python code that can be imported inside another Python program. inside module multiple function are there
# Python standard library consistor of more than 200 modules

'''

The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

It's an oversized 8 ball with some of the following answers:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.
Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

'''
import random

num=random.randint(1,9)

question=input('Ask me a YES or NO question : ')

if num==1:
    print('Yes - definitely.')
elif num==2:
    print('It is decidedly so. ')
elif num==3:
    print('Without a doubt.')
elif num==4:
    print('Reply hazy, try again.')
elif num==5:
    print('Ask again later.')
elif num==6:
    print('Better not tell you now.')
elif num==7:
    print('My sources say no.')
elif num==8:
    print('Outlook not so good.')
else:
    print('Very doubtful.')