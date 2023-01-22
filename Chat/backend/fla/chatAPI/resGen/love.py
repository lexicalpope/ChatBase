import random
def love(argSen,pm=0):
    reslistPlus = ['ええなー','うらやましい','モテモテやね','おめでとう','最高やな','幸せそうやなあ','いいね']
    reslistMinus = ['振られてしまえ','恋愛してる場合かよ','しょうもないな','あんたのこと誰が好きになるん','そんな時間ないやろ','そんなことしてる場合やないやろ']
    if(pm==1):
        return reslistPlus[random.randint(0,(len(reslistPlus)-1))]
    return reslistMinus[random.randint(0,(len(reslistMinus)-1))]
    