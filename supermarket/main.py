#메인
# from base imfort item
# from  base import company
# from  base import customer
from base import *
import os
#프로그램실행시 아큐먼드 받기
import  sys
#['main.py', 'root', '1111'
av = sys.argv
print(av)
if len(av) < 3:
    print('아이디와 패스워드 입력해주세요!')
    exit(0)#프로그램 종료

if av[1]=='root' and av[2]=='1111':
    print('슈퍼권한 유저')
else:
    print('일반 유저')

while True:
    #콘솔화면 지우기
    #콘솔에서만 작동
    #import os
    #os.system('cls')
    print('-'*15)
    print('슈퍼마켓 관리v0.1' )
    print('-'*15)
    print('1.상품입고')
    print('2.상품출고')
    print('3.거래처등록')
    print('4.고객등록')
    print('q.종료')
    print('-'*15)
    no = input('작업번호:')
    if no=='1':
        from base import item
        item.itemInput()
    elif no=='2':
        from base import item
        item.itemOutput()
    elif no=='3':
        from  base import company
        company.addcompany()
    elif no=='4':
        from  base import customer
        customer.addcustomer()
    elif no=='q':
        break
    else:
        print('잘못된 선택입니다.')

    input('엔터를 입력하세요')
