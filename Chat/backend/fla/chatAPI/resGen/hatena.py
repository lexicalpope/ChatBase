import random

def hatena(argSen):
    reslist = ['私に質問しないで','しらねーよ','知らん','考えろよ','質問すんなよ','自分で考えろ']
    return reslist[random.randint(0,(len(reslist)-1))]