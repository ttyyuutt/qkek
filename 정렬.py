from 유틸 import *

def 정렬_메뉴(list):
    if len(list)==0:
        print("노래가 없습니다. 먼저 노래를 추가하세요.")
        구분선()
        return
    def 정렬_제목():
        print('제목을 기준으로 정렬합니다.')
        list.sort(key=lambda list:list[0])
        for i in range(len(list)):
            print('%d. %s | %s'%(i+1,list[i][0],list[i][1]))
        구분선()

    def 정렬_가수():
        print('가수를 기준으로 정렬합니다.')
        list.sort(key=lambda list:list[1])
        for i in range(len(list)):
            print('%d. %s | %s'%(i+1,list[i][0],list[i][1]))
        구분선()
    
    while 1:
        print('[ 정렬 메뉴 ]')
        print('1. 제목 기준 정렬')
        print('2. 가수 기준 정렬')
        print('3. 뒤로가기')
        com=int(input('실행 번호: '))
        if com==1:
            구분선()
            정렬_제목()
        elif com==2:
            구분선()
            정렬_가수()
        elif com==3:
            뒤로가기()
            break
        else:
            다시입력()