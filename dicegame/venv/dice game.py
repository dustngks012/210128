# 메인
# 사용자등록
from cx_Oracle import *
from random import *

# 아이디 존재 유무
def member_selectCheckYn(data):
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('select count(*) cnt from member where userid = :1',data)
    cnt = tuple(cur)[0][0]
    cur.close()
    conn.close()
    return cnt

#멤버추가
def member_insert(data):
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('insert into member values (:1,:2)',('hong','홍길동'))
    cur.close();
    conn.commit();
    conn.close();

Ascore = 0
Bscore = 0
num = 0

while True :
	print('-----#주사위 게임-----')
	print('-----시작(s)-----')
	print('-----종료(p)-----\n\n\n')
	start = input('시작을 원하면 s 종료를 원하시면 p를 입력하세요.\n\n\n')
	if start == 's' or start == 'S':
		'''print('주사위 게임')
		print('시작!')
		print("게임 횟수를 입력해주세요")
		num = input()
		int(num)'''
#사용자등록
		userid = input('아이디는?')
		name = input('이름은?')
		print('등록되었습니다')

	for A in range (1,4):
		diceA = randint(1,6)
		diceB = randint(1,6)
		print('player A dice:', diceA)
		print('player B dice:', diceB , '\n\n\n')
		if Ascore >= 0 and Bscore>=0 :
			if diceA > diceB :
				Ascore +=1
				print('Player A score:', Ascore )
				print('Player B score:', Bscore,'\n\n\n' )
				print('----------')
				wait = input()

			elif diceA < diceB :
				Bscore +=1
				print('Player A score:', Ascore)
				print('Player B score:', Bscore,'\n\n\n')
				wait = input()
			else:
				print('Player A score:', Ascore)
				print('Player B score:', Bscore,'\n\n\n')

		if Ascore > 0 :
			if Ascore < Bscore:
				print('Player B win')
				break

			elif Bscore > Ascore:
				print('Player A win')
				break

			elif Ascore == Bscore:
				print('same score')
				break

				if start == 'p' or start == 'P':
					print('종료되었습니다.')
					break
			else:
				Ascore
				print('잘못입력하셨습니다.\n\n')
				print('게임이 다시 시작되었습니다\n\n')


