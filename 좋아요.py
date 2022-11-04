from 유틸 import *
from 정렬 import 정렬_메뉴

def 좋아요_메뉴(music_list,singer_list,playlist,heartlist):
    def 좋아요_추가():
        while 1:
            print('1. 장르 목록에서 좋아요 추가하기')
            print('2. 플레이리스트에서 좋아요 추가하기')
            print('3. 뒤로가기')
            com=int(input('실행 번호: '))
            if com==1:
                구분선()
                print('[ 장르 목록 ]')
                print('1. 멜론 top 50')
                print('2. 발라드')
                print('3. 힙합')
                print('4. 노래방 인기차트')
                print('5. 팝')
                gen_sel=int(input('장르 목록의 번호를 입력하세요: '))
                while gen_sel<1 or gen_sel>5:
                    다시입력()
                    gen_sel=int(input('장르 목록의 번호를 입력하세요: '))
                구분선()
                for i in range(len(music_list[gen_sel-1])):
                    print('%d. %s | %s'%(i+1,music_list[gen_sel-1][i],singer_list[gen_sel-1][i]))
                sel=int(input('좋아요 목록에 추가할 노래의 번호를 입력하세요: '))
                while sel<1 or sel>len(music_list[gen_sel-1]):
                    다시입력()
                    sel=int(input('좋아요 목록에 추가할 노래의 번호를 입력하세요: '))
                if heartlist.count([music_list[gen_sel-1][sel-1],singer_list[gen_sel-1][sel-1]])>0:
                    이미있음()
                    continue
                구분선()
                print('좋아요 목록에 "%s | %s"을(를) 추가합니다.'%(music_list[gen_sel-1][sel-1],singer_list[gen_sel-1][sel-1]))
                구분선()
                heartlist.append([music_list[gen_sel-1][sel-1],singer_list[gen_sel-1][sel-1]])
            elif com==2:
                if len(playlist)==0:
                    구분선()
                    print("플레이리스트에 노래가 없습니다. 먼저 노래를 추가하세요.")
                    구분선()
                    continue
                구분선()
                print('플레이리스트:')
                for i in range(len(playlist)):
                    print('%d. %s | %s'%(i+1,playlist[i][0],playlist[i][1]))
                sel=int(input('좋아요 목록에 추가할 노래의 번호를 입력하세요: '))
                while sel<1 or sel>len(playlist):
                    다시입력()
                    sel=int(input('좋아요 목록에 추가할 노래의 번호를 입력하세요: '))
                if heartlist.count([playlist[sel-1][0],playlist[sel-1][1]])>0:
                    이미있음()
                    continue
                구분선()
                print('좋아요 목록에 "%s | %s"을(를) 추가합니다.'%(playlist[sel-1][0],playlist[sel-1][1]))
                구분선()
                heartlist.append([playlist[sel-1][0],playlist[sel-1][1]])
            elif com==3:
                뒤로가기()
                break
            else:
                다시입력()

    def 좋아요_제거():
        while 1:
            print('1. 좋아요 목록에서 노래 제거하기')
            print('2. 뒤로가기')
            com=int(input('실행 번호: '))
            if com==1:
                if len(heartlist)==0:
                    구분선()
                    print("좋아요 목록에 노래가 없습니다.")
                    구분선()
                    continue
                구분선()
                print('좋아요 목록:')
                for i in range(len(heartlist)):
                    print('%d. %s | %s'%(i+1,heartlist[i][0],heartlist[i][1]))
                구분선()
                sel=int(input('좋아요 목록에서 제거할 노래의 번호를 입력하세요: '))
                while sel<1 or sel>len(heartlist):
                    다시입력()
                    sel=int(input('좋아요 목록에서 제거할 노래의 번호를 입력하세요: '))
                구분선()
                print('좋아요 목록에서 "%s | %s"을(를) 제거했습니다.'%(heartlist[sel-1][0],heartlist[sel-1][1]))
                구분선()
                heartlist.remove([heartlist[sel-1][0],heartlist[sel-1][1]])

            elif com==2:
                뒤로가기()
                break
            else:
                다시입력()

    def 좋아요_목록():
        while 1:
            print('1. 좋아요 목록 보기')
            print('2. 뒤로가기')
            com=int(input('실행 번호: '))
            if com==1:
                if len(heartlist)==0:
                    구분선()
                    print("좋아요 목록에 노래가 없습니다. 먼저 노래를 추가하세요.")
                    구분선()
                    continue
                구분선()
                print('좋아요 목록:')
                for i in range(len(heartlist)):
                    print('%d. %s | %s'%(i+1,heartlist[i][0],heartlist[i][1]))
                구분선()
            elif com==2:
                뒤로가기()
                break
            else:
                다시입력()
    while 1:
            print('[ 좋아요 메뉴 ]')
            print('1. 좋아요 목록 보기')
            print('2. 좋아요 목록에 노래 추가하기')
            print('3. 좋아요 목록에서 노래 제거하기')
            print('4. 좋아요 목록 정렬하기')
            print('5. 뒤로가기')
            com=int(input('실행 번호: '))
            if com==1:
                구분선()
                좋아요_목록()
            elif com==2:
                구분선()
                좋아요_추가()
            elif com==3:
                구분선()
                좋아요_제거()
            elif com==4:
                구분선()
                정렬_메뉴(heartlist)
            elif com==5:
                뒤로가기()
                break
            else:
                다시입력()