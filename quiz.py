#coding:utf-8

import tkinter as tk

def forward_(num):
    print("Hey!")
    global masu, team_masu
    for i in range(1,13):
        if(masu[team_masu[num]+i] == 0):
            masu[team_masu[num]] = 0
            masu[team_masu[num]+i] = num+1
            team_masu[num] += i
            break
    print(masu)
    print(team_masu)

def back_(num):
    print("Hey!!")
    global masu, team_masu
    for i in range(1,13):
        if(masu[team_masu[num]-i] == 0):
            masu[team_masu[num]] = 0
            masu[team_masu[num]-i] = num+1
            team_masu[num] -= i
            break
    print(masu)
    print(team_masu)

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
    forward(5)

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
    f2.pack_forget()
    f1.pack(
        fill=tk.BOTH,
        expand=True
        )
    

if(__name__ == '__main__'):
    root = tk.Tk()

    root.title("運命の13階段!!　～高きを仰げ静高生～")
    root.attributes("-fullscreen", True)
    #root.geometry("1380x680")

    winw = root.winfo_screenwidth()
    winh = root.winfo_screenheight()
    #print(winw)
    #print(winh)

    #クイズ本体のほう
    #ビジュアルはこっちに書く
    f1 = tk.Frame(
        root,
        #bg = "#FFE47C"
        )
    """
    testLabel = tk.Label(
        f1,
        text = "Test",
        )
    testLabel.pack(
        expand=True
        )
        """
        
    #8色のカラーコードを定数にして保存
    colors = ["#FFE47C","#FDDDEF","#E57FFF","#1CCAA6","#C21614","#FD7B0D","#0068B7","#257321"]
    #can1:Canvas。これの上に全部表示する。
    can1 = tk.Canvas(
        f1,
        #bg = "#FFE47C",
        #bg = "white",
        )
    can1.pack(
        expand=True,
        fill=tk.BOTH,
        )
    #startの箱
    for i in range(4):
        can1.create_rectangle(
            winw*0.05, winh*(0.125*i+0.125), winw*0.125, winh*(0.125*i+0.25),
            )
        can1.create_rectangle(
            winw*0.125, winh*(0.125*i+0.125), winw*0.2, winh*(0.125*i+0.25),
            )
    #マス目
    for i in range(7):
        can1.create_rectangle(
            winw*(0.05*i+0.25), winh*0.125, winw*(0.05*i+0.3), winh*0.35,
            )
    for i in range(6):
        can1.create_rectangle(
            winw*(0.05*i+0.35), winh*0.4, winw*(0.05*i+0.4), winh*0.625,
            )
    #勝ち抜けの箱
    for i in range(4):
        can1.create_rectangle(
            winw*0.7, winh*(0.125*i+0.125), winw*0.775, winh*(0.125*i+0.25),
            )
    #ボタンのところの色
    for i in range(8):
        can1.create_rectangle(
            winw*0.875, winh*(0.1*i+0.05), winw*0.925, winh*(0.1*i+0.1),
            fill=colors[i]
            )
    #線
    can1.create_line(winw*0.8, 0, winw*0.8, winh)
    #各チームの駒
    komax = []
    komay = []
    #マス移動用のボタン
    bm1 = tk.Button(
        f1,
        text="-",
        command=bm1_c
        )
    bp1 = tk.Button(
        f1,
        text="+",
        command=bp1_c
        )
    bm2 = tk.Button(
        f1,
        text="-",
        command=bm2_c
        )
    bp2 = tk.Button(
        f1,
        text="+",
        command=bp2_c
        )
    bm3 = tk.Button(
        f1,
        text="-",
        command=bm3_c
        )
    bp3 = tk.Button(
        f1,
        text="+",
        command=bp3_c
        )
    bm4 = tk.Button(
        f1,
        text="-",
        command=bm4_c
        )
    bp4 = tk.Button(
        f1,
        text="+",
        command=bp4_c
        )
    bm5 = tk.Button(
        f1,
        text="-",
        command=bm5_c
        )
    bp5 = tk.Button(
        f1,
        text="+",
        command=bp5_c
        )
    bm6 = tk.Button(
        f1,
        text="-",
        command=bm6_c
        )
    bp6 = tk.Button(
        f1,
        text="+",
        command=bp6_c
        )
    bm7 = tk.Button(
        f1,
        text="-",
        command=bm7_c
        )
    bp7 = tk.Button(
        f1,
        text="+",
        command=bp7_c
        )
    bm8 = tk.Button(
        f1,
        text="-",
        command=bm8_c
        )
    bp8 = tk.Button(
        f1,
        text="+",
        command=bp8_c
        )
    #ボタン配置
    bm1.place(
        relx = 0.825,
        rely = 0.05,
        relwidth = 0.025,
        relheight = 0.05
        )
    bp1.place(
        relx = 0.95,
        rely = 0.05,
        relwidth = 0.025,
        relheight = 0.05
        )
    bm2.place(
        relx = 0.825,
        rely = 0.15,
        relwidth = 0.025,
        relheight = 0.05
        )
    bp2.place(
        relx = 0.95,
        rely = 0.15,
        relwidth = 0.025,
        relheight = 0.05
        )
    bm3.place(
        relx = 0.825,
        rely = 0.25,
        relwidth = 0.025,
        relheight = 0.05
        )
    bp3.place(
        relx = 0.95,
        rely = 0.25,
        relwidth = 0.025,
        relheight = 0.05
        )
    bm4.place(
        relx = 0.825,
        rely = 0.35,
        relwidth = 0.025,
        relheight = 0.05
        )
    bp4.place(
        relx = 0.95,
        rely = 0.35,
        relwidth = 0.025,
        relheight = 0.05
        )
    bm5.place(
        relx = 0.825,
        rely = 0.45,
        relwidth = 0.025,
        relheight = 0.05
        )
    bp5.place(
        relx = 0.95,
        rely = 0.45,
        relwidth = 0.025,
        relheight = 0.05
        )
    bm6.place(
        relx = 0.825,
        rely = 0.55,
        relwidth = 0.025,
        relheight = 0.05
        )
    bp6.place(
        relx = 0.95,
        rely = 0.55,
        relwidth = 0.025,
        relheight = 0.05
        )
    bm7.place(
        relx = 0.825,
        rely = 0.65,
        relwidth = 0.025,
        relheight = 0.05
        )
    bp7.place(
        relx = 0.95,
        rely = 0.65,
        relwidth = 0.025,
        relheight = 0.05
        )
    bm8.place(
        relx = 0.825,
        rely = 0.75,
        relwidth = 0.025,
        relheight = 0.05
        )
    bp8.place(
        relx = 0.95,
        rely = 0.75,
        relwidth = 0.025,
        relheight = 0.05
        )
    #masu:マスが埋まっているかをチーム番号で保存、初期は全部0
    masu = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #team_masu:各チームがどこのマスにいるか保存、スタートが0、ゴールが13
    team_masu = [0, 0, 0, 0, 0, 0, 0, 0]

    #スタート画面
    f2 = tk.Frame(
        root,
        bg = "#FFE47C",
        #width = 1000,
        #height = 1000,
        )
    #f2.place(x = 0, y = 0)
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

    
    root.mainloop()

