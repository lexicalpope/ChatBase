import random
def tripTalk(argSen,pm=0):
    reslistMinus = ['遠かったんじゃない？','遊んでて大丈夫？','いくら使ったの？','もっと違うところいこうよ','目的ないんかい','退屈そうだな','行く時期おかしいだろ','何しに行ったんだよ','もっと行く場所あるだろ','時間もったいないよ','どこだよ','お土産ないの？','金の無駄だろ','遊んでばっかりだな']
    reslistPlus = ['どこに行ったの','お土産は？','私も行きたい！','次はどこに行く？','リラックスだね！','誰と行ったの？','いつ行ったの？','楽しそう！','いい思い出だね！','いい場所だね！','おいしいもの食べた？','楽しそうだね','観光地いった？','今の時期いいね！','いいね！','うらやましいなー']

    if (pm==1):
        return reslistPlus[random.randint(0,(len(reslistPlus)-1))]
    return reslistMinus[random.randint(0,(len(reslistMinus)-1))]