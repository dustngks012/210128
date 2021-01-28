#공통모듈
def fileRead(fileName):
    f =  open(fileName, 'r')
    print(f.read())
    f.close()