import random
def bougen(argSen):
    reslist = ['うざい','だまれ','意味不明','ちょっとだまってよ','つまんないこというね']
    return reslist[random.randint(0,(len(reslist)-1))]