from tkinter import *

# -*- coding: utf-8 -*-
"""
Created on Wed May 20 00:09:33 2020

@author: jago
"""
root = Tk()

score = 0

Multiplechoice = [
    "What is the colour of rose \na. blue\nb. green\nc. red\n\n",
    "what is the colour of rice \na. black\nb. white\nc. grey\n\n",
    "What is the colour of the sea \na. red\nb. blue\nc. green\n\n"
    ]

answers = ["c", "b", "b"]

i = 0

while i < len(Multiplechoice):
    answer = input(Multiplechoice[i])
    if answer == answers[i]:
            score += 1
    i = i + 1
        
print("you got " + str(score) + "/" + str(len(Multiplechoice)))

root.mainloop()
    
