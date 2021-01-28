#딕셔너리
#인덱스가 없다(순서가없다)
#키와 값으로 데이터표현
#d = {'홍':90,'이':70, '유':80}
#print(d['유'])
#d['박'] = 75
#print(d)

#dic = {'1':'one','2':'two', '3':'three', '4': 'four', '5': 'five'}
#no = int(input('숫자는?'))
#print (dic[no])


#학생들의 국영수 점수를 딕셔너리에 저장
#d = {'국':100, '영':80, '수':78}
#d = {'홍':[100,90,78], '박':[70,90,78]}
#d = {'홍': {'국':100,'영':80,'수':78}
#d={}


#입력
#kor = int(input('국어?'))
#d['국'] = kor
#eng = int(input('영어?'))
#d['영'] = eng
#math = int(input('수학?'))
#d['수'] = math
#print(d)

#계산
#sum = d['국']+d['영']+d['수']
#print('합계:%d'%(sum))
#avg=sum/3
#print('평균:%.2f'%(sum/3))

# d = {'홍':{'국':99,'영':80,'수':78,'총점':258,'평균':85.66}}
#s={};d={}
#name = input('이름은?')
#kor = int(input('국어?'))
#eng = int(input('영어?'))
#math = int(input('수학?'))
#summary = kor + eng + math
#avg = summary /3
#s['국']=kor; s['영']=eng; s['수']=math;
#s['총점']=summary; s['평균']=float('%.2f'%avg)
#d[name] = s
#print(d)

#부울린(boolean) : True(참:1) / False(거짓:0)
#print('홍' in dic)
#print('h' in 'hello')
#print(30 in [10,20])
#print(30 in (10,20))

#키만 알아내기
#dic = {'홍':100, '박':90}
#l = list(dic.keys())  #list형으로 변환
#print(l[0])
#값만 알아내기
#print(list(dic.values())[1]
#키와 값을 알아내기
#dic = {'홍': 100, '박': 90}
#print(dic.items())

#실습1)날씨 바꾸기

# dicW = {'mon':'sun', 'tue':'cloud', 'wed':'rain', 'thu':'sun', 'fri':'rain'}
# dicW['thu']='cloud'
# print(dicW)


#실습2)math 포함 여부

# dicSubject = {'kor':80,'eng':95,'math':75,'art':85}
# print('math' in dicSubject)


#실습3)학생정보 딕셔너리

# name = input('이름은?')
# age = int(input('나이는?'))
# blood = input('혈액형은?')
# dicW = {'이름': name,'나이':age,'혈액형':blood}
# print(dicW)

#실습)
score = input('국영수점수는?').split()
# score[0] = int(score[0])
# score[1] = int(score[1])
# score[2] = int(score[2])
print(score)
print(list(map(int, score)))


