import random
def hobbies(argSen,pm=0):
    reslistPlus = ['めっちゃいいやん！','すごいやん','やっぱ君最高すぎ！','天才やん','素晴らしい','そうなんですね!', '面白そう','どのくらいの頻度するの?','いいね！','いいセンスしてるね','趣味会うかも','その趣味は生かしてるね','それはイケてるね','君のセンスは最高だね']
    reslistMinus = ['つまんない趣味だね','センスがない','それはなくね','あまりいいと思わない','ふーん、つまらないね','あまり良いとは感じないなー','気に入らないかも','なんか変わってるね','それって面白いの？','何が面白いのか分からん','おもんなさそう','何が楽しいの？','退屈そう']
    if(pm==1):
        return reslistPlus[random.randint(0,(len(reslistPlus)-1))]
    return reslistMinus[random.randint(0,(len(reslistMinus)-1))]
    