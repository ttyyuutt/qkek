import tkinter as tk
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import schedule
import time
import os
import platform

if(platform.system() == "Windows"):
    from winotify import Notification
else:
    pass

window = tk.Tk()
window.title("공지사항 알림")
window.geometry("700x400+400+300")
window.resizable(True, True)

url = "https://www.smu.ac.kr/lounge/notice/notice.do?srCampus=smuc"
title_list = []
driver = webdriver.Chrome(ChromeDriverManager().install())
cycle_input = 0
post_check = 0
cnt_log = 0
new_post = 0

label1 = tk.Label(window, text="상명대학교 공지사항", font=('Monaco', 23))
label1.grid(row=1, column=1)


def macNotification(message,title=None,subtitle=None,soundname=None):

	titlePart = ''
	if(not title is None):
		titlePart = 'with title "{0}"'.format(title)
	subtitlePart = ''
	if(not subtitle is None):
		subtitlePart = 'subtitle "{0}"'.format(subtitle)
	soundnamePart = ''
	if(not soundname is None):
		soundnamePart = 'sound name "{0}"'.format(soundname)

	appleScriptNotification = 'display notification "{0}" {1} {2} {3}'.format(message,titlePart,subtitlePart,soundnamePart)
	os.system("osascript -e '{0}'".format(appleScriptNotification))


def title_update():
    global title_list
    time.sleep(1)
    listbox = tk.Listbox(window, selectmode='extended', width=20, height=0, relief="solid", font=('Monaco', 20))
    for i in range(1, 11, 1):
        title = driver.find_element(By.XPATH, '//*[@id="ko"]/div[4]/ul/li[%d]/dl/dt/table/tbody/tr/td[3]/a' % (i))
        title_list.append(title.text)
        # print(title_list[i-1])
        listbox.insert(i, title_list[i-1])
    if(platform.system() == "Windows"):
        toast1 = Notification(app_id="Notice", title = "첫 실행입니다!" if new_post == 0 else str(new_post) + "개의 새로운 알람입니다!" , msg=title_list[0], icon=r"c:\path\to\icon.png")
        toast1.show()
    elif(platform.system() == "Darwin"):
        if __name__ == '__main__':
            macNotification(title_list[0], "새로운 공지가 있습니다.")
    else:
        pass
    listbox.place(x=25, y=80, width=650)


def cnt_update():
    global cnt_log
    global new_post
    driver.get(url)
    time.sleep(3)
    cnt_str = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[4]/div[1]/div/div/div[3]/span[1]')
    cnt_str = str(cnt_str.text)
    cnt = int(cnt_str)
    if cnt > cnt_log:
        if cnt_log == 0:
            if(platform.system() == "Windows"):
                toast1 = Notification(app_id="Notice",
                        title="프로그램을 시작합니다.",
                        msg="4시간마다 업데이트를 확인합니다.!",
                        icon=r"c:\path\to\icon.png")
                toast1.show()
            elif(platform.system() == "Darwin"):
                macNotification("4시간마다 업데이트를 확인합니다.!", "프로그램을 시작합니다.")
            else:
                pass
        else:
            if  cnt_log != 0:
                new_post = cnt - cnt_log
            else:
                new_post = 0
        cnt_log = cnt
        title_update()
    else:
        message = tk.Message(window, text="새로운 공지가 없습니다.", width=550, relief="solid", font=('Monaco', 20))
        message.place(x=25, y=80)
        if(platform.system() == "Windows"):
            toast1 = Notification(app_id="Notice",
                    title="새로운 공지사항이 없습니다!",
                    msg="4시간마다 업데이트를 확인합니다.!",
                    icon=r"c:\path\to\icon.png")
            toast1.show()
            #toaster.show_toast("새로운 공지사항이 없습니다.", "4시간마다 새로운 공지사항을 확인합니다.", duration=10)
        elif(platform.system() == "Darwin"):
            macNotification("4시간마다 업데이트를 확인합니다.!", "새로운 공지사항이 없습니다!")
        else:
            pass
    window.grid_rowconfigure(0, minsize=20)
    window.grid_columnconfigure(0, minsize=30)
    window.mainloop()

cnt_update()
schedule.every(4).hours.do(cnt_update)

while True:
    schedule.run_pending()
    time.sleep(1)
