import os
def foodJudge(argSen):
    foodword=['ご飯','おいしい','ごはん','カレー','うどん','そば','お箸']
    for i in foodword:
        if i in argSen:
            return True
    return False
