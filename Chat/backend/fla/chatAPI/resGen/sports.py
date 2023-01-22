import random

def sports(argSen,pm=0):
    reslistPlus = ['めっちゃいいやん','最高','天才やん','素晴らしい','面白そう','いいね','とても上手','前より上達したね','すごい活躍だったね','今日のヒーローだね','運動するのが楽しいよね','なんでもできるよね、すごい','うまいね、運動神経いいんだ','運動は、体にいいよね','体を動かすと、気分いいよね','活躍できると最高だよね']
    reslistMinus = ['下手くそ','今日の戦犯はお前だな','やめた方がいいんちゃう','帰れよ','運動なんてする意味ないよ','スポーツより仕事しなよ','遊んでいいの？そんな暇ないよ','君下手だね','君、運動神経悪すぎ']

    if(pm==1):
        return reslistPlus[random.randint(0,(len(reslistPlus)-1))]
    return reslistMinus[random.randint(0,(len(reslistMinus)-1))]
    