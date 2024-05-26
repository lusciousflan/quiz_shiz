#coding:utf-8

import tkinter as tk
import tkinter.messagebox as mess

#タイマーの中身
def Timer():
    #print("Hello")
    global countdown, timering
    #timering = 0
    countdown = countdown - 1
    #nowTime.set(str(countdown))
    if(countdown == 0):
        can1.lift(timer_images[countdown])
        timering = 1
        countdown = 6
        mess.showinfo("無題","時間切れです")
        #nowTime.set(str(countdown))
        can1.lift(timer_images[5]) 
    elif(timering == 1):
        countdown = 6
        can1.lift(timer_images[5])
    if(timering == 0):
        can1.lift(timer_images[countdown])
        f1.after(1000, Timer)

#タイマーのボタン押したときの処理
def Timer_st():
    global timering
    if(timering == 1):
        timering = 0
        Timer()
    else:
        timering = 1
        Timer()

def close():
    tojiru = mess.askyesno("閉じる", "ウィンドウを閉じますか？")
    if(tojiru == True):
        root.destroy()

#前進む処理
def forward_(num):
    #print("Hey!")
    global masu, team_masu, can1, goal
    for i in range(1,13):
        if(team_masu[num]+i == 13):
            can1.delete(komaimage[num])
            can1.create_image(komax[num], komay[num], image = clear_, anchor = tk.NW)
            masu[team_masu[num]] = 0
            mess.showinfo("ゴール！", team_name[num]+"さんおめでとうございます！")
            goal += 1
            team_masu[num] += i
            if(goal == 4):
                mess.showinfo("ゲーム終了", "終了！！")
                close()
            break
        if(masu[team_masu[num]+i] == 0):
            masu[team_masu[num]] = 0
            masu[team_masu[num]+i] = num+1
            team_masu[num] += i
            can1.moveto(komaimage[num], masux[team_masu[num]-1], masuy[team_masu[num]-1])
            break
    #print(masu)
    #print(team_masu)

#後ろ戻る処理
def back_(num):
    #print("Hey!!")
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
    #print(masu)
    #print(team_masu)

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
    #print(winw2)
    #print(winh2)
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
        command = Timer_st
        )
    timer_button.place(
        relx = 0,
        rely = 0.9,
        relwidth = 0.5,
        relheight = 0.1
        )
    for i in range(8):
        team_name[i] = txtbx[i].get()

    #閉じるボタン
    close_button = tk.Button(
        subroot,
        text = "close",
        command = close
        )
    close_button.place(
        relx = 0.5,
        rely = 0.9,
        relwidth = 0.5,
        relheight = 0.1
        )

#チーム名入力時にエンターで次のところにfocusする
def kaigyo(event):
    kariname = str(can3.focus_get())
    #print(kariname)
    #print(kariname[len(kariname)-1])
    cur = kariname[len(kariname)-1]
    if(str(cur) == "y"):
        cur = 1
    txtbx[int(cur)].focus_set()
    #txtbx[can3.focus_get()].focus_set()

"""
def pushed(e):
    global cursor
    #cursor = e
    print(e)
    if(598 <= e.x <= 700 and 246 <= e.y <= 423):
        for i in range(1,9):
            if((700-598)/8*i <= e.y <= (700-598)/8*(i+1)):
                txtbx[i-1].focus_set()
                cursor = i-1
                break
"""

if(__name__ == '__main__'):
    root = tk.Tk()

    root.title("運命の13階段!!　～高きを仰げ静高生～")
    #root.attributes("-fullscreen", True)
    root.geometry("1300x700+0+0")

    winw = root.winfo_screenwidth()
    winh = root.winfo_screenheight()
    #print(winw)
    #print(winh)

    #画像読み込み
    bgimage = tk.PhotoImage(file="bgimage4.png")
    st_bg = tk.PhotoImage(file="start_bg2.png")
    clear_ = tk.PhotoImage(file="clear3.png")
    team_image = []
    for i in range(1,9):
        team_image.append(tk.PhotoImage(file="team"+str(i)+".png"))
        """
    team_image.append(tk.PhotoImage(file="team2.png"))
    team_image.append(tk.PhotoImage(file="team3.png"))
    team_image.append(tk.PhotoImage(file="team4.png"))
    team_image.append(tk.PhotoImage(file="team5.png"))
    team_image.append(tk.PhotoImage(file="team6.png"))
    team_image.append(tk.PhotoImage(file="team7.png"))
    team_image.append(tk.PhotoImage(file="team8.png"))"""
    timer_image = []
    for i in range(6):
        timer_image.append(tk.PhotoImage(file="timer"+str(i)+".png"))
        """
    timer_image.append(tk.PhotoImage(file="timer1.png"))
    timer_image.append(tk.PhotoImage(file="timer2.png"))
    timer_image.append(tk.PhotoImage(file="timer3.png"))
    timer_image.append(tk.PhotoImage(file="timer4.png"))
    timer_image.append(tk.PhotoImage(file="timer5.png"))"""

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
    #colors = ["#FFE47C","#07005C","#E57FFF","#1CCAA6","#C21614","#FD7B0D","#0068B7","#257321"]
    colors = ["red", "deeppink", "purple", "blue", "aqua", "forestgreen", "greenyellow", "yellow"]
    # #07005C #FD7B0D #257321 #FDDDEF #C21614
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
    can1.create_image(0, 0, image = bgimage, anchor = tk.NW)
    """
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
            winw*0.825, winh*(0.1*i+0.05), winw*0.85, winh*(0.1*i+0.1),
            fill=colors[i]
            )
    #線
    can1.create_line(winw*0.8, 0, winw*0.8, winh)
    """
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
    """
    for i in range(8):
        komaimage.append(can1.create_image(komax[i], komay[i], image = clear_, anchor = tk.NW))
        """
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
    """
    nowTime = tk.StringVar()
    nowTime.set(str(countdown))
    nowTimeLabel = tk.Label(
        f1,
        textvariable = nowTime,
        font = (40),
        )
    nowTimeLabel.place(
        x = 185,
        y = 485
        )
        """
    timer_images = []
    for i in range(6):
        timer_images.append(can1.create_image(105, 485, image = timer_image[i], anchor = tk.NW))

    #ゴール時
    goal = 0

    #スタート画面
    f2 = tk.Frame(
        root,
        #bg = "#FFE47C",
        #width = 1000,
        #height = 1000,
        )
    #f2.place(x = 0, y = 0)
    f2.pack(
        fill=tk.BOTH,
        expand=True
        )
    team_name = ["A", "B", "C", "D", "E", "F", "G", "H"]
    can3 = tk.Canvas(
        f2,
        )
    can3.pack(
        expand=True,
        fill = tk.BOTH
        )
    can3.create_image(
        0,
        0,
        image = st_bg,
        anchor = tk.NW
        )
    """
    Title = tk.Label(
        can3,
        text = "運命の13階段!!　～高きを仰げ静高生～" ,
        font=(20),
        )
    Title.pack(
        expand=True
        )
    #Title.pack_forget()
    """
    txtbx = []
    txtbx_name = []
    cursor = 0
    #pushed = lambda pa : cursor = pa
    for i in range(8):
        txtbx.append(tk.Entry(
            can3,
            width = 14
            ))
        txtbx[i].insert(0, team_name[i])
        #txtbx_name.append(txtbx[i].nametowidget())
        if(i == 0):
            txtbx[i].pack(
                expand = True,
                anchor = tk.S
                )
        else:
            txtbx[i].pack(
                #side = tk.BOTTOM
                )
    root.bind('<Return>', kaigyo)
    #can3.bind('<ButtonRelease>', pushed)
    """
    txtbx = tk.Entry(
        f2,
        width=14
        )
    txtbx.pack(
        expand=True
        )
        """
    stButton = tk.Button(
        can3,
        text = "Start",
        command = qzst
        )
    stButton.pack(
        expand=True,
        #side = tk.BOTTOM
        )
    """
    maker = tk.Label(
        can3,
        text="作った人:甘糖ぷりん",
        font=(30)
        )
    maker.pack(
        #expand=True,
        anchor=tk.SE,
        side = tk.BOTTOM
        )
        """
    
    root.mainloop()

