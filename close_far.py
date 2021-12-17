def close_far(a, b, c):

    if (abs(abs(a)-abs(b))<=1):
        close=b
        far=c
    if (abs(abs(a)-abs(c))<=1):
        close=c
        far=b

    if (abs(abs(a)-abs(far))>=2 and abs(abs(close)-abs(far))>=2):
        return True
    
    return False
        