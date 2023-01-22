import os
def musicJudge(argSen):
    with open(str(os.getcwd())+'/fla/chatAPI/datas/music.txt','r',encoding="utf-8") as f:
        kw_list = f.read().split("\n")

    for val in kw_list:
        if(val in argSen):
            return True
    return False