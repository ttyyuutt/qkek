import random
import turtle as t      # te = 경찰 거북이
          # ts = 먹이 거북이
                             # t  = 플레이어
score = 0 
heart = 3 # 목숨 3개    
playing = False  # playing 함수를 적용시키기 전

te = t.Turtle()    
te.shape("turtle")  # 경찰 거북이의 외형 
te.color("blue")
te.speed(0)
te.up()
te.goto(0, 200)   # 경찰 거북이의 스폰 위치

ts = t.Turtle()      
ts.shape("circle")  # 먹이 외형
ts.color("green")   
ts.speed(0)
ts.up()
ts.goto(0, -200)  # 먹이 스폰 위치

t_1 = t.Turtle()
t_1.color("red") 
t_1.shape("turtle")
t_1.up()
t_1.speed(0)
t_1.goto(235, 235)
t_1.setheading(90)

t_2 = t.Turtle()
t_2.color("red")
t_2.shape("turtle")
t_2.up()
t_2.speed(0)
t_2.goto(210, 235)
t_2.setheading(90)

t_3 = t.Turtle()
t_3.color("red")
t_3.shape("turtle")
t_3.up()
t_3.speed(0)
t_3.goto(185, 235)
t_3.setheading(90)

def turn_right():                
    t.setheading(0)   # 플레이어를 오른쪽으로 가게 하는 함수

def turn_up():                   
    t.setheading(90)   # 플레이어를 위로 가게 하는 함수
                       
def turn_left():                 
    t.setheading(180)  # 플레이어를 왼쪽으로 가게 하는 함수

def turn_down():                
    t.setheading(270)   # 플레이어를 아래로 가게 하는 함수

def start():    # 사람이 실제로 조종할 수 있게 하는 함수              
    global playing
    if playing == False:    
        playing = True
        t.clear()      #처음으로 돌아가게 함          
        play()

def play():                    
    global score  # 점수 함수 적용
    global playing  # 사람이 조종 가능하게 함
    global heart
    t.forward(10)   
    
    if t.xcor() > 235:     # 벽에 부딪히면 반대 방향으로 이동함 
        t.right(180)
    if t.xcor() < -235:
        t.right(180)
    if t.ycor() < -235:  
        t.right(180) 
    if t.ycor() > 235: 
        t.right(180)
    
    if heart == 2:
        t_3.color("grey")
    if heart == 1:
        t_2.color("grey")   
    
    if random.randint(1, 5) == 3:        
        ang = te.towards(t.pos())  # 경찰 거북이가 내 거북이를 쳐다보게 함
        te.setheading(ang)
    speed = score + 5   # 경찰 거북이의 속도는 내 점수가 올라가면 빨라짐
    if speed > 15:                     
        speed = 15
    te.forward(speed)  # 경찰 거북이 처음 속도 지정
    if t.distance(te) < 12: # '나'와 경찰 거북이의 거리가 12 픽셀 이하일때
        heart -= 1
        t.goto(-235,235) # 경찰 거북이랑 부딪히면 지정된 위치로 이동
        if heart == 0: 
            t_1.color("grey")      
            text = "점수 : " + str(score) # 점수 쓰기        
            message(text , '''다시 시작하려면 스페이스바를 누르세요''')  # 메세지 입력        
            playing = False # 사람이 조종 못 하게 하는 함수
            score = 0  # 다시 0점
            heart = 3
   
    if t.distance(ts) < 12:  # '나'와 먹이 거북이의 거리가 12 픽셀 이상일때
        score = score + 1   # 점수를 적고 1점씩 추가
        t.write(score)  # 내가 점수 얻은 자리에 "SCORE"라고 쓰기                        
        p_x = random.randint(-230, 230)  # p_x = 먹이 스폰 위치 범위 (x 축)
        p_y = random.randint(-230, 230)  # p_y = 함수 범위
        ts.goto(p_x, p_y) #위에서 지정한 함수 범위로 먹이 스폰 위치 지정
    
    if playing:
        t.ontimer(play, 100)  # 0.1초 후 play 함수 시작          

def message(m1, m2):  # 메세지 쓰게 함            
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))  # '시작하려면"을 적는 위치
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))  # "스페이스바를 누르세요"를 적는 위치
    t.home()

t.title("도둑잡기")
t.setup(500, 500)     # 게임 배경, 제목
t.bgcolor("grey")
t.shape("turtle")  
t.speed(0)          
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")   
t.onkeypress(turn_up, "Up")         # 방향키를 사용함
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")   
t.onkeypress(start, "space")


t.listen()  # 내 입력이 적용되게 하는 것      
message("도둑잡기", "시작하려면 스페이스바를 누르세요")

# input("press any key to exit ...")
