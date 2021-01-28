#함수(내장함수)
# data =[5,6,7,2,1]
# print((max(data))
# print((min(data))
# print((min(data))
# print(sum(data)/len(data))
#
# #ㅋ드값)
# print(ord('A'))
# print(ord('홍'))
# print(ord('김'))
# #코드=>문자
# print(chr(65))
# print(chr(44608))



#2진수를 10진수로
#8bit (1bytes)
#00000000~11111111 => 0 ~ 255


# print(bin(255))#10진법=>2진법
# print(oct(255))#10진법=>8진법
# print(hex(255))#10진법=>16진법

#사용자함수 만들기
#반환값이 없는 함수
#def printName(name,age):
#     print(name, age)

#printName('홍길동',20)
#printName('이순신',45)

#반환값이 있는 함수

#합(add)
# def add(a,b): #지역변수(매개변수)
#     return a+b
# s = add(30,20)  #전역변수
# print('더하기:', s)
#
# #차(sub)
# def sub(a,b):
#     return a-b
# d = sub(100,50)
# print('빼기:', d)
#
# #곱(mul)
# def mul(a,b):
#     return a*b
# d = mul(5,6)
# print('곱하기:', d)
#
# #나누기(div)
# def div(a,b):
#     return a/b
# m = div(10,2)
# print('나누기:', m )

#함수에서 전역변수 사용
# a=100
# def cal():
#     global a #전역변수 a
#     print(a+10)
# cal()

#두수를 매개변수로 받아서 사칙연산을 return
# def cal(a,b):
#     return a+b,a-b,a*b,a/b

# a,b,c,d=cal(30,20)
# print('더하기:', a)
# print('빼기:', b)
# print('곱하기:', c)
# print('나누기:', d)
#실습) 구구단 출력함수

#def cal(a,b):
# g=int(input('숫자입력'))
# def gugudan(d):
#     for x in range(2, 10):  #
#         print('%d * %d = %d' % (d, x, d * x))
# gugudan(g)

#실습) 매개변수(리스트)의 값을 더하는 함수

# def sum(data):
#     s = 0
#     for x in data:
#         s+=x #누적하는 방법
#
#     return s #합계를 반환
#
# data=[4,5,6,7,8,1]
# print(sum(data))

#실습 팩토리얼 구하기 숫자를 입력 받아 팩토리얼을 구하고 리턴하는 함수
#팩토리얼 : (n!= 1*2*3*...*n)
#4팩토리얼 4!= 1*2*3*4

# def fac(data):
#     s = 1
#     for x in data:
#         s*=x

#     return s

# data=[1,2,3,4]
# print(fac(data))


# def factory(n):
#     m=1
#     for x in range(1,n+1):
#         m *= x
#         return m

# print(factory(5))


#실습 원의 넓이를 구하여 반환하는 함수
#함수명 : circleArea
# 매개변수 : 반지름
# 반환값 : 원의 넓이

# def circleArea(r):
#     s=r * r * 3.14
#     return s
# print(circleArea(5))

#함수의 장점 : 재활용성, 유지보수
#사용자에게 정수를 입력받아
#입력받은 값을 반환하는 함수
# 함수명 : inputDigital
# 매개변수 : 없음
#반환값 : 입력받은 정수
# def inputDigital():
#     n= input('정수를 입력:')

#     return n
# print(inputDigital())


# def inputDigital(msg):
#     a = input(msg)
#     if a.isdigit():
#         return int(a)

# a=inputDigital('첫번째 정수?')
# b=inputDigital('두번째 정수?')
# print(a+b)

#실습) 두수를 사용자에게 입력받아 사칙연산을
#사용자입력함수:inputDigital(msg)
#기호입력받기 : inputsign
#사칙연산함수 : add, sub, mul, div
def inputDigital(msg):
    while True:
        a = input(msg)
        if a.isdigit():
            return int(a)
def inputSign():
    sign = ['+','-','*','/']
    while True:
        a = input('기호?')
        if a in sign:
            return a
# 합(add)
def add(a,b): #지역변수(매개변수)
    return a+b
#차(sub)
def sub(a,b):
    return a-b
#곱(mul)
def mul(a,b):
    return a*b
#나누기(div)
def div(a,b):
    return a/b

#사용자가 첫번째 정수에 0을 입력 종료
while True:
    print('-'*20)
    a=inputDigital('첫번째정수?')
    if a==0:
        print('종료')
        break
    b=inputDigital('두번째정수?')
    sign = inputSign()
    if sign=='+':
        print('더하기:', add(a,b))
    elif sign =='-':
        print('빼기:', sub(a, b))
    elif sign == '*':
        print('곱하기:', mul(a, b))
    elif sign == '/':
        print('나누기:', div(a, b))
    else:
        print('잘못된 연산')
#시간 모듈 imfort
import time
print(time.localtime())#현재시간
#3초간 시간 정지
print('3초간 시간을 멈춘다.')