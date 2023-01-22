import os
from ..resGen import hatena
from ..resGen import bougen
from ..resGen import yasasi
from ..resGen import foodtalk
from ..resGen import hobbies
from ..resGen import tripTalk
from ..resGen import hobbies
from ..resGen import gameTalk
from ..resGen import love
from ..resGen import sports
from ..resGen import gorakutalk
from ..resGen import anime
from ..resGen import music
from ..resGen import physicalcondition
from . import foodJudge
from . import hobbiesJudge
from . import tripJudge
from . import gameJudge
from . import loveJudge
from . import sportsJudge
from . import gorakuJudge
from . import animeJudge
from . import musicJudge
from . import physicalconditionJudge

def judge(argSen):

    #0=minus 1=plus
    pm=0
    if('♡' in argSen or '♥' in argSen or '❥' in argSen or '💓' in argSen or '💔' in argSen or '💕' in argSen or '💖' in argSen or '💗' in argSen or '💙' in argSen or '💚' in argSen or
    '💛' in argSen or '💜' in argSen or '💝' in argSen or '💞' in argSen or '💟' in argSen or '🤍' in argSen or '🤎' in argSen or '❤' in argSen or '❣' in argSen):
        pm=1

    if('?' in argSen or '・・' in argSen):
        return hatena.hatena(argSen)

    if(foodJudge.foodJudge(argSen)):
        return foodtalk.foodtalk(argSen,pm)

    if(sportsJudge.sportsJudge(argSen)):
        return sports.sports(argSen,pm)
        
    if(gameJudge.gameJudge(argSen)):
        return gameTalk.gameTalk(argSen,pm)
        
    if(hobbiesJudge.hobbiesJudge(argSen)):
        return hobbies.hobbies(argSen,pm)
        
    if(loveJudge.loveJudge(argSen)):
        return love.love(argSen,pm)
    
    if(gorakuJudge.gorakuJudge(argSen)):
        return gorakutalk.goraku(argSen,pm)
        
    if(animeJudge.animeJudge(argSen)):
        return anime.anime(argSen,pm)
        
    if(musicJudge.musicJudge(argSen)):
        return music.music(argSen,pm)
        
    if(loveJudge.loveJudge(argSen)):
        return love.love(argSen,pm)
        
    if(physicalconditionJudge.physicalconditionJudge(argSen)):
        return physicalcondition.physicalcondition(argSen,pm)

    if(pm>=1):
        return yasasi.yasasi(argSen)

    return bougen.bougen(argSen)
