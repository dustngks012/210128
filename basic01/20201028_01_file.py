#파일다루기
#텍스트파일
#w:쓰기모드:기존파일삭제하고 새로운 파일생성
#a:추가모드:기존파일에 추가
# w: 기존파일삭제하고 새로운 파일생성
# f=open('sample.txt', 'w')
# f.write('짜장면\n')
# f.write('짬뽕\n')
# f.close()

#실습) 사용자에게 입력을 받아서 파일에 저장
#파일명 : menu.txt
# f = open('./data/menu.txt', 'w',  encoding='utf-8')
# while True:
#     m = input('메뉴를 입력해주세요')
#     if m =='': break
#     f.write(m+'\n')

# f.close()

#텍스트 파일 읽기
# #r:읽기모드
# f = open('./data/menu.txt', 'r',  encoding='utf-8')
# print(f.read())
# f.close()

#한라인씩 읽기
# f=open('./data/menu.txt', 'r', encoding='utf-8')
# while True:
#
#     data=f.readline()
#     if data=='': break
#     print(data,end='')
# f.close()

#여러줄 읽기
# f=open('./data/menu.txt','r', encoding='utf-8')
# data = f.readlines()
# for x in data:
#     print(x[:-1])#슬라이싱
#
# f.close()

#읽기/쓰기 모드
#r+:파일이 반드시 존재
#w+:파일이 존재하지 않으면 생성
# f = open('./data/menu.txt', 'r+', encoding='utf-8')
# print(f.read())
# print('-'*10)
# f.write('짬뽕\n')
# f.seek(0)#파일의 포인터위치를 처음으로 이동
# print(f.read())
# f.close()


#바이너리 파일
# f = open('./data/images.jfif', 'rb')
# w = open('./data/images_copy.jfif', 'wb')
# size=1024 #1kbyte
# while True:
#     data=f.read(size)
#     if not data: break#더이상 읽어들일 파일이 없다면
#     w.write(data)

# f.close()
# w.close()
#실습)메뉴 읽어보기 판매 메뉴 리스트를 읽어와서 화면에 출력해 보시오

# f = open('./data/menu.txt', 'r', encoding='utf-8')
#     data=f.readlines()
#     print(data)
#     print(f.read())
# for x in range(len(data)):
#
# f.close()