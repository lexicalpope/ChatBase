import os
def tripJudge(argSen):
    words=['旅','旅行','温泉','海外']
    for w in words:
        if w in argSen:
            return True
    return False