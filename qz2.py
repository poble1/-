# -*- coding: utf8 -*-

import sys
import random
import socket
import re
from imp import reload
#test = socket.create_connection(("172.31.20.61",8080))



# 유니코드 한글 시작 : 44032, 끝 : 55199
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = [u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = [u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ', u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ']

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [u' ', u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ', u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']
score =0


if __name__ == '__main__':
    arr=[]
    arr2=[]
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

        arr=[]
        arr2=[]
        string =""
        
        
        if len(strs) == 1 :
            continue
        for str1 in strs:

#             print '\n\n한글 : {} '.format(str)


            for charTemp in str1:
                cBase = ord(charTemp) - BASE_CODE
                c1 = int(cBase / CHOSUNG)
                    #print format(CHOSUNG_LIST[c1])

                hi = format(CHOSUNG_LIST[c1])
                string = string + hi
                arr.append(hi)
        print (string)
        strs = input ("정답 입력 : ")
        
        if re.match('.*[ㄱ-ㅎ ㅏ-ㅣ 가-힣]+.*',strs)is None:
            print("잘못된 문자입니다.")
            continue
        if strs.isalpha == True:
            print("잘못된 문자입니다.")
            continue


        for str in strs:
#                    print strs
#                    print '\n\n한글 : {} '.format(str)
            for charTemp in str:
                cBase = ord(charTemp) - BASE_CODE
                c1 = int(cBase / CHOSUNG)
#                    print '초성 : {}'.format(CHOSUNG_LIST[c1])
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
        if flag==1: print("오답입니다.")
        else:
            if strs in List:
                print("정답입니다.")
                score = score + 10
            else:
                print("오답입니다.")
    print ("당신의 점수는 %d 입니다!"%score)
        
