import os
def physicalconditionJudge(argSen):
    with open(str(os.getcwd())+'/fla/chatAPI/datas/physicalcondition.txt','r',encoding="utf-8") as f:
        kw_list = f.read().split("\n")
    for val in kw_list:
        if(val in argSen):
            print(val)
            return True
    return False