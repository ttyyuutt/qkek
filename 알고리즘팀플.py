import os
global hunger
hunger = 0
global thirst
thirst = 0
global happy
happy = 0
global well
well = 0
global tired
tired = 0
global health
health = 0
global day
day = 1
global book_1
global book_2
global book_3
global act_1
global act_2
global act_3
global act_4
global act_5
act_1=0
act_2=0
act_3=0
act_4=0
act_5=0
book_1=0
book_2=0
book_3=0

def act_clear():
    global act_1,act_2,act_3,act_4,act_5
    act_1 = 0
    act_2 = 0
    act_3 = 0
    act_4 = 0
    act_5 = 0

os.system('cls')
print(" ★　　　 　★　°　　　•　✯")
print("　　　♬　*　　　　　°　　　　★ 　°·　　   ●")
print("　　　 　★　°　☄　　•　　.°•　　　")
print("　　　　*　　　　　°　　　　 　°·　　   ")
print("   ★　　　 　★　°　　●　•　　.°•　　✯")
print("　　 　★　°　　　•　　.°•　　 ")
print("　　　*　　　☄　　°　　　　★ 　°·　　   ")
print("　　　 　　°　　　•　　.°•　　　")
print("　　　♬　*　　　　　°　 　°·　　   ●")
print("    ★　　　 　★　°　　　•　　.°•　　　★ ")
print("　　　　*　　　　　°　　　　　°·　　   ")
print("　　　*　　　　　°　　　　★ 　°·　　   ")
print(".　　　•　° ★　•  ☄")
print("▁▂▃▄▅▆▇▇▆▅▄▃▂▁                   [너에게 고양이를]")
print("*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*")
input("             <<게임을 시작하려면 엔터 >>")

def cat1():
    print()
    print(" 　　　　  ／＞　　 フ")
    print("　　　　　 | 　_　 _l")
    print("　 　　   ／` ミ  Yノ")
    print("　　 　 /　　　 　 |")
    print("　　　 /　 ヽ　　 ﾉ")
    print("　 　 │　　|　|　|")
    print("　／￣|　　 |　|　|")
    print("　| (￣ヽ＿_ヽ_)__)")
    print("　＼二つ")
    print("*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*")

def cat2():
    print()
    print(" 　　　　  ／＞　　 フ")
    print("　　　　　 | 　_　 *l")
    print("　 　　   ／` ミ  Yノ")
    print("　　 　 /　　　 　 |")
    print("　　　 /　 ヽ　　 ﾉ")
    print("　 　 │　　|　|　|")
    print("　／￣|　　 |　|　|")
    print("　| (￣ヽ＿_ヽ_)__)")
    print("　＼二つ")
    print("*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*")

def cat3():
    print()
    print(" 　　　　  ／＞　　 フ")
    print("　　　　　 | 　*　 *l")
    print("　 　　   ／` ミ  Yノ")
    print("　　 　 /　　　 　 |")
    print("　　　 /　 ヽ　　 ﾉ")
    print("　 　 │　　|　|　|")
    print("　／￣|　　 |　|　|")
    print("　| (￣ヽ＿_ヽ_)__)")
    print("　＼二つ")
    print("*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*")

def cat4():
    print()
    print(" 　　　　  ／＞　　 フ")
    print("　　　　　 | 　★　★l     ---^--")
    print("　 　　   ／` ミ  Yノ")
    print("　　 　 /　　　 　 |")
    print("　　　 /　 ヽ　　 ﾉ")
    print("　 　 │　　|　|　|")
    print("　／￣|　　 |　|　|")
    print("　| (￣ヽ＿_ヽ_)__)")
    print("　＼二つ")
    print("*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*")

def egg1():
    print()
    print()
    print()
    print()
    print("                                      __ ")
    print("                                    /    ＼")
    print("                                   |      |")
    print("                                   |      |")
    print("                                   ＼____ / ")
    print("*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*")
def egg2():
    print("   #",day,"일차                                ",player_name," [",pet_name,"]")
    print("           포만[",hunger,"] 갈증[",thirst,"] 행복[",happy,"] 체력[",well,"] 피로[",tired,"] 청결[",health,"]")
    print()
    print()
    print("                                      __ ")
    print("                                    /    ＼")
    print("                                   |      |")
    print("                                   |      |")
    print("                                   ＼____ / ")
    print("*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*")

def egg():
    print("   #",day,"일차                             ",player_name," [",pet_name,"]")
    print("           포만[",hunger,"] 갈증[",thirst,"] 행복[",happy,"] 체력[",well,"] 피로[",tired,"] 청결[",health,"]")
    print()
    print()
    print("                                      __ ")
    print("                                    /    ＼")
    print("                                   |      |")
    print("                                   |      |")
    print("                                   ＼____ / ")
    print("*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*")
    print("      1. 쓰다듬기 2. 먹이주기 3. 산책가기 4. 씻겨주기 5. 책 읽어주기 6. 자기")
    print("*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*")
def baby():
    print("   #",day,"일차                             ",player_name," [",pet_name,"]")
    print("           포만[",hunger,"] 갈증[",thirst,"] 행복[",happy,"] 체력[",well,"] 피로[",tired,"] 청결[",health,"]")
    print()
    print()
    print("             　　 　　　/ﾞﾐヽ､,,___,,／ﾞヽ")
    print("             　　 　　　i ノ　　 川　｀ヽ")
    print("             　　 　　　/　｀ ・　 ．・ i､")
    print("             　　 　　彡,　  ミ(_,人_)彡ミ")
    print("             　   ∩, /　ヽ､,　 　　　ノ")
    print("             　   丶ニ|　　   '''-'´ﾉ")
    print("            　　　　  ∪⌒∪''￣￣∪")
    print("*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*")
    print("      1. 쓰다듬기 2. 먹이주기 3. 산책가기 4. 씻겨주기 5. 책 읽어주기 6. 자기")
    print("*ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ*")

def end1():
    os.system('cls')
    cat4()
    print("튜토리얼 : 너.. 애를 어쩌다 이 지경으로 만든거냐")
    input()
    print("튜토리얼 : 잔인하구나..")
    input()
    print("튜토리얼 : 이 아이는 내가 살려내서 다른 주인에게 보낼 것이다.")
    input()
    print("튜토리얼 : 너같은 녀석은 생명을 키울 자격이 없다.")
    input()
    print()
    print()
    print()
    print("END 1 : 무책임")
    input()

def end_2():
    os.system('cls')
    print("___________________________________________________________________________")
    print("                                Congratulations!.")
    print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
    print()
    print("　 　 　 　.__,,ｪェェｰェｪｪｭ")
    print("　 　 　 　 Ⅷ、ニ三≧ゞ彡!")
    print("　　　　　　lミ 　三三三彡|")
    print("　 　 　 　　lミ　三三三彡!")
    print("　　　　＿　}ミ 三三三彡{")
    print("　　　　弋圦　　　　　　　ｲ三ｦ")
    print("　　　　 　㌧ミ≡===≡ｱヲ'´")
    print("　　 　　　/　｀　・　.・i､")
    print("　　 　　彡,　　ミ(_,人_)彡ミ      '동전마술이다냐'")
    print("      ∩, /　ヽ､,　 　　ノ")
    print("      丶ニ|　　  '''-'´ﾉ")
    print("          ∪⌒∪''￣￣∪")
    print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
    print("튜토리얼 : 잘 키워냈구나")
    input()
    print("튜토리얼 : 음.. 그러니까.. '마술사'가 된거로군")
    input()
    print("튜토리얼 : 즐거워보여서 다행이야.")
    input()
    print("튜토리얼 : 여기까지 해내느라 수고많았다.")
    input()
    print()
    print()
    print("END 2-1 : 마술묘")
    input()

def end_3():
    os.system('cls')
    print("___________________________________________________________________________")
    print("                                Congratulations!.")
    print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
    print()
    print("　　　　 　 ,;r'''~￣^' ヽ,")
    print("　 　　　 ./　　　　　　 　)")
    print("　　　　　l　　∠ニニニニニニゝ")
    print("　　　　　l.∩.|　・　. ・ i､")
    print("　　 　　 ﾞl∪|　ミ(_,人_)彡ミ      '스트라이크냐'")
    print("      ∩, /　ヽ､,　 　　ノ")
    print("      丶ニ|　　  '''-'´ﾉ")
    print("          ∪⌒∪''￣￣∪")
    print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
    print("튜토리얼 : 잘 키워냈구나")
    input()
    print("튜토리얼 : 음.. 그러니까.. '야구선수'가 된거로군")
    input()
    print("튜토리얼 : 즐거워보여서 다행이야.")
    input()
    print("튜토리얼 : 여기까지 해내느라 수고많았다.")
    input()
    print()
    print()
    print("END 2-2 : 야구묘")
    input()

def end_4():
    os.system('cls')
    print("___________________________________________________________________________")
    print("                                Congratulations!.")
    print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
    print()
    print("　!　　　　　　　　　　　　　　　|　　　　　　　　　　　　i　　　　　　　　　!")
    print("　　　　　　　　　　　i　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　i")
    print("　　　　　　|　　　　　　　　　　　　　_　　　　　　!")
    print("　　　　　 　 　 　 　 　 　 　　|_|＿_　　　　　　　　　　　　　　　　　i")
    print("　　　　　　　　_　-‐ '' ¨,￣´　 !　｀ ､￣ ¨ ''‐- ､")
    print("　|　 　 　 _　´ 　 　 ／　　　　i　 　　＼　　 　 　｀ヽ、　　　　　　　　　|")
    print("　 　 　／　 　 　 , ' 　　 　 　 !　　 　 　ヽ　 　 　 　　＼")
    print("　　 , '　　 　　　/ 　 　 　 　　!　　　 　　　' , 　　　　　　ヽ　　!")
    print("　 /　 　 　 　 /　　　 　　　　l　　　　 　　 　 ,　　 _　-─-）")
    print("　', 　 ＿　　 ,'　 _　-─- ､、 |　_,,　- ─ -　､ ,ｒ''　　　　　　　　　　　")
    print("（''´　　 ｀ヽｒ''´　　　　　Ｙ !")
    print("　　　　　　　　　　　　　　　　| |")
    print("　　　　　　　　　　　　　　　　| |")
    print("　　　　　　 ,/ﾞﾐヽ､,,_,,／ﾞヽ  | |")
    print("  　　　 　　 i ノ　　川 　｀ヽ | |")
    print("　　　 　　　/  ｀  ・  . ・ i  | |")
    print("　　　 　　彡,　  ミ(_,人_)彡.  | |　　　'우산 같이 쓸까뇨'")
    print("　　 ∩,　/　ヽ､,　　 　　　ノ..| |")
    print("　　 丶ニ|　　 '"''" 　    ´  つ")
    print("　　　　　∪⌒∪'￣￣  ''￣'    ヽ`ｰ' 7")
    print("                                  ￣")
    print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
    print("튜토리얼 : 잘 키워냈구나")
    input()
    print("튜토리얼 : 음.. 그러니까.. '배우'가 된거로군")
    input()
    print("튜토리얼 : 즐거워보여서 다행이야.")
    input()
    print("튜토리얼 : 여기까지 해내느라 수고많았다.")
    input()
    print()
    print()
    print("END 2-3 : 배우묘")
    input()

os.system('cls')
cat1()
print("??? : zzz...")
input("대화를 진행하려면 엔터를 눌러주세요")
os.system('cls')
cat2()
print("??? : .....으응..?")
input()
os.system('cls')
cat3()
print("??? : 이런 깜빡 잠들었었네.")
input()
os.system('cls')
cat3()
print("튜토리얼 : 안녕. 내 이름은 튜토리얼")
player_name = input("네 이름은? : ")
print("튜토리얼 : 흐음..좋아 [",player_name,"]")
input()
os.system('cls')
cat3()
print("튜토리얼 : 자, 이제 이 게임에 대해 설명해주도록하지")
input()
os.system('cls')
egg1()
print("튜토리얼 : 이게 너가 키울 녀석이다.")
print("튜토리얼 : 이름을 정해주는게 좋겠군")
pet_name = input("이름을 지어주세요 : ")
os.system('cls')
egg2()
print("튜토리얼 : 좋아 그럼 이렇게 너와 펫 이름을 보여주지")
print("튜토리얼 : 그 아래는 너의 펫에 대한 정보를 보여준다.")
input()
os.system('cls')
egg2()
print("튜토리얼 : 아직 모든 수치가 0 이지? 차근차근 올려서 잘 성장하게 도와주는거다.")
input()
os.system('cls')
egg()
print("튜토리얼 : 자 아래에 보이는 것이 너가 저 아이를 위해 해줄 수 있는 행동들이다.")
print("튜토리얼 : 행동들을 잘 활용해서 훌륭히 키워내는 것이 이 게임의 목표다.")
input()
os.system('cls')
egg()
print("튜토리얼 : '포만'은 배부른 정도다. 0이 되면 안된다.")
print("튜토리얼 : '갈증'은 목마른 정도다. 100이 되면 안된다.")
print("튜토리얼 : '행복'은 행복한 정도다. 0이 되면 안된다.")
print("튜토리얼 : '체력'은 건강의 정도다. 0이 되면 안된다.")
print("튜토리얼 : '피로'는 피곤한 정도다. 100이 되면 안된다.")
print("튜토리얼 : '청결'은 깨끗한 정도다. 0이 되면 안된다.")
input()
os.system('cls')
egg()
print("튜토리얼 : 아, 책은 3가지 종류를 가져다두었다.")
print("튜토리얼 : 어떤 책을 듣고 자라냐에 따라 다른 모습이 나올 수 있을거다.")
print("튜토리얼 : 또한 행동들은 하루에 3번씩만 할 수 있다. 너도 피곤하지 않겠어?")
input()
os.system('cls')
cat3()
print("튜토리얼 : 자 여기까지가 내가 알려주는 과정이다.")
print("튜토리얼 : 만약 너가 굶기거나 피곤해 죽게 만들면..")
input()
os.system('cls')
cat4()
print("튜토리얼 : ...너한테서 그 아이를 빼앗아 다른 주인을 찾아줄거다.")
input()
os.system('cls')
cat3()
print("튜토리얼 : 생명은 소중한거니까 제대로 키우도록")
print("튜토리얼 : 난 이만 돌아가도록하지. 잘 키워내라")
input()
os.system('cls')
egg()
print("튜토리얼이 끝났습니다. 지금부터는 행동을 골라서 ",pet_name,"을(를) 잘 키워내봅시다.")
input()

while(day<4):
    os.system('cls')
    egg()
    num = int(input("무엇을 하시겠습니까 >> "))
    if num ==1:
        if act_1 ==3:
            print("이 행동은 오늘 더이상 할 수 없다.")
            input()
            continue
        print("사랑을 담아 진심으로 ",pet_name,"을(를) 쓰다듬었다.")
        print(pet_name,"의 행복도가 5 증가하였다.")
        happy=happy+5
        act_1+=1
        print("현재 행복도 : ",happy)
        input()
        continue
    if num ==6:
        print("잠을 잡니다. 모두의 피로도가 회복됩니다.")
        day +=1
        act_clear()
        input()
        continue
    else :
        print("아직 부화하기 전이라 할 수 없는 행동이다.")
        input()
os.system('cls')
hunger = 50
thirst = 50
well = 30
tired = 10
health = 80
baby()
print(pet_name,"이(가) 부화했다!")
input()
start = 0
if (happy == 0):
    start +=1
    os.system('cls')
    cat4()
    print("튜토리얼 : 너.. 알을 한번도 사랑해주지 않았군..")
    input()
    print("튜토리얼 : 너같은 녀석에게 더 맡겨봤자 의미가 없을거 같군그래")
    input()
    print("튜토리얼 : 썩 사라져라")
    input()
    print()
    print()
    print("END 0 : 시작도 못한")
if start == 0:
    while (True):
        if book_1 >= 100 :
            end_2()
            break
        if book_2 >= 100:
            end_3()
            break
        if book_3 >= 100:
            end_4()
            break

        if hunger <=0 or happy <= 0 or thirst >= 100 or well <= 0 or tired >= 100 or health <= 0:
            end1()
            os.system('cls')
            break
        os.system('cls')
        baby()
        num = int(input("무엇을 하시겠습니까 >> "))
        if num == 1:
            if act_1 == 3:
                print("이 행동은 오늘 더이상 할 수 없다.")
                input()
                continue
            os.system('cls')
            print()
            print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
            print()
            print("　　　　　　,/ﾞﾐ∩　__,,／ﾞヽ 　∩")
            print("　　 　　　i ノ(⌒ )川　｀ヽ'  ()E）")
            print("　　 　　　/　/ /  ・   .・  i/ /")
            print("　　 　　彡, / /   ミ(_,人_)彡 /")
            print("　　　 　/　/ / 　　 　　 ノ  /")
            print("　　　　　　　　 ''''''''''")
            print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
            print("사랑을 담아 진심으로 ", pet_name, "을(를) 쓰다듬었다.")
            print(pet_name, "의 행복도가 5 증가하였다.")
            happy = happy + 5
            act_1 += 1
            input()
            continue
        if num == 2:
            if act_2 == 3:
                print("이 행동은 오늘 더이상 할 수 없다.")
                input()
                continue
            print("1. 음식 2. 물")
            food = int(input("어떤 것을 줄까? : "))
            if food == 1:
                if hunger >= 100:
                    print("이미 충분히 배가 부르다.")
                    input()
                    continue
                os.system('cls')
                print()
                print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
                print()
                print("　　　　　　/ﾞﾐヽ､,__,,／ﾞヽ")
                print("　　 　　　i ノ　　 川   )")
                print("　　 　　  /　｀  ・  .・i､")
                print("　　 　　彡,　  ミ(_,人_)彡ミ")
                print("　  ∩,  / ヽ､,　 l　　 ⊃　⌒_つ")
                print("　  丶ニ|　 '"'''  ---ヽｰ------ﾉ""''')
                print("　　　　∪⌒∪''￣￣∪")
                print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
                print("생선 하나를 구워서 살을 발라줬다. 맛있게 먹는다.")
                print(pet_name, "의 포만도가 30 증가하였다.")
                print(pet_name, "의 목마름이 10 증가하였다.")
                hunger = hunger + 30
                thirst = thirst + 10
                act_2 += 1
                input()
                continue
            if food == 2:
                if thirst <= 20:
                    print("지금은 목 마르지 않다.")
                    input()
                    continue
                os.system('cls')
                print()
                print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
                print()
                print("　　　　　　/ﾞﾐヽ､,__,,／ﾞヽ")
                print("　　 　　　i ノ　　 川   )")
                print("　　 　　  /　｀  ・  .・i､")
                print("　　 　　彡,　  ミ(_,人_)彡ミ")
                print("　  ∩,  / ヽ､,　  　∪ノ")
                print("　  丶ニ|　 '-''''-''''  ")
                print("　　　　∪⌒∪''￣￣∪")
                print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
                print("물을 떠다주었다. 물을 마시고 있다.")
                print(pet_name, "의 목마름이 20 감소하였다.")
                thirst = thirst - 20
                act_2 += 1
                input()
                continue
        if num == 3:
            if act_3 == 3:
                print("이 행동은 오늘 더이상 할 수 없다.")
                input()
                continue
            os.system('cls')
            print()
            print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
            print()
            print("　　　　　　　   ∧∧　　　　　　　　　　  っ")
            print("　　　　　　　 （・・)　　　　　　　　    ((´")
            print("　　　　　　  ) ノ　|　　　 　     ∧∧⌒ヽ))")
            print("　　　　　　 ( ( ),j,j　　　　    (- -）（  )")
            print("[￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣]")
            print("　][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][")
            print("[￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣]")
            print("　][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][")
            print("[￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣]")
            print("　][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][")
            print("[￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣][￣]")
            print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
            print("즐겁게 산책을 다녀왔다.")
            input()
            print(pet_name, "의 체력이 15 증가하였다.")
            print(pet_name, "의 행복도가 5 증가하였다.")
            print(pet_name, "의 포만도가 15 감소하였다.")
            print(pet_name, "의 목마름이 10 증가하였다.")
            print(pet_name, "의 피로도가 15 증가하였다.")
            print(pet_name, "의 청결도가 15 감소하였다.")
            hunger = hunger - 15
            thirst = thirst + 10
            well = well + 15
            happy = happy + 5
            tired = tired + 15
            health = health - 15
            act_3 += 1
            input()
            continue
        if num == 4:
            if act_4 == 3:
                print("이 행동은 오늘 더이상 할 수 없다.")
                input()
                continue
            os.system('cls')
            print()
            print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
            print()
            print("（　）")
            print("　　（ ）　　　（　）")
            print("")
            print("　　 ,/ﾞﾐヽ､,,___/ﾞヽ")
            print("　 　i ノ　　 川 ｀ヽ")
            print("　　　/ ｀ ・  . ・ i")
            print("　　彡,   ミ(_,人_)彡ミ")
            print("　　　ヽ､,　　 　 ノ")
            print("　|￣￣￣Ｕ￣￣￣Ｕ￣|")
            print("（====================）")
            print("　＼＿＿＿＿＿＿＿__／")
            print("　　从从从从从从从从")
            print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
            print("따뜻한 물에 샤워를 한다. 따뜻해서 좋긴하지만 물을 싫어하는지 조금 짜증을 낸다.")
            print(pet_name, "의 청결도가 20 증가하였다.")
            print(pet_name, "의 피로도가 5 증가하였다.")
            print(pet_name, "의 행복도가 5 감소하였다.")
            health = health + 20
            tired = tired + 5
            happy = happy - 5
            act_4 += 1
            input()
            continue

        if num == 5:
            if act_5 == 3:
                print("이 행동은 오늘 더이상 할 수 없다.")
                input()
                continue
            print("1. 고양이 동전 마술")
            print("2. 털뭉치로 야구하는 법")
            print("3. 고양이 표정연기 비법")
            book=int(input("어떤 책을 읽어 줄까 : "))
            os.system('cls')
            print()
            print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
            print()
            print("　　 　　 /ﾞﾐヽ､,,___,,／ﾞヽ")
            print("　　 　 　i ノ　 　 川 ｀ヽ'")
            print("　 　　　/　　　　　　　　l")
            print("　∩　彡,　 　 ・　 ． ・　iミ")
            print("　 ヾ〆　ヽ､, ミ(_,人_)彡｀")
            print("⊂二、___　'''つ''''''"",,,つ")
            print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
            print(pet_name,"은(는) 누워서 읽어주는 책을 듣습니다.")
            if book == 1:
                book_1 = book_1 + 10
                print(pet_name,"은(는) 마술에 흥미도가 올라갔습니다.")
            if book == 2:
                book_2 = book_2 + 10
                print(pet_name, "은(는) 야구에 흥미도가 올라갔습니다.")
            if book == 3:
                book_3 = book_3 + 10
                print(pet_name, "은(는) 연기에 흥미도가 올라갔습니다.")
            act_5 +=1
            print(pet_name, "의 체력이 5 감소하였다.")
            print(pet_name, "의 피로도가 10 증가하였다.")
            well = well - 5
            tired = tired + 10
            input()
            continue

        if num == 6:
            os.system('cls')
            print()
            print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
            print()
            print("　　 　　 /ﾞﾐヽ､,,___,,／ﾞヽ")
            print("　　 　 　i ノ　 　 川 ｀ヽ'")
            print("　 　　　/　　　　　　　　l")
            print("　∩　彡,　 　  -　 ． -　iミ")
            print("　 ヾ〆　ヽ､, ミ(_,人_)彡｀")
            print("⊂二、___　'''つ''''''"",,,つ")
            print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
            print("잠을 잡니다. 모두의 피로도가 회복됩니다.")
            print("자고 일어나면 배가 조금 고파집니다.")
            tired = tired - 50
            hunger = hunger - 30
            day += 1
            act_clear()
            input()
            continue
