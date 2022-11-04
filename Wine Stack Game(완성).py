#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 각종 반복적으로 사용하는 함수들 정의

# 색코드를 사용하기 위해 쓰임 (이 중 일부만 활용)
STD_INPUT_HANDLE   = -10
STD_OUTPUT_HANDLE  = -11
STD_ERROR_HANDLE   = -12
  
FOREGROUND_BLACK     = 0x00
FOREGROUND_BLUE      = 0x01 # text color contains blue.
FOREGROUND_GREEN     = 0x02 # text color contains green.
FOREGROUND_RED       = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE      = 0x10 # background color contains blue.
BACKGROUND_GREEN     = 0x20 # background color contains green.
BACKGROUND_RED       = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

# 출력화면 삭제를 위해 쓰임
import os

# cmd에서 쓰이는 색코드를 활용하기 위해 쓰임
import ctypes
from re import L

# 색코드 값 초기화를 위해 쓰임
import sys

# 무작위 추첨 코드를 위해 쓰임
import random

# 자동 턴 넘김을 위해 쓰임
import time

# cmd에서 색 코드를 사용하기 위해 쓰임
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

# 색코드를 쓰면 코드에 맞게 색이 변하는 set_color 함수
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

# 플레이어별 대표하는 색상 코드 - 일부 출력되는 문자의 색상을 통해 현재 플레이어가 누구인지 육안으로 파악하기 쉽도록 도와준다.
p1_color = 4
p2_color = 6
p3_color = 9

# 와인잔이 쌓이는 슬롯의 색을 받고, 그 색으로 바꿔주는 함수
def print_slot(a):
    sys.stdout.flush()
    set_color(int(pyramid_row[a][2]))
    print(str(pyramid_row[a][0]), end='')
    sys.stdout.flush()
    set_color(8)

# 게임 화면 호출 함수
def print_gamescreen(current_color, current_player):
    # 플레이어 차례와 남은 와인잔 개수
    print('')
    sys.stdout.flush()
    set_color(8)
    print('                                  ㅣ  플레이어  |    | 개수 |')
    print('                                  ㅣ ', end='')
    sys.stdout.flush()
    set_color(p1_color)
    print('플레이어 1 ', end='')
    sys.stdout.flush()
    set_color(8)
    print('|', player1, '| ', player1_wine, ' |')
    print('                                  ㅣ ', end='')
    sys.stdout.flush()
    set_color(p2_color)
    print('플레이어 2 ', end='')
    sys.stdout.flush()
    set_color(8)
    print('|', player2, '| ', player2_wine, ' |')
    print('                                  ㅣ ', end='')
    sys.stdout.flush()
    set_color(p3_color)
    print('플레이어 3 ', end='')
    sys.stdout.flush()
    set_color(8)
    print('|', player3, '| ', player3_wine, ' |')      
    print('')
    print('')
    # 8층
    print('                           [ ', end='')
    print_slot(35)
    print(' ]')
    # 7층
    print('                        [ ', end='')
    print_slot(33)
    print(' ] [ ', end='')
    print_slot(34)
    print(' ]')
    # 6층
    print('                     [ ', end='')
    print_slot(30)
    print(' ] [ ', end='')
    print_slot(31)
    print(' ] [ ', end='')
    print_slot(32)
    print(' ]')
    # 5층
    print("                  [ ", end='')
    print_slot(26)
    print(' ] [ ', end='')
    print_slot(27)
    print(' ] [ ', end='')
    print_slot(28)
    print(' ] [ ', end='')
    print_slot(29)
    print(' ]')
    # 4층
    print("               [ ", end='')
    print_slot(21)
    print(' ] [ ', end='')
    print_slot(22)
    print(' ] [ ', end='')
    print_slot(23)
    print(' ] [ ', end='')
    print_slot(24)
    print(' ] [ ', end='')
    print_slot(25)
    print(' ]')
    # 3층
    print("            [ ", end='')
    print_slot(15)
    print(' ] [ ', end='')
    print_slot(16)
    print(' ] [ ', end='')
    print_slot(17)
    print(' ] [ ', end='')
    print_slot(18)
    print(' ] [ ', end='')
    print_slot(19)
    print(' ] [ ', end='')
    print_slot(20)
    print(' ]')
    # 2층
    print("         [ ", end='')
    print_slot(8)
    print(' ] [ ', end='')
    print_slot(9)
    print(' ] [ ', end='')
    print_slot(10)
    print(' ] [ ', end='')
    print_slot(11)
    print(' ] [ ', end='')
    print_slot(12)
    print(' ] [ ', end='')
    print_slot(13)
    print(' ] [ ', end='')
    print_slot(14)
    print(' ]')
    # 1층
    print("      [ ", end='')
    print_slot(0)
    print(' ] [ ', end='')
    print_slot(1)
    print(' ] [ ', end='')
    print_slot(2)
    print(' ] [ ', end='')
    print_slot(3)
    print(' ] [ ', end='')
    print_slot(4)
    print(' ] [ ', end='')
    print_slot(5)
    print(' ] [ ', end='')
    print_slot(6)
    print(' ] [ ', end='')
    print_slot(7)
    print(' ]')
    # 색 정상화
    sys.stdout.flush()
    set_color(7)
    #
    print('')
    sys.stdout.flush()
    set_color(current_color)
    print('                    |', current_player, '의 덱 |')
    print('      -----------------------------------------------')
    sys.stdout.flush()
    set_color(7)
    print('       a | b | c | d | e | f | g | h | i | j | k | l ')
    sys.stdout.flush()
    set_color(current_color)
    print('      -----------------------------------------------')
    sys.stdout.flush()
    set_color(7)
    print('      ', str(wineselect_ui[0]), '|', str(wineselect_ui[1]), '|', str(wineselect_ui[2]), '|', str(wineselect_ui[3]), '|', str(wineselect_ui[4]), '|', str(wineselect_ui[5]), '|', str(wineselect_ui[6]), '|', str(wineselect_ui[7]), '|', str(wineselect_ui[8]), '|', str(wineselect_ui[9]), '|', str(wineselect_ui[10]), '|', str(wineselect_ui[11]))
    sys.stdout.flush()
    set_color(current_color)
    print('      -----------------------------------------------')
    print('')
    sys.stdout.flush()
    set_color(8)
    print('      -----------------------------------------------')
    sys.stdout.flush()
    set_color(7)

# 일반 와인잔 각각 7개, 특수 와인잔 1개의 데이터를 보관하는, 불러내는 용도의 리스트 선언
resource_wine = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F']

# 매 게임마다 wine의 값을 복사해 렌덤하게 배분하는 용도로 쓰이는 리스트 선언
wine_random = [0 for i in range(36)]

# 사용자가 와인을 선택할 때, 플레이어 별로 자료를 불러오고 수정하고 저장하는 데 쓰이는 리스트(큰 틀의 역할)
wineselect_ui = ['U' for i in range(12)]

# 피라미드를 구성하는 칸에 저장될 정보들을 담을 배열을 특징에 맞게 선언한다.
pyramid_XY=[[[0]*2 for _ in range(8)]for _ in range(8)] # 2차원 배열을 이용해 XY 평면을 구현한 배열 - 와인잔의 배치가 가능한지, 불가능한지 판단하는, 즉 게임의 규칙 판별을 위한 용도로 쓰임
pyramid_row=[[0]*3 for _ in range(36)] # 피라미드의 1층 왼쪽 칸부터 차례대로 0~35의 숫자를 지정해 만든 배열 - 2차원 배열을 1차원 배열로 변환함으로써 규칙 판별이 아닌 연산들을 단순하고 빠르게 처리하기에 적합하도록 쓰임

# pyramid_XY와 pyramid_row 배열 사이를 왔다갔다 하려면 완전히 다른 형태의 두 배열을 연결할 번호가 필요하다.
# 파이썬에는 따로 메모리를 할당하는 포인터가 없기 때문에, 이를 대체할 '주소값'을 직접 만들어 pyramid_row[x][1]에 저장한다.
# 주소값을 만드는 방법은 pyramid_XY의 x축 좌표에 10을 곱하고, y축 좌표를 더하는 것으로 했다. 피라미드는 8층으로, 배열 숫자가 7을 넘지 않기 때문에 가능하다.

# 예) pyramid_XY[2][4] = 피라미드 3층 5번째 칸
#     pyramid_row[19(피라미드 3층 5번째 칸은 전체 슬롯에서 20번째 칸이다)][1] = 2 * 10 + 4 = 24
#     위 숫자, 24를 역으로 10을 나누어 근을 pyramid의 x축 좌표, 나머지를 y축 좌표로 둔다면 pyramid_row[19]와 매칭되는 pyramid_XY[2][4]를 찾을 수 있다.
pyramid_number = 0
for a in range(8):
    for b in range(8-a):
        pyramid_row[pyramid_number][1]=(10*a+b)
        pyramid_number += 1

# pyramid[x][x][0]의 값을 1차적으로 게임 규칙에 맞게 판별해준다.
def calc_primary(X, Y):
    if(pyramid_XY[X][Y][0] == 'Filled' and pyramid_XY[X][Y+1][0] == 'Filled'):
        if(pyramid_XY[X][Y][1] == 'F' or pyramid_XY[X][Y+1][1] == 'F'):
            pyramid_XY[X+1][Y][0]='X'
        elif(pyramid_XY[X+1][Y][0] == 'Blank'):
            pyramid_XY[X+1][Y][0]='Avail'
        elif(pyramid_XY[X+1][Y][0] == 'Avail'):
            pyramid_XY[X+1][Y][0]='Avail'
    elif(pyramid_XY[X][Y][0] == 'X' or pyramid_XY[X][Y+1][0] == 'X'):
        pyramid_XY[X+1][Y][0]='X'
    elif(pyramid_XY[X][Y][1] == 'F' or pyramid_XY[X][Y+1][1] == 'F'):
        pyramid_XY[X+1][Y][0]='X'
    else:
        pyramid_XY[X+1][Y][0]='Blank'

# calc_primary를 모든 와인잔 슬롯에 대하여 실행하는 코드
def ingame_c_p():
    for a in range(7):
        for b in range(7-a):
            calc_primary(a, b)

# pyramid_XY[a][b][0]값을 if로 두고, 피라미드의 '모든 칸'에 걸쳐 다음과 같은 작업을 한다.

# pyramid_XY[a][b][0]의 값이
# Pre_Avail 일때 - pyramid_row[a+1층 b+1번째 칸 번호][0] = 'Y' 를 대입한다.
# Avail 일때 - 아래 두 와인잔이 어떤 와인잔이냐를 확인하고 이를 selected_wine과 비교한다. 규칙에 부합한다면 pyramid_row[a+1층 b+1번째 칸 번호][0] = 'Y' 를 대입하고, 부합하지 않는다면 0을 대입한다.
# Filled 일때 - pyramid_row[a+1층 b+1번째 칸 번호][0] = pyramid[x][x][1] (채워져있는 와인잔의 종류가 저장된 배열) 을 대입한다.
# Blank 일때 - pyramid_row[a+1층 b+1번째 칸 번호][0] = 0을 대입한다.
# X 일때 - 와인잔을 넣는 것 자체가 불가능한 상황이므로, pyramid_row[a+1층 b+1번째 칸 번호][0] = 'X'를 대입한다.

# 위 작업이 끝나면 pyramid_row[a+1층 b+1번째 칸 번호][0]에는 'Y', 0, 'X'가 대입되어 있고, 각각 와인잔 쌓기 가능, 판정 보류, 불가임을 뜻한다.
# 또한 pyramid_row[x][2]에 상황에 맞는 색코드를 저장한다. 화면 출력 시 사용된다.
def calc_secondary(X, Y, slot_num, selected_wine):
    if(pyramid_XY[X][Y][0]=='Pre_Avail'):
        pyramid_XY[X][Y][1]='V'
        pyramid_row[slot_num][0]='Y'
        pyramid_row[slot_num][2]=2 # 초록색 색코드 저장
    elif(pyramid_XY[X][Y][0]=='Avail'):
        if(selected_wine =='A' and (pyramid_XY[X-1][Y][1]=='A' or pyramid_XY[X-1][Y+1][1]=='A')):
            pyramid_XY[X][Y][1]='V'
            pyramid_row[slot_num][0]='Y'
            pyramid_row[slot_num][2]=2 # 초록색 색코드 저장
        elif(selected_wine =='B' and (pyramid_XY[X-1][Y][1]=='B' or pyramid_XY[X-1][Y+1][1]=='B')):
            pyramid_XY[X][Y][1]='V'
            pyramid_row[slot_num][0]='Y'
            pyramid_row[slot_num][2]=2 # 초록색 색코드 저장
        elif(selected_wine =='C' and (pyramid_XY[X-1][Y][1]=='C' or pyramid_XY[X-1][Y+1][1]=='C')):
            pyramid_XY[X][Y][1]='V'
            pyramid_row[slot_num][0]='Y'
            pyramid_row[slot_num][2]=2 # 초록색 색코드 저장
        elif(selected_wine =='D' and (pyramid_XY[X-1][Y][1]=='D' or pyramid_XY[X-1][Y+1][1]=='D')):
            pyramid_XY[X][Y][1]='V'
            pyramid_row[slot_num][0]='Y'
            pyramid_row[slot_num][2]=2 # 초록색 색코드 저장
        elif(selected_wine =='E' and (pyramid_XY[X-1][Y][1]=='E' or pyramid_XY[X-1][Y+1][1]=='E')):
            pyramid_XY[X][Y][1]='V'
            pyramid_row[slot_num][0]='Y'
            pyramid_row[slot_num][2]=2 # 초록색 색코드 저장
        elif(selected_wine == 'F'):
            pyramid_XY[X][Y][1]='V'
            pyramid_row[slot_num][0]='Y'
            pyramid_row[slot_num][2]=2 # 초록색 색코드 저장
        else:
            pyramid_XY[X][Y][1]=0
            pyramid_row[slot_num][0]=0
            pyramid_row[slot_num][2]=7 # 기본 흰색 색코드 저장
    elif(pyramid_XY[X][Y][0]=='Filled'):
        pyramid_row[slot_num][0]=pyramid_XY[X][Y][1]
        if(pyramid_XY[X][Y][1]=='A'):
            pyramid_row[slot_num][2]=11 # 하늘색 색코드 저장
        elif(pyramid_XY[X][Y][1]=='B'):
            pyramid_row[slot_num][2]=14 # 노랑색 색코드 저장
        elif(pyramid_XY[X][Y][1]=='C'):
            pyramid_row[slot_num][2]=10 # 연두색 색코드 저장
        elif(pyramid_XY[X][Y][1]=='D'):
            pyramid_row[slot_num][2]=9 # 파랑색 색코드 저장
        elif(pyramid_XY[X][Y][1]=='E'):
            pyramid_row[slot_num][2]=5 # 짙은핑크색 색코드 저장
        elif(pyramid_XY[X][Y][1]=='F'):
            pyramid_row[slot_num][2]=12 # 밝은 빨간색 색코드 저장
        else:
            pyramid_row[slot_num][2]=7 # 기본 흰색 색코드 저장
    elif(pyramid_XY[X][Y][0]=='Blank'):
        pyramid_XY[X][Y][1]=0
        pyramid_row[slot_num][0]=0
        pyramid_row[slot_num][2]=7 # 기본 흰색 색코드 저장
    elif(pyramid_XY[X][Y][0]=='X'):
        pyramid_XY[X][Y][1]='X'
        pyramid_row[slot_num][0]='X'
        pyramid_row[slot_num][2]=8 # 회색 색코드 저장

# calc_secondary를 모든 와인잔 슬롯에 대하여 실행하는 코드
def ingame_c_s(selected_wine):
    pyramid_number = 0
    for a in range(8):
        for b in range(8-a):
            calc_secondary(a, b, pyramid_number, selected_wine)
            pyramid_number += 1

# 와인잔을 쌓을 수 있는 자리를 표시하고 계산하느라 변경된 모든 pyramid_row[x][0] 값들을 '(와인잔)', 0, 'X'로 일괄 처리한다.
# 플레이어의 턴이 끝나고 모든 계산이 끝나 화면에 현재까지 와인잔이 어떻게 쌓였고, 어디를 둘 수 없는지 표시할 때 쓴다.
def organize_screen(X, Y, slot_num):
    if(pyramid_XY[X][Y][0]=='Pre_Avail'):
        pyramid_XY[X][Y][1]='V'
        pyramid_row[slot_num][0]=0
        pyramid_row[slot_num][2]=7 # 기본 흰색 색코드 저장
    elif(pyramid_XY[X][Y][0]=='Avail'):
        pyramid_XY[X][Y][1]='V'
        pyramid_row[slot_num][0]=0
        pyramid_row[slot_num][2]=7 # 기본 흰색 색코드 저장
    elif(pyramid_XY[X][Y][0]=='Filled'):
        pyramid_row[slot_num][0]=pyramid_XY[X][Y][1]
        if(pyramid_XY[X][Y][1]=='A'):
            pyramid_row[slot_num][2]=11 # 하늘색 색코드 저장
        elif(pyramid_XY[X][Y][1]=='B'):
            pyramid_row[slot_num][2]=14 # 노랑색 색코드 저장
        elif(pyramid_XY[X][Y][1]=='C'):
            pyramid_row[slot_num][2]=10 # 연두색 색코드 저장
        elif(pyramid_XY[X][Y][1]=='D'):
            pyramid_row[slot_num][2]=9 # 파랑색 색코드 저장
        elif(pyramid_XY[X][Y][1]=='E'):
            pyramid_row[slot_num][2]=5 # 짙은핑크색 색코드 저장
        elif(pyramid_XY[X][Y][1]=='F'):
            pyramid_row[slot_num][2]=12 # 밝은 빨간색 색코드 저장
        else:
            pyramid_row[slot_num][2]=7 # 기본 흰색 색코드 저장
    elif(pyramid_XY[X][Y][0]=='Blank'):
        pyramid_XY[X][Y][1]=0
        pyramid_row[slot_num][0]=0
        pyramid_row[slot_num][2]=7 # 기본 흰색 색코드 저장
    elif(pyramid_XY[X][Y][0]=='X'):
        pyramid_XY[X][Y][1]='X'
        pyramid_row[slot_num][0]='X'
        pyramid_row[slot_num][2]=8 # 회색 색코드 저장

# organize_screen를 모든 와인잔 슬롯에 대하여 실행하는 코드
def ingame_o_s():
    pyramid_number = 0
    for a in range(8):
        for b in range(8-a):
            organize_screen(a, b, pyramid_number)
            pyramid_number += 1

# 와인잔을 선택했을 시 wineselect_ui에서 일어나는 계산
# num 값이 0이면 select_confirm은 값을 반환하는데 쓰이고, num 값이 1이면 값을 수정하는데 쓰이고, num 값이 2이면 - 값을 반환할 때 오류를 띄우기 위해 쓰인다.
def select_confirm(typed, num):
    if(typed == 'A' or typed == 'a'):
        if(num==0):
            return wineselect_ui[0]
        elif(num==2 and wineselect_ui[0] == "-"):
            return 1
        elif(num==1):
            wineselect_ui[0] = "-"
    elif(typed == 'B' or typed == 'b'):
        if(num==0):
            return wineselect_ui[1]
        elif(num==2 and wineselect_ui[1] == "-"):
            return 1            
        elif(num==1):
            wineselect_ui[1] = "-"
    elif(typed == 'C' or typed == 'c'):
        if(num==0):
            return wineselect_ui[2]
        elif(num==2 and wineselect_ui[2] == "-"):
            return 1
        elif(num==1):
            wineselect_ui[2] = "-"
    elif(typed == 'D' or typed == 'd'):
        if(num==0):
            return wineselect_ui[3]
        elif(num==2 and wineselect_ui[3] == "-"):
            return 1
        elif(num==1):
            wineselect_ui[3] = "-"
    elif(typed == 'E' or typed == 'e'):
        if(num==0):
            return wineselect_ui[4]
        elif(num==2 and wineselect_ui[4] == "-"):
            return 1
        elif(num==1):
            wineselect_ui[4] = "-"
    elif(typed == 'F' or typed == 'f'):
        if(num==0):
            return wineselect_ui[5]
        elif(num==2 and wineselect_ui[5] == "-"):
            return 1
        elif(num==1):
            wineselect_ui[5] = "-"
    elif(typed == 'G' or typed == 'g'):
        if(num==0):
            return wineselect_ui[6]
        elif(num==2 and wineselect_ui[6] == "-"):
            return 1
        elif(num==1):
            wineselect_ui[6] = "-"
    elif(typed == 'H' or typed == 'h'):
        if(num==0):
            return wineselect_ui[7]
        elif(num==2 and wineselect_ui[7] == "-"):
            return 1
        elif(num==1):
            wineselect_ui[7] = "-"
    elif(typed == 'I' or typed == 'i'):
        if(num==0):
            return wineselect_ui[8]
        elif(num==2 and wineselect_ui[8] == "-"):
            return 1
        elif(num==1):
            wineselect_ui[8] = "-"
    elif(typed == 'J' or typed == 'j'):
        if(num==0):
            return wineselect_ui[9]
        elif(num==2 and wineselect_ui[9] == "-"):
            return 1
        elif(num==1):
            wineselect_ui[9] = "-"
    elif(typed == 'K' or typed == 'k'):
        if(num==0):
            return wineselect_ui[10]
        elif(num==2 and wineselect_ui[10] == "-"):
            return 1
        elif(num==1):
            wineselect_ui[10] = "-"
    elif(typed == 'L' or typed == 'l'):
        if(num==0):
            return wineselect_ui[11]
        elif(num==2 and wineselect_ui[11] == "-"):
            return 1
        elif(num==1):
            wineselect_ui[11] = "-"
    elif(typed == 'Y' or typed == 'y'):
        if(num==0):
            return 0
    else:
        if(num==0):
            return 1

# 턴 넘김 여부 확인용 코드
def calc_turnpass(X, Y, selected_wine):
    if(pyramid_XY[X][Y][0]=='Pre_Avail'):
        return 1
    elif(pyramid_XY[X][Y][0]=='Avail'):
        if(selected_wine =='A' and (pyramid_XY[X-1][Y][1]=='A' or pyramid_XY[X-1][Y+1][1]=='A')):
            return int(1)
        elif(selected_wine =='B' and (pyramid_XY[X-1][Y][1]=='B' or pyramid_XY[X-1][Y+1][1]=='B')):
            return int(1)
        elif(selected_wine =='C' and (pyramid_XY[X-1][Y][1]=='C' or pyramid_XY[X-1][Y+1][1]=='C')):
            return int(1)
        elif(selected_wine =='D' and (pyramid_XY[X-1][Y][1]=='D' or pyramid_XY[X-1][Y+1][1]=='D')):
            return int(1)
        elif(selected_wine =='E' and (pyramid_XY[X-1][Y][1]=='E' or pyramid_XY[X-1][Y+1][1]=='E')):
            return int(1)
        elif(selected_wine == 'F'):
            return int(1)
    else:
        return int(0)

# calc_turnpass를 모든 와인잔 슬롯에 대하여 실행하는 함수
def ingame_c_t(selected_wine):
    sum = 0
    for a in range(8):
        for b in range(8-a):
            if(calc_turnpass(a, b, selected_wine) == 1):
                sum = sum + int(calc_turnpass(a, b, selected_wine))
            else:
                continue
    return sum

# 선택한 와인잔이 둘 수 있는 곳이 없는 와인잔일 때 입력을 거부하는 함수
def ingame_input(selected_wine):
    wine_input = 'No'
    for a in range(8):
        for b in range(8-a):
            if(calc_turnpass(a, b, selected_wine) == 1):
                wine_input = 'Yes'
            else:
                continue
    return wine_input

# 입력 가능한 자리에 숫자 입력
def ingame_avail():
    for a in range(8):
        for b in range(36):
            if(pyramid_row[b][0] == 'Y'):
                pyramid_row[b][0]=(a+1)
                break

# 게임 종료 판별 함수
def game_over():
    go_point = 0
    for a in range(12):
            if(player_1[a]=="-"):
                continue
            else:
                go_point = go_point + int(ingame_c_t(player_1[a]))
    for a in range(12):
            if(player_2[a]=="-"):
                continue
            else:
                go_point = go_point + int(ingame_c_t(player_2[a]))
    for a in range(12):
            if(player_3[a]=="-"):
                continue
            else:
                go_point = go_point + int(ingame_c_t(player_3[a]))
    if(go_point == 0):
        return int(1)
    else:
        return int(0)

# 5초 카운터
def time_counter():
    sec = int(5)
    while(sec != 0):
        sec = sec-1
        time.sleep(1)
        if(sec==4):
            print("      >", end='')
        elif(sec==3):
            print(">", end='')
        elif(sec==2):
            print(">", end='')
        elif(sec==1):
            print(">", end='')
        elif(sec==0):
            os.system('cls')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 게임 시작

# wine_random에 resource_wine 불러옴
wine_random = resource_wine

# random.shuffle을 이용해 wine_random의 내용물을 섞음
random.shuffle(wine_random)

# 플레이어 1, 2, 3에 개수에 맞게 와인잔을 배분함
player_1 = wine_random[0:12]
player_2 = wine_random[12:24]
player_3 = wine_random[24:36]

# 각각의 리스트를 알파벳 순으로 정렬함
player_1.sort()
player_2.sort()
player_3.sort()

# 플레이어 1, 2, 3의 와인잔 개수
player1_wine = 12
player2_wine = 12
player3_wine = 12

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 플레이어 1 턴, 게임 초기 설정
# player 1번
player1 = "<<"
player2 = "  "
player3 = "  "

# wineselect_ui에 플레이어 1의 와인잔 로드
wineselect_ui = player_1

# calc_primary를 통해 모든 pyramid_XY[x][x][0] = Blank 처리
ingame_c_p()

# 1층 pyramid_XY[x][x][0] = Pre_Avail 처리
for a in range(8):
    pyramid_XY[0][a][0]='Pre_Avail'

# calc_secondary를 통해 pyramid_XY[x][x][1]과 pyramid_row[x][0]에 올바른 값 대입. 선택한 와인잔이 없으니, 선택한게 없다는 뜻으로 0값을 넣어준다.
ingame_c_s(0)

# organize_screen으로 pyramid_row[x][0], pyramid_row[x][2] 정리
ingame_o_s()

# 피라미드 & 입력 문구 출력 (player_1 자료 불러옴)
output = print_gamescreen(p1_color, '플레이어 1')
print("      와인잔을 선택해주세요.")
received = input("      : ")
received_alphabet = received

# 화면 삭제
os.system('cls')

# selected_wine은 함수 select_confirm을 거쳐서, 플레이어가 인풋한 알파벳 값을 대응하는 와인잔을 값으로 받게 된다
selected_wine = select_confirm(received_alphabet, 0)

# avail_wine을 통해 pyramid_XY[x][x][1]과 pyramid_row[x][0]에 올바른 값 대입
ingame_c_s(selected_wine)

# pyramid_row[x][0] = 'Y', 즉 선택 가능한 구역을 스캔해서 찾으면 'Y'를 0~7까지의 숫자로 순서대로 변경
ingame_avail()

# 와인잔을 놓을 수 있는 자리를 표시하고 Y를 입력하면 선택을 할 수 있게 함. Y를 입력할 때 까지 와인잔을 선택할 수 있음
# 모든 경우의 오류를 방지함
confirm = 0
error = 0
while(confirm == 0):
    output = print_gamescreen(p1_color, '플레이어 1')
    if(error == 0):
        print("      선택하신", received, "슬롯에는", selected_wine, "와인잔이 있습니다.")
        print("      사용한다 : Y | 사용하지 않는다면 다른 와인잔을 선택해주세요.")
    elif(error == 1):
        print("      입력이 올바르지 않습니다.")
        print("      올바른 문자를 입력해주세요.")
    elif(error == 2):
        print("      선택한 와인잔은 배치가 불가능합니다(공간 부족).")
        print("      다른 와인잔을 선택해주세요.")
    elif(selected_wine == "-"):
        print("      이 칸은 와인잔이 비어있습니다.")
        print("      다른 와인잔을 선택해주세요.")
    received = input("      : ")
    if(select_confirm(received, 0) == 0 and error == 0):
        if(selected_wine != "-" and ingame_input(selected_wine) == 'Yes'):
            confirm = 1
        elif(selected_wine != "-" and ingame_input(selected_wine) == 'No'):
            os.system('cls')
            error = 2
            continue
        else:
            os.system('cls')
            error = 1
            continue
    elif(select_confirm(received, 0) == 0 and error == 1):
        os.system('cls')
        error = 1
        continue
    elif(select_confirm(received, 0) == 1):
        os.system('cls')
        error = 1
        continue
    elif(select_confirm(received, 2) == 1):
        os.system('cls')
        error = 1
        continue
    else:
        os.system('cls')
        error = 0
        received_alphabet = received
        selected_wine = select_confirm(received_alphabet, 0)
        ingame_c_s(selected_wine)
        ingame_avail()
os.system('cls')

# 피라미드 & 입력 문구 출력
print_gamescreen(p1_color, '플레이어 1')
print("      선택하신 와인잔은", selected_wine, "와인잔입니다.")
print("      와인잔을 쌓을 자리를 입력해주세요.")
selected_slot = int(input("      : "))

# 화면 삭제
os.system('cls')

# 선택한 자리의 숫자와 일치하는 pyramid_row[a][0]을 찾고, pyramid_row[a][1]에 저장된 '주소값'을 불러내어 해당하는 pyramid_XY의 pyramid_XY[x][x][0]값을 'Filled', pyramid_XY[x][x][1]값을 선택한 와인잔으로 바꾼다.
for a in range(36):
    if(pyramid_row[a][0] == selected_slot):
        pyramid_XY[int(pyramid_row[a][1])//10][int(pyramid_row[a][1])%10][0] = 'Filled'
        pyramid_XY[int(pyramid_row[a][1])//10][int(pyramid_row[a][1])%10][1] = selected_wine
    else:
        continue

# 큰 규칙 어긋나지 않았는지 확인
ingame_c_p()

# organize_screen으로 pyramid_row[x][0], pyramid_row[x][2] 정리
ingame_o_s()

# 고른 와인잔은 -로 바꾸어 비어있음을 알린다
select_confirm(received_alphabet, 1)

# '-'로 바꿔 입력
player_1 = wineselect_ui

# player 1 와인잔 개수 1 차감
player1_wine = player1_wine - 1

# 다음 턴
print_gamescreen(p1_color, '플레이어 1')
print("      5초 후 다음 플레이어의 턴으로 넘어갑니다.")
time_counter()





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 여기서부터는 플레이어1,2,3이 턴을 넘기며, GameOver가 1이 되는 조건이 나올 때 까지 계속 반복
# GameOver 판정 변수 초깃값
GameOver = 0
while(GameOver != 1):
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # GameOver 판정
    GameOver = int(game_over())    
    # 플레이어 2 턴
    player1 = "  "
    player2 = "<<"
    player3 = "  "
    wineselect_ui = player_2
    ingame_c_p()
    ingame_o_s()
    # 턴넘김 여부 확인
    turnpass = 0
    for a in range(12):
        if(wineselect_ui[a]=="-"):
            continue
        else:
            turnpass = turnpass + int(ingame_c_t(wineselect_ui[a]))
    if(turnpass == 0):
        print_gamescreen(p2_color, '플레이어 2')
        print("      쌓을 수 있는 와인잔이 없어 자동으로 5초 후")
        print("      다음 플레이어의 턴으로 넘어갑니다.")
        time_counter()
    else:    
        # 와인잔을 선택하세요
        output = print_gamescreen(p2_color, '플레이어 2')
        print("      와인잔을 선택해주세요.")
        print('')
        received = input("      : ")
        received_alphabet = received
        os.system('cls')
        # 화면 뒷 작업
        selected_wine = select_confirm(received_alphabet, 0)
        ingame_c_s(selected_wine)
        ingame_avail()
        # 와인잔 선택 반복문 시작
        confirm = 0
        error = 0
        while(confirm == 0):
            output = print_gamescreen(p2_color, '플레이어 2')
            if(error == 0):
                print("      선택하신", received, "슬롯에는", selected_wine, "와인잔이 있습니다.")
                print("      사용한다 : Y | 사용하지 않는다면 다른 와인잔을 선택해주세요.")
            elif(error == 1):
                print("      입력이 올바르지 않습니다.")
                print("      올바른 위치를 입력해주세요.")
            elif(error == 2):
                print("      선택한 와인잔은 배치가 불가능합니다(공간 부족).")
                print("      다른 와인잔을 선택해주세요.")
            elif(selected_wine == "-"):
                print("      입력이 올바르지 않습니다.")
                print("      올바른 위치를 입력해주세요.")
            received = input("      : ")
            if(select_confirm(received, 0) == 0 and error == 0):
                if(selected_wine != "-" and ingame_input(selected_wine) == 'Yes'):
                    confirm = 1
                elif(selected_wine != "-" and ingame_input(selected_wine) == 'No'):
                    os.system('cls')
                    error = 2
                    continue
                else:
                    os.system('cls')
                    error = 1
                    continue
            elif(select_confirm(received, 0) == 0 and error == 1):
                os.system('cls')
                error = 1
                continue
            elif(select_confirm(received, 0) == 1):
                os.system('cls')
                error = 1
                continue
            elif(select_confirm(received, 2) == 1):
                os.system('cls')
                error = 1
                continue
            else:
                os.system('cls')
                error = 0
                received_alphabet = received
                selected_wine = select_confirm(received_alphabet, 0)
                ingame_c_s(selected_wine)
                ingame_avail()
        os.system('cls')
        # 놓고 싶은 자리를 입력하세요
        print_gamescreen(p2_color, '플레이어 2')
        print("      선택하신 와인잔은", selected_wine, "와인잔입니다.")
        print("      와인잔을 쌓을 자리를 입력해주세요.")
        selected_slot = int(input("      : "))
        os.system('cls')
        # 화면 뒷 작업
        for a in range(36):
            if(pyramid_row[a][0] == selected_slot):
                pyramid_XY[int(pyramid_row[a][1])//10][int(pyramid_row[a][1])%10][0] = 'Filled'
                pyramid_XY[int(pyramid_row[a][1])//10][int(pyramid_row[a][1])%10][1] = selected_wine
            else:
                continue
        ingame_c_p()
        ingame_o_s()
        select_confirm(received_alphabet, 1)
        player_2 = wineselect_ui
        # player 2 와인잔 개수 1 차감
        player2_wine = player2_wine - 1
        # 다음 턴
        print_gamescreen(p2_color, '플레이어 2')
        print("      5초 후 다음 플레이어의 턴으로 넘어갑니다.")
        time_counter()
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # GameOver 판정
    GameOver = int(game_over())    
    # 플레이어 3 턴
    player1 = "  "
    player2 = "  "
    player3 = "<<"  
    wineselect_ui = player_3
    ingame_c_p()
    ingame_o_s()
    # 턴넘김 여부 확인
    turnpass = 0
    for a in range(12):
        if(wineselect_ui[a]=="-"):
            continue
        else:
            turnpass = turnpass + int(ingame_c_t(wineselect_ui[a]))
    if(turnpass == 0):
        print_gamescreen(p3_color, '플레이어 3')
        print("      쌓을 수 있는 와인잔이 없어 자동으로")
        print("      5초 후 다음 플레이어의 턴으로 넘어갑니다.")
        time_counter()
    else:       
        # 와인잔을 선택하세요
        output = print_gamescreen(p3_color, '플레이어 3')
        print("      와인잔을 선택해주세요.")
        print('')
        received = input("      : ")
        received_alphabet = received
        os.system('cls')
        # 화면 뒷 작업
        selected_wine = select_confirm(received_alphabet, 0)
        ingame_c_s(selected_wine)
        ingame_avail()
        # 와인잔 선택 반복문 시작
        confirm = 0
        error = 0
        while(confirm == 0):
            output = print_gamescreen(p3_color, '플레이어 3')
            if(error == 0):
                print("      선택하신", received, "슬롯에는", selected_wine, "와인잔이 있습니다.")
                print("      사용한다 : Y | 사용하지 않는다면 다른 와인잔을 선택해주세요.")
            elif(error == 1):
                print("      입력이 올바르지 않습니다.")
                print("      올바른 위치를 입력해주세요.")
            elif(error == 2):
                print("      선택한 와인잔은 배치가 불가능합니다(공간 부족).")
                print("      다른 와인잔을 선택해주세요.")
            elif(selected_wine == "-"):
                print("      입력이 올바르지 않습니다.")
                print("      올바른 위치를 입력해주세요.")
            received = input("      : ")
            if(select_confirm(received, 0) == 0 and error == 0):
                if(selected_wine != "-" and ingame_input(selected_wine) == 'Yes'):
                    confirm = 1
                elif(selected_wine != "-" and ingame_input(selected_wine) == 'No'):
                    os.system('cls')
                    error = 2
                    continue                    
                else:
                    os.system('cls')
                    error = 1
                    continue
            elif(select_confirm(received, 0) == 0 and error == 1):
                os.system('cls')
                error = 1
                continue
            elif(select_confirm(received, 0) == 1):
                os.system('cls')
                error = 1
                continue
            elif(select_confirm(received, 2) == 1):
                os.system('cls')
                error = 1
                continue
            else:
                os.system('cls')
                error = 0
                received_alphabet = received
                selected_wine = select_confirm(received_alphabet, 0)
                ingame_c_s(selected_wine)
                ingame_avail()
        os.system('cls')
        # 놓고 싶은 자리를 입력하세요
        print_gamescreen(p3_color, '플레이어 3')
        print("      선택하신 와인잔은", selected_wine, "와인잔입니다.")
        print("      와인잔을 쌓을 자리를 입력해주세요.")
        selected_slot = int(input("      : "))
        os.system('cls')
        # 화면 뒷 작업
        for a in range(36):
            if(pyramid_row[a][0] == selected_slot):
                pyramid_XY[int(pyramid_row[a][1])//10][int(pyramid_row[a][1])%10][0] = 'Filled'
                pyramid_XY[int(pyramid_row[a][1])//10][int(pyramid_row[a][1])%10][1] = selected_wine
            else:
                continue
        ingame_c_p()
        ingame_o_s()
        select_confirm(received_alphabet, 1)
        player_3 = wineselect_ui
        # player 3 와인잔 개수 1 차감
        player3_wine = player3_wine - 1
        # 다음 턴
        print_gamescreen(p3_color, '플레이어 3')
        print("      5초 후 다음 플레이어의 턴으로 넘어갑니다.")
        time_counter()
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # GameOver 판정
    GameOver = int(game_over())
    # 플레이어 1 턴
    player1 = "<<"
    player2 = "  "
    player3 = "  "
    wineselect_ui = player_1
    ingame_c_p()
    ingame_o_s()
    # 턴넘김 여부 확인
    turnpass = 0
    for a in range(12):
        if(wineselect_ui[a]=="-"):
            continue
        else:
            turnpass = turnpass + int(ingame_c_t(wineselect_ui[a]))
    if(turnpass == 0):
        print_gamescreen(p1_color, '플레이어 1')
        print("      쌓을 수 있는 와인잔이 없어 자동으로 5초 후")
        print("      다음 플레이어의 턴으로 넘어갑니다.")
        time_counter()
    else:      
        # 와인잔을 선택하세요
        output = print_gamescreen(p1_color, '플레이어 1')
        print("      와인잔을 선택해주세요.")
        print('')
        received = input("      : ")
        received_alphabet = received
        os.system('cls')
        # 화면 뒷 작업
        selected_wine = select_confirm(received_alphabet, 0)
        ingame_c_s(selected_wine)
        ingame_avail()
        # 와인잔 선택 반복문 시작
        confirm = 0
        error = 0
        while(confirm == 0):
            output = print_gamescreen(p1_color, '플레이어 1')
            if(error == 0):
                print("      선택하신", received, "슬롯에는", selected_wine, "와인잔이 있습니다.")
                print("      사용한다 : Y | 사용하지 않는다면 다른 와인잔을 선택해주세요.")
            elif(error == 1):
                print("      입력이 올바르지 않습니다.")
                print("      올바른 위치를 입력해주세요.")
            elif(error == 2):
                print("      선택한 와인잔은 배치가 불가능합니다(공간 부족).")
                print("      다른 와인잔을 선택해주세요.")
            elif(selected_wine == "-"):
                print("      입력이 올바르지 않습니다.")
                print("      올바른 위치를 입력해주세요.")
            received = input("      : ")
            if(select_confirm(received, 0) == 0 and error == 0):
                if(selected_wine != "-" and ingame_input(selected_wine) == 'Yes'):
                    confirm = 1
                elif(selected_wine != "-" and ingame_input(selected_wine) == 'No'):
                    os.system('cls')
                    error = 2
                    continue
                else:
                    os.system('cls')
                    error = 1
                    continue
            elif(select_confirm(received, 0) == 0 and error == 1):
                os.system('cls')
                error = 1
                continue
            elif(select_confirm(received, 0) == 1):
                os.system('cls')
                error = 1
                continue
            elif(select_confirm(received, 2) == 1):
                os.system('cls')
                error = 1
                continue
            else:
                os.system('cls')
                error = 0
                received_alphabet = received
                selected_wine = select_confirm(received_alphabet, 0)
                ingame_c_s(selected_wine)
                ingame_avail()
        os.system('cls')
        # 놓고 싶은 자리를 입력하세요
        print_gamescreen(p1_color, '플레이어 1')
        print("      선택하신 와인잔은", selected_wine, "와인잔입니다.")
        print("      와인잔을 쌓을 자리를 입력해주세요.")
        selected_slot = int(input("      : "))
        os.system('cls')
        # 화면 뒷 작업
        for a in range(36):
            if(pyramid_row[a][0] == selected_slot):
                pyramid_XY[int(pyramid_row[a][1])//10][int(pyramid_row[a][1])%10][0] = 'Filled'
                pyramid_XY[int(pyramid_row[a][1])//10][int(pyramid_row[a][1])%10][1] = selected_wine
            else:
                continue
        ingame_c_p()
        ingame_o_s()
        select_confirm(received_alphabet, 1)
        player_1 = wineselect_ui
        # player 1 와인잔 개수 1 차감
        player1_wine = player1_wine - 1
        # 다음 턴
        print_gamescreen(p1_color, '플레이어 1')
        print("      5초 후 다음 플레이어의 턴으로 넘어갑니다.")
        time_counter()
os.system('cls')

# 승리자 판별
if(player1_wine<player2_wine and player1_wine<player3_wine):
    winner = "플레이어 1"
elif(player2_wine<player1_wine and player2_wine<player3_wine):
    winner = "플레이어 2"
elif(player3_wine<player1_wine and player3_wine<player2_wine):
    winner = "플레이어 3"
elif(player1_wine==player2_wine and player1_wine<player3_wine):
    winner = "플레이어 1 & 플레이어 2"
elif(player2_wine<player1_wine and player2_wine==player3_wine):
    winner = "플레이어 2 & 플레이어 3"
elif(player3_wine==player1_wine and player3_wine<player2_wine):
    winner = "플레이어 3 & 플레이어 1"
elif(player1_wine==player2_wine==player3_wine):
    winner = "플레이어 1 & 플레이어 2 & 플레이어 3"

print('승리자 |', winner)
sys.stdout.flush()
set_color(112)
print('        …………………………………       ')
sys.stdout.flush()
set_color(14)
print('🎈⁝  ✨승리하셨습니다!✨ ⁝🎈')
sys.stdout.flush()
set_color(112)
print('        …………………………………       ')
sys.stdout.flush()
set_color(7)
print('             👑            ')
print('    🎉   ¯l_(ツ)_/¯   🎉   ')
print('            ( )             ')
print('            / )             ')