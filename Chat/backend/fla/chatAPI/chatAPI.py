from .funcs import judge
def mainProcess(argSen):
    res = judge.judge(argSen)
    if(argSen=='つかれた'):
        res='さよなら'
    return res



