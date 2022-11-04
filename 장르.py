import random
from 유틸 import *
from 플레이리스트 import 플레이리스트_메뉴
from 좋아요 import 좋아요_메뉴

def 장르_메뉴(music_list,singer_list,playlist,heartlist):
    genre=['멜론 top 50','발라드','힙합','팝','노래방 인기차트']
    def 장르_랜덤추천():
        while 1:
            print('[ 장르 목록 ]')
            print('1. 멜론 top 50')
            print('2. 발라드')
            print('3. 힙합')
            print('4. 팝')
            print('5. 노래방 인기차트')
            reco_num=int(input('몇 개 추천해드릴까요?(최대 2개): '))
            구분선()
            if 0<reco_num<3:
                print('추천: ',end='')
                print(random.sample(genre,reco_num))
                print()
                구분선()
                break
            else:
                다시입력()
    def 장르_장르별노래():
        while 1:
            print('1. 장르별 노래 목록 보기')
            print('2. 뒤로가기')
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
                구분선()
            elif com==2:
                뒤로가기()
                break
            else:
                다시입력()
    while 1:
        print('[ 장르 메뉴 ]')
        print('1. 랜덤 장르 추천')
        print('2. 장르별 노래 목록 보기')
        print('3. 뒤로가기')
        com=int(input('실행 번호: '))
        if com==1:
            구분선()
            장르_랜덤추천()
        elif com==2:
            구분선()
            장르_장르별노래()
        elif com==3:
            뒤로가기()
            break
        else:
            다시입력()