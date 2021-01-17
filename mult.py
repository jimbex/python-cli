# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:36:50 2020

@author: jago
"""
from prompt import Questions

Multiplechoice = [
    "What is the colour of rose \na. blue\nb. green\nc. red\n\n",
    "what is the colour of rice \na. black\nb. white\nc. grey\n\n",
    "What is the colour of the sea \na. red\nb. blue\nc. green"
    ]

question = [
    
    Questions(Multiplechoice[0], "c"),
    Questions(Multiplechoice[1], "b"),
    Questions(Multiplechoice[2], "b")
    
    ]


def run_test(question):
    Score = 0
    for q in Multiplechoice:
       print(question.paper)
       answer = input()
       if answer == question.answer:
           Score += 1
    print("You got " + str(Score) + "/" + str(len(question)) + " correct")
            
run_test(question)
        
    
    

    

