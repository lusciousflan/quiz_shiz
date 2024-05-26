#coding:utf-8

import tkinter as tk
import tkinter.messagebox as mess

def Timer():
    global countdown, timering
    timering = 0
    countdown = countdown - 1
    if(countdown == 0):
        can1.lift(timer_images[countdown])
        timering = 1
        countdown = 6
        mess.showinfo("無題","時間切れです")
        can1.lift(timer_images[5])
    if(timering == 0):
        can1.lift(timer_images[countdown])
        f1.after(1000, Timer)

def forward_(num):
    global masu, team_masu, can1
    for i in range(1,13):
        if(team_masu[num]+i >= 13):
            can1.delete(komaimage[num])
            can1.create_image(komax[num], komay[num], image = clear_, anchor = tk.NW)
            masu[team_masu[num]] = 0
            break
        if(masu[team_masu[num]+i] == 0):
            masu[team_masu[num]] = 0
            masu[team_masu[num]+i] = num+1
            team_masu[num] += i
            can1.moveto(komaimage[num], masux[team_masu[num]-1], masuy[team_masu[num]-1])
            break

def back_(num):
    global masu, team_masu, can1
    for i in range(1,13):
        if(team_masu[num]-i <= 0):
            masu[team_masu[num]] = 0
            team_masu[num] = 0
            can1.moveto(komaimage[num], komax[num], komay[num])
            break
        if(masu[team_masu[num]-i] == 0):
            masu[team_masu[num]] = 0
            masu[team_masu[num]-i] = num+1
            team_masu[num] -= i
            can1.moveto(komaimage[num], masux[team_masu[num]-1], masuy[team_masu[num]-1])
            break

def bm1_c():
    back_(0)

def bp1_c():
    forward_(0)
    
def bm2_c():
    back_(1)

def bp2_c():
    forward_(1)

def bm3_c():
    back_(2)

def bp3_c():
    forward_(2)

def bm4_c():
    back_(3)

def bp4_c():
    forward_(3)

def bm5_c():
    back_(4)

def bp5_c():
    forward_(4)

def bm6_c():
    back_(5)

def bp6_c():
    forward_(5)

def bm7_c():
    back_(6)

def bp7_c():
    forward_(6)

def bm8_c():
    back_(7)

def bp8_c():
    forward_(7)
    
def qzst():
    #startボタンを押したときの処理
    #クイズの中身の処理はこっちと思ったけど書くことなさそう
    global colors
    f2.pack_forget()
    f1.pack(
        fill=tk.BOTH,
        expand=True
        )
    subroot = tk.Toplevel()
    subroot.geometry("300x600")
    winw2 = 300
    winh2 = 600
    can2 = tk.Canvas(
        subroot,
        )
    can2.pack(
        expand=True,
        fill=tk.BOTH,
        )
    
    #マス移動用のボタン
    bm = []
    bp = []
    bm.append(tk.Button(
        subroot,
        text="-",
        command=bm1_c
        ))
    bp.append(tk.Button(
        subroot,
        text="+",
        command=bp1_c
        ))
    bm.append(tk.Button(
        subroot,
        text="-",
        command=bm2_c
        ))
    bp.append(tk.Button(
        subroot,
        text="+",
        command=bp2_c
        ))
    bm.append(tk.Button(
        subroot,
        text="-",
        command=bm3_c
        ))
    bp.append(tk.Button(
        subroot,
        text="+",
        command=bp3_c
        ))
    bm.append(tk.Button(
        subroot,
        text="-",
        command=bm4_c
        ))
    bp.append(tk.Button(
        subroot,
        text="+",
        command=bp4_c
        ))
    bm.append(tk.Button(
        subroot,
        text="-",
        command=bm5_c
        ))
    bp.append(tk.Button(
        subroot,
        text="+",
        command=bp5_c
        ))
    bm.append(tk.Button(
        subroot,
        text="-",
        command=bm6_c
        ))
    bp.append(tk.Button(
        subroot,
        text="+",
        command=bp6_c
        ))
    bm.append(tk.Button(
        subroot,
        text="-",
        command=bm7_c
        ))
    bp.append(tk.Button(
        subroot,
        text="+",
        command=bp7_c
        ))
    bm.append(tk.Button(
        subroot,
        text="-",
        command=bm8_c
        ))
    bp.append(tk.Button(
        subroot,
        text="+",
        command=bp8_c
        ))
    #ボタン配置
    for i in range(8):
        bm[i].place(
            relx = 0,
            rely = 0.1*i,
            relwidth = 0.4,
            relheight = 0.1
            )
        bp[i].place(
            relx = 0.6,
            rely = 0.1*i,
            relwidth = 0.4,
            relheight = 0.1
            )
    for i in range(8):
        can2.create_rectangle(
            winw2*0.4, winh2*(0.1*i), winw2*0.6, winh2*(0.1*i+0.1),
            fill=colors[i]
            )
    #タイマー
    timer_button = tk.Button(
        subroot,
        text = "timer",
        command = Timer
        )
    timer_button.place(
        relx = 0,
        rely = 0.9,
        relwidth = 0.5,
        relheight = 0.1
        )
    

if(__name__ == '__main__'):
    root = tk.Tk()

    root.title("運命の13階段!!　～高きを仰げ静高生～")
    root.geometry("1300x700+0+0")

    winw = root.winfo_screenwidth()
    winh = root.winfo_screenheight()

    #画像読み込み
    bgimage = tk.PhotoImage(file="bgimage4.png")
    clear_ = tk.PhotoImage(file="clear3.png")
    team_image = []
    team_image.append(tk.PhotoImage(file="team1.png"))
    team_image.append(tk.PhotoImage(file="team2.png"))
    team_image.append(tk.PhotoImage(file="team3.png"))
    team_image.append(tk.PhotoImage(file="team4.png"))
    team_image.append(tk.PhotoImage(file="team5.png"))
    team_image.append(tk.PhotoImage(file="team6.png"))
    team_image.append(tk.PhotoImage(file="team7.png"))
    team_image.append(tk.PhotoImage(file="team8.png"))
    timer_image = []
    timer_image.append(tk.PhotoImage(file="timer0.png"))
    timer_image.append(tk.PhotoImage(file="timer1.png"))
    timer_image.append(tk.PhotoImage(file="timer2.png"))
    timer_image.append(tk.PhotoImage(file="timer3.png"))
    timer_image.append(tk.PhotoImage(file="timer4.png"))
    timer_image.append(tk.PhotoImage(file="timer5.png"))

    #クイズ本体のほう
    #ビジュアルはこっちに書く
    f1 = tk.Frame(
        root,
        )
        
    #8色のカラーコードを定数にして保存
    colors = ["#FFE47C","#FDDDEF","#E57FFF","#1CCAA6","#C21614","#FD7B0D","#0068B7","#257321"]
    #can1:Canvas。これの上に全部表示する。
    can1 = tk.Canvas(
        f1,
        )
    can1.pack(
        expand=True,
        fill=tk.BOTH,
        )
    can1.create_image(0, 0, image = bgimage, anchor = tk.NW)

    #各チームの駒のスタート位置
    komax = []
    komay = []
    for i in range(4):
        komax.append(50)
        komay.append(105*i+50)
    for i in range(4):
        komax.append(155)
        komay.append(50+105*i)
    #各駒のimage
    komaimage = []
    for i in range(8):
        komaimage.append(can1.create_image(komax[i], komay[i], image = team_image[i], anchor = tk.NW))
    #masu:マスが埋まっているかをチーム番号で保存、初期は全部0
    masu = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #team_masu:各チームがどこのマスにいるか保存、スタートが0、ゴールが13
    team_masu = [0, 0, 0, 0, 0, 0, 0, 0]
    #各マスの座標
    masux = []
    masuy = []
    for i in range(7):
        masux.append(355+105*i)
        masuy.append(122.5)
    for i in range(5):
        masux.append(510+105*i)
        masuy.append(382.5)

    #タイマー
    countdown = 6
    timering = 1
    timer_images = []
    for i in range(6):
        timer_images.append(can1.create_image(105, 485, image = timer_image[i], anchor = tk.NW))

    #スタート画面
    f2 = tk.Frame(
        root,
        bg = "#FFE47C",
        )
    f2.pack(
        fill=tk.BOTH,
        expand=True
        )
    Title = tk.Label(
        f2,
        text = "運命の13階段!!　～高きを仰げ静高生～",
        font=(20),
        )
    Title.pack(
        expand=True
        )
    txtbx = tk.Entry(
        f2,
        width=14
        )
    txtbx.pack(
        expand=True
        )
    stButton = tk.Button(
        f2,
        text = "Start",
        command = qzst
        )
    stButton.pack(
        expand=True
        )
    maker = tk.Label(
        f2,
        text="作った人:甘糖ぷりん",
        font=(30)
        )
    maker.pack(
        anchor=tk.SE
        )

    
    root.mainloop()

