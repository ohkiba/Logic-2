def make_bricks(small, big, goal):
    smallVal=1
    bigVal=5

    smallTot=small*smallVal
    bigTot=big*bigVal

    #Fail Cases
    if (goal>bigTot+smallTot):
        return False
    if (goal % 5 > smallTot):
        return False
        
    #Success Case
    if (goal//5 <= big):
        if (goal % 5 < smallTot):
            return True
    if (goal % 5 < smallTot):
        if (goal//5 <= big):
        
            return True
