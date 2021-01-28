#변수
a = 30
b = 60
10
#print(a,'+', b,'=',a+b)
#print(a,'-', b,'=',a-b)
#print(a,'*', b,'=',a*b)
#print(a,'/', b,'=',a/b)
#문자와 숫자의 +연산자 불가
#print(a + '+'
#print('*' * 10)

#포맷문자열
# 30 + 20 = 50
a = 30 ; b = 20
#print('%d + %d = %d'%(a,b,a+b))
#print('%d - %d = %d'%(a,b,a-b))
#print('%d * %d = %d'%(a,b,a*b))
#print('%d / %d = %d'%(a,b,a/b))
#print('%d // %d = %d'%(a,b,a//b))
#print('%d %% %d = %d'%(a,b,a%b))
#print('korea \\ node')

#당신의 나이는 10
a = 10
#print('당신의 나이는 %d살'%a)
#원주율은 3.14
a = 3.14
#print('원주율은 %.2f'%a)
#반갑습니다. 안녕하세요!
a = '안녕하세요 !'
#print('반갑습니다.\n%s'%a)
#1000$
a = '$'
#print('1000%c'%a)
#2차 방정식
x=3
y=3*x**2+2*x+1
#print('y=',y, sep='')
#실습 : 시분초구하기

s=10000
t=s//3600
print('시간'':', t)
r=s%3600
print('남은초: ',r)
m=r//60
print('분:', m)
print('초:', r%60)
