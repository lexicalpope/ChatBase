import random

def music(argSen,pm=0):
    reslistPlus = ['その音楽めっちゃいいやん','俺も聞いてるで','聞いてみたい','素敵やね','いいね','曲調が好き','私もよく聞く！','ライブ行きたいね','ライブ行ったことある？','どんなジャンルが好きなの？','そのジャンルが好きなの？','流行ってる','それマジでいいきょくだよね','聴いてると癒されるよね','流れてるとテンション上がる','知ってる、私も好きだよ','それ私も好きだよ','いいよねそれ、センスあるね君']
    reslistMinus = ['聞いたことないわ','それ全然良くないで','その音楽ダサい','へー','全然興味ないわ','センスないな','ミーハーだな','それみんな知ってる','何それ','その曲かっこいいか？','誰が聞くねん','それはあんまり好きじゃない','ミーハーなんだね','音楽の方向性が違う','それはセンスないね','音楽なんて聴いてる暇ない','音楽好きじゃない','趣味悪いね','趣味古いね']

    if(pm==1):
        return reslistPlus[random.randint(0,(len(reslistPlus)-1))]
    return reslistMinus[random.randint(0,(len(reslistMinus)-1))]