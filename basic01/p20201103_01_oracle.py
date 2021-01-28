from cx_Oracle import *
# def item_insert():
#     conn = cx_Oracle.connect('hr/hr@localhost:1521/xe',)
#     cur = conn.cursor()
#     cur.execute('insert into item values(:1,:2,:3,:4)',('8805','샘플2',5000,'파이썬테스트'))
#     cur.close()
#     conn.commit()
#     conn.close()
#
#
# item_insert('8805','샘플2',5000,'파이썬3')

# def item_delete():
#     conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
#     cur = conn.cursor()
#     cur.execute('delete from item where code=:1', data)
#     cur.close()
#     conn.commit
#     conn.close()
# item_delete(('8805',))

# def item_update(data):
#     conn = connect('hr/hr@localhost:1521/xe')
#     cur = conn.cursor()
#     cur.execute('''update item
#                     set itemname =;1,
#                     price = :2,
#                     bigo = :3
#                     where code = :4''',data)
#     cur.close()
#     conn.commit()
#     conn.close()
#
# item_update(('상품변경',1800,'수정테스트','8804'))
#
# #조회
# def item_select():
#     conn = connect('hr/hr@localhost:1521/xe')
#     cur = conn.cursor()
#     cur.execute('select * from item order by code')
#     #언패킹
#     for code,name,price,bigo in cur:
#             print(code,name,price,bigo)
#     cur.close()
#     conn.close()
#순위 조회
def victor_seq():
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('''select m.userid, m.name, c)
#조건 조회
def item_select_find(data):
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('''select * from item
        where itemname like :find ''',data)
    #언패킹
    for code,nane,price,bigo, in cur:
        print(code,name,price,bigo)
    cur.close()
    conn.close()
name = input('검색할 상품명?')
item_select_find((name,))
no = input('작업번호:')
    if no=='1': #등록
        item = ItemP()#객체생성
        item.itemInput()#입력받기
        item.itemInsert()#추가하기
    elif no == '2': #조회
        find = input('조회할 상품명은?')
        item = ItemP()  #객체생성
        item.itemSelect((find,)) #조회하기
        input('조회완료....')
    elif no=='q':
        break
    else:
        print('잘못된 번호')