def make_chocolate(small, big, goal):
    smallVal=1
    bigVal=5
    newGoal=0

    smallTot=small*smallVal
    bigTot=big*bigVal

    #Fail Cases
    if (goal>bigTot+smallTot):
        return -1
    if (goal % 5 > small):
        return -1
    
    #Success Case
    if (goal % 5 <= small):
        if (goal//5<=big): #does not require all bigs + partial small remainder
            newGoal=goal-(goal//5)*bigVal
        else: #requires all bigs + partial small remainder
            newGoal=goal-bigTot
    return newGoal
    
