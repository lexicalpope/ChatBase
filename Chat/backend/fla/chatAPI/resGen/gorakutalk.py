import random
def goraku(argSen,pm=0):
    reslistPlus = ['一日中楽しめそうやね','あのアトラクションめっちゃ面白いよね','次は何乗る？','めっちゃ楽しいね！','パレードめっちゃ良かったよね！','ジェットコースターが最高すぎる','楽しい気分になるよね','テンションめっちゃあがるよね','夢の空間だよねー','新アトラクション楽しみすぎる','あの乗り物楽しいよね']
    reslistMinus = ['人多いじゃん','子供っぽいね','歩くのだるい','飽きた','何が楽しいの？','入場料高すぎじゃない？','待ち時間が嫌やわ','私、人多いとこ嫌い','わざわざそんな人ごみに行く必要がない','お金はらってそんなことする意味がない','わざわざしなくていい','つまんなそうに思ったな']
    if(pm==1):
        return reslistPlus[random.randint(0,(len(reslistPlus)-1))]
    return reslistMinus[random.randint(0,(len(reslistMinus)-1))]
    