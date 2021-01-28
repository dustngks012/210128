#반복문
# for x in ['a', 'b', 'c']:
#     print(x)

# for x in 'hello':
#     print(x)

# for x in (1,2,3,4,5):
#     print(x, end=' ')

# print({1:'a',2:'b',3:'c'}.keys())
# print({1:'a',2:'b',3:'c'}.values())
# print({1:'a',2:'b',3:'c'}.items())

#언패킹
# for x,y in ({1:'a',2:'b',3:'c'}.items():
#     print(x, y)

#정수리스트를 생성해주는 함수
# print(list(range(11)))#stop
# print(list(range(5,11)))#start,stop
# print(list(range(1,11,2)))#start,stop,step(2씩건너뛰기)


# #5,4,3,2,1
# print(list(range(5,0,-1)))
# #7,6,5,4,3
# print(list(range(7,2,-1)))


# for x in range(1,11,2):
#     print(x)

# a=[['말티즈',65], ['치와와',55], ['진돗개',45]]
# # print(len(a))
# print('번호 이름 몸무게')
# print('='*20)
# for x in range(len(a)): #[0,1,2]
#     print('%3d |%5s |%4d' %(x+1,a[x][0],a[x][1]))

#1~10까지의 합계구하기
# s=0 #초기화
# for x in range(1,11):
#     # print(x)
#     s = s + x
# print('합계:', s)

#짝홀수 구분하기
# for x in range(1,11):
#     print(x,':',end='')
#     if x%2==0:
#         print('짝수')
#     else:
#         print('홀수')

#합계가 100이 넘으면 때까지의 수

#1부터 100까지의 합
# s = 0
# for x in range(1,100):
#      s += x
#      if s > 100:
#          print('100이 넘는수 x:', x)
#          print('합계:', s)
#          break #반복문을 탈출하는 효과
# else: #정상적인 수행(break를 만나지 않았을 경우)
#     print('합계가 100을 넘지 못했다')

# badB = False
# wordL = ['안녕', '반가워', '고마워','바보', '또만나']
# badword = ['바보', '멍청이', '홍보']
# for x in wordL:
#     if x in badword:
#         badB = True
#         print('강퇴')
#         break
#         #for문을 빠져나간다(비정상적인 종료)


# if badB==False:
#     print('바른말 사용')

#continue
# for x in [80,65,55,44,90]:
#     if x<60: continue
#     print('%d점 합격'%x)

# for x in [80,65,55,44,90]:
#     if x>60:
#         print('%d점 합격'%x)

# for x in [65,45,95,55,70]:
#     if x<60:
#         print('불합격')
#         break
# else:
#     print('합격')

# for x in [65,45,95,55,70]:
#     if x>60:continue
#     print('불합격')
#     break
# else:
#     print('합격')


# score = [60,58,10,69,45]
# s = 0
# for x in score:
#      s+=x
#      if s > 300:
#          print('합격')
#          break
# else:
#     print('불합격')

#합계를 출력해야 하면
# score = [100,100,100,69,45]
# s = 0
# for x in score:
#     s += x
# if s > 300:
#     print('합격')
# else:
#     print('불합격')
#
# print('합계:', s)

#flag값 (booean)으로 체크한다면
# score = [100,100,100,69,45]
# flag = False #합격여부
# s = 0
# for x in score:
#     s += x
#     if s>=300: flag=True
# #flag는 값이 True/False
# if flag==True:
#     print('합격')
#
# else:
#     print('불합격')
# print(s)

#실습 >
# dan = int(input('단수는?'))
# for x in range(1,10,):
#     # print(2,'*', x,'=', 2*x)
#     print('%d* %d = %d'%(dan,x, dan*x))

# no= int(input('3의배수'))
# for x in range(0, 31, 3):
#     print(x)

# no = int(input('마지막 숫자?'))
# for x in range(no+1):
#     if x%3 == 0:
#         print(x)
# 별찍기1
# star=int(input('줄 수를 입력해주세요'))
#     print('*'*x)
# for x in range(1, 7):
# for x in range(1,star+1):
#     print('*' * x)
##별찍기2
# for x in range(6,0,-1):
#     print('*'* x)
#별찍기3) 과제
# su = int(input('몇 줄?'))
# for x in range(1,su+1):
#     print(' '*(su-x))

# #실습5 반학생들의 점수가 딕셔너리로 저장되어 있을 때 값이 90점 이상인 학생들의 key만 출력하시오.
# dica = {1:94, 2:87, 3:91, 4:75, 5:92}
# for x in dica.items():
#     if x[1]>90:
#         print(x[0],'번', x[1],'점')

# 2)
# dica = {1:94, 2:87, 3:91, 4:75, 5:92}
# for no, score in dica.items():
#     if score>90:
#     # print(no, score)
#         print(no,'번:', score)
#히스토그램 그리기
# listA = ['김정우', '전관음', '구민규', '김동욱']
# qty=[]
# #판매수량 입력
# #김정우의 판매수량은? 10

# for name in listA:
#    q = int(input('%4s 판매수량?'%name))
   # qty.append(q)


#판매수량 출력
# # qty=int(input('과일판매수량은?'))
# for x in range(len(listA)):
#     print('%-5s:'%listA[x], '*' * qty[x])

#딕셔너리로 데이터 표현
# sales= {'홍길동':0, '이순신':0,'박자바':0}
# for x in sales.keys():
#     qty = int(input(x+'판매수량?'))
#     sales[x] = qty
#
# print(sales)
#
# for name, qty in sales.items():
#     print(name+':','*'* qty)


#구구단 2~9단
for y in range(2,10): #단
    print(y, '단')
    for x in range(1,10):
        print('%d * %d = %d'%(y,x,y*x))







