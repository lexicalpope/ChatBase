import random
def tripTalk(argSen,pm=0):
    reslistMinus = ['効率的にやれよ','こんなこともできんのか','納期に間に合ってないけど？','前の部下はもっとできたんだけどな','もっとできただろ','前も同じミスしてたよね','言い訳するなよ','遅れるなら連絡しろよ','何度も同じこと聞くなよ','残業ばっかりだよね','部下の教育ができてないんじゃない？']
    reslistPlus = ['よくやった','素晴らしい','優秀だね','君に任せて良かった','あんまり無理するなよ','ちゃんと休めてる？','自分のペースで進めれば良いよ','真面目に働いててすごいよ！','福利厚生って大事だよね']

    if (pm==1):
        return reslistPlus[random.randint(0,(len(reslistPlus)-1))]
    return reslistMinus[random.randint(0,(len(reslistMinus)-1))]