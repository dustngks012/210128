#모듈 사용하기
# import time
# s=list(time.localtime())
# print(s[0],'년', s[1],'월',s[2],'일')
#
# import datetime
# print(datetime.datetime.now())

# print(time.time())
# import time
# print('시작')
# time.sleep(3) #~초 동안 실행x
# print('3초지남')


#1초마다 화면에 타이머를 출력
#결과
# import time
# for x in range(1,5):
#     print(x,'초')
#     time.sleep(1)
# print('End')

#실습)
# import a20201026_01_function
# import time
# sec = a20201026_01_function.inputDigital('초?')
# print('시작')
# for x in range(1,sec+1):
#     print(x,'초')
#     time.sleep(1)
# print('끝')

#캘린더 모듈 추가
# import calendar
# calendar.prcal(2020)
# calendar.prmonth(2020, 10)

#랜덤 모듈
# import random
# #0 <= 난수 <1
# # print(random.random())
# aw=0
# bw=0 #이긴 횟수
# for x in range(5):
#     a = random.randint(1,6)
#     b = random.randint(1,6)
#     print('A:', a, end=' ')
#     print('B:', b)
#     if a>b:
#         print('A 승리')
#         aw=aw+1
#     elif a<b:
#         print('B 승리')
#         bw=bw+1
#     else:
#         print('무승부')
#     print('-'*15)
#
# #최종결과
# print('A의 승:', aw)
# print('B의 승:', bw)
# if aw>bw:
#     print('A최종승리')
# elif aw<bw:
#     print('B최종승리')
#2) 3승이 먼저 되면 종료
# aw=0
# bw=0
# import random
#
# while aw<3 and bw<3:
#     a = random.randint(1,6)
#     b = random.randint(1,6)
#     if a>b:
#         print('A승')
#         aw+=1
#     elif b>a:
#         print('B승')
#         bw+=1
#     else:
#         print('무승부')
#         print('-'*10)
#     #만약에 aw가 3이상이거나
#     #bw가 3이상이면 반복문 탈출
#     if aw>=3 or bw>=3:
#         break
# #최종결과
# print('A의 승:', aw)
# print('B의 승:', bw)
# if aw>bw:
#     print('A최종승리')
# elif aw<bw:
#     print('B최종승리')
# else:
#     print('무승부')

'''
import random
data = ['해', '해', '달', '달']
random.shuffle(data)
print(data)'''

#가위/바위/보 게임
# import random
# a = random.choice(['가위', '바위', '보'])
# b = random.choice(['가위', '바위', '보'])
# if a=='가위'  and b=='가위':
#     print('무승부')
# elif a == '가위' and b == '바위':
#     print('B승')
# elif a=='가위' and b=='보':
#     print('A승')
# elif a=='바위' and b=='보':
#     print('B승')
# elif a=='바위' and b=='가위':
#     print('A승')
# elif a=='보' and b=='가위':
#     print('B승')
# elif a=='보' and b=='바위':
#     print('A승')

#딕셔너리로 표현한다면
# import random as r #알리어스명
# d={'가위바위': ' B','가위보':'A',
#    '바위가위':'A','바위보':'B',
#    '보가위':'B','보바위':'A'}
# a = r.choice(['가위', '바위', '보'])
# b = r.choice(['가위', '바위', '보'])
# if a==b:
#     print('무승부')
# else:
#     print(d[a+b])


from random import sample
lotto = (sample(range(1,46),6))
print(lotto)
# lotto.sort()
# print(lotto)
print(sorted(lotto))
print(lotto)
#
# #사용자에게 로또 번호를 입력받아 맞은 개수 출력
lotto = input('로또번호는?').split(',')
print(lotto)
right = 0 #맞은갯수