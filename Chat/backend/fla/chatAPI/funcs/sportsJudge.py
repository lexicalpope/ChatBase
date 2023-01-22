import os
def sportsJudge(argSen):
    with open(str(os.getcwd())+'/fla/chatAPI/datas/sports.txt','r',encoding="utf-8") as f:
        kw_list = f.read().split("\n")

    for val in kw_list:
        if(val in argSen):
            return True
    return False