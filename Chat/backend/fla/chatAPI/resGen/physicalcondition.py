import random

def physicalcondition(argSen,pm=0):
    reslistPlus = ['大丈夫？','よく頑張っているね','素晴らしい','いいね','病院には行った？','お大事に','健康が一番大事だよね','ほんと、お大事にね','体調万全にしたいね','つかれたときは、休んでいいよ','いつもお疲れ様、自分に優しくね。']
    reslistMinus = ['もっと働け','逃げるのは簡単でいいな','お前は楽でいいな','甘えるな','絶対仮病やん','休みすぎじゃない？','病院行き過ぎるのもね','それくらい、一日ねれば治るだろ','薬に頼りすぎ','そんなこと言ってたら何もできない','さぼらず働けよ']

    if(pm==1):
        return reslistPlus[random.randint(0,(len(reslistPlus)-1))]
    return reslistMinus[random.randint(0,(len(reslistMinus)-1))]
    