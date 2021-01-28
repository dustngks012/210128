#상품관리모듈
from base.common import fileRead
def itemInput():
    print('*')
    print('*.상품관리*')
    print('*''*15')
    print('1.상품등록')
    print('2.상품조회')
    print('3.메인메뉴(q)')
    print('*'*15)
    no = input('작업번호:')
    if no=='1':
        itemInput()
    elif no == '2':
        itemOutput()
    else:
        print('잘못된 번호')
#상품입력받기
def itemInput(self):
        self.code = input('상품코드는?')
        self.itemname = input('상품명은?')
        self.price = int(input('가격은?'))
        self.bigo = input('비고?')
    #db insert
    def itemInsert(self):
        conn = connect('hr/hr@localhost:1521/xe')
        cur=conn.cursor()
        data = (self.code,self.itemname,self.price, self bigo)
        cur.execute('insert into item values(:1,:2,:3,:4)', data)
        cur.close()
        cur.commit()
        cur.close()

#서브메뉴
def itemMenu():
    while True:
    print('상품을 출고합니다.')

def itemList():
    fileRead('./data/item.txt')