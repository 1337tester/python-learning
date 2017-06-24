# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 17:23:03 2016

@author: Miso
"""

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    import random
    success = 0
    for i in range(numTrials):
        pick = 0
        balls = [1,1,1,1,0,0,0,0]
        for i in range(3):
            choice = random.choice(balls) 
#            print(choice)
            balls.remove(choice)
            pick += choice
#            print(balls.pop(choice))
        if pick in [0,3]: success += 1
    return success/numTrials
        
        
        

print(drawing_without_replacement_sim(100))