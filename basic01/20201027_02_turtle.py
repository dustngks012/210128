#거북이 (그래픽모듈)
# import turtle as t
# p = t.Pen()
# p.shape('turtle')
# p.color('red', 'blue')




#사각형
'''
for x in range(4):
    p. forward(100)
    p. right(90)

#삼각형
for x in range(3):
    p.forward(100)
    p.right(360/3)
#오각형
for x in range(5):
    p.forward(200)
    p.right(360 / 5)
'''
#실습) 각형을 사용자에게 입력받아 그리는 함수
#함수명 : draw
#매개변수: 각형
#반환형:없음

# def draw(n):
#     for x in range(n):
#         p.forward(100)
#         p.right(360/n)
# while True:
#     a = int(input('각형은?'))
#     draw(a)
# t.done()
'''
t.done
p.penup()
p.goto(200,200)
p.pendown()             
p.begin_fill()
p.circle(100)
t.done()
'''
#재귀함수
# 자기자신을 호출하는 함수
def test(n):
    if n>2 : return
    print(n)
    test(n+1)

test(0)

