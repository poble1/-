from aiohttp import web
import socketio
import sys
import random
import re
from imp import reload

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.on('connect')
async def connect(sid, environ):
    print("connect ", sid)

@sio.on('start')
async def message(sid, instrs):
    print (instrs)
    await sio.emit('start', dic)

@sio.on('send')
async def send(sid, mesg):
    kt = ck()
    await sio.emit('send', dic)
   
    print (dic)
    
@sio.on('answer')
async def answer(sid, instrs):  
    await sio.emit('answer', instrs)
    print (instrs)
    
@sio.on('correct')
async def correct(sid, instrs):
    print (instrs)
    div(instrs)
    await sio.emit('correct', mesg)
    print (mesg)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

# 유니코드 한글 시작 : 44032, 끝 : 55199
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = [u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = [u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ', u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ']

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [u' ', u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ', u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']
score =0

def div(k):

        instrs3 = ""
        instrs3 = k[0]
        arr2=[]
        global mesg
        mesg=""

        if re.match('.*[ㄱ-ㅎ ㅏ-ㅣ 가-힣]+.*',instrs3)is None:
            mesg="잘못된 문자입니다."

            return
        if instrs3.isalpha == True:
            mesg="잘못된 문자입니다."
            return

        for instrs2 in instrs3:
            for charTemp in instrs2:
                cBase = ord(charTemp) - BASE_CODE
                c1 = int(cBase / CHOSUNG)
                    #print '초성 : {}'.format(CHOSUNG_LIST[c1])
                hello = format(CHOSUNG_LIST[c1])
            
                arr2.append(hello)

        flag = 0        
        if len(arr2) == len(arr):
            for i in range(0,len(arr2)):
                if arr[i] != arr2[i]:
                    flag = 1
                    break
                i=i+1
        else:
            flag=1

        if flag==1: 
            mesg = "Wrong Answer."
            return
        else:
            if instrs3 in List:
                mesg="Correct."
                return
            else:
                mesg="Wrong Answer."
                return
                
def ck():
        i = int( random.randrange(0,len(List)))
        strs = list(List[i])
        global dic
        dic={}
        print (k)

        global string
        string =""
        
        arr=[]
        
        if len(strs) == 1 :
            return
            
        print (strs)
        
        for str1 in strs:
            #p rint '\n\n한글 : {} '.format(str)

            for charTemp in str1:
                cBase = ord(charTemp) - BASE_CODE
                c1 = int(cBase / CHOSUNG)
                hi = format(CHOSUNG_LIST[c1])
                string = string + hi
                arr.append(hi)
        
        print (string)
        dic['key']=string
        return dic
    
if __name__ == '__main__':
    global arr
    arr=[]
    global arr2
    arr2=[]
    global instrs

    res=[]
    List=[]

    tst = open('eksdjwkd.txt','r')
    
    for tstline in tst:
        tstline=tstline[0:-1]
        List.append(tstline)
    List[0] = "가게"
    
    for k in range(0,11):    
        i = int( random.randrange(0,len(List)))
        strs = list(List[i])
        global dic
        dic={}
        print (k)

        global string
        string =""
        arr=[]
        if len(strs) == 1 :
            continue
        for str1 in strs:
             #print '\n\n한글 : {} '.format(str)
            for charTemp in str1:
                cBase = ord(charTemp) - BASE_CODE
                c1 = int(cBase / CHOSUNG)
                hi = format(CHOSUNG_LIST[c1])
                string = string + hi
                arr.append(hi)
        
        print (string)
        print (strs)
        dic['key']=string
        web.run_app(app)