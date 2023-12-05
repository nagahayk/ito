import PySimpleGUI as sg
sg.theme("DarkBrown3")
#時間
import datetime

"""
プレイ人数: select_people
人数選択画面: make1_select_number
カード閲覧説明: make2_showdown_card(プレイ人数)

"""

def make1_select_number():
    global win
    # ------------ 人数選択画面の作成 ------------
    member = [3,4,5,6,7,8]
    select_number_layout = [[sg.T("何人で遊びますか",size = (100,10), justification="center")],
    [sg.Listbox(values = member, size = (50,6))],
    [sg.Button("次へ", k="select_number")]]
    
    win = sg.Window("人数選択", select_number_layout,font=(None,14), size=(1000,700),finalize=True)


def make2_showdown_card():
    global win
    # ------------ カードを見る説明画面 ------------
    showdown_card_layout = [[sg.Button("次へ", k="next3")],
                            [sg.Text(select_number)]]               
    win = sg.Window("カードを見る説明", showdown_card_layout, font=(None,14), size=(1000,700), finalize=True)

def make3_show_number_next():
    global win
    # -------------次の人に順番を回す-------------
    show_number_next = [[sg.Text("次の人に回してください")],[sg.Button("次へ", k = "next4")]]
    win = sg.Window("次の人に回す", show_number_next)
    
def make4_show_number():
    global win
    # -------------カードを見る画面---------------
    show_number =[[sg.Text("あなたのカードです")],
        [sg.Button("次へ", k = "next5")]]
    win = sg.Window("実際にカードを見る", show_number, font=(None,14), size=(1000,700), finalize=True)

'''
#--------------名前入力----------------------------------
def make3_wright_name():
    global win
    layout = [[sg.Text('-'*100)],
              [sg.Text("一人目 このカードを見る人の名前を入力してください",k="txt", size=(100,1), justification="center",pad=((0,0), (0,0)))],
              [sg.InputText(k="txt", size=(100,1), justification="center",pad=((0,0), (0,0)))],
              [sg.Image(filename='pic2.gif', pad=((150,0), (30,30)))],
              [sg.Text('-'*100)],
              [sg.B("つぎへ", k="btn_NameNext")],
              [sg.Text('-'*100)]]
    win = sg.Window("カードをめくる", layout,
                font=(None,20), size=(1000,700), keep_on_top=True)
  
    

#--------------カードを配るウィンドウ--------------------
def make4_showdown():
    global win
    left=150
    right=0
    top=0
    bottom=0
    layout = [[sg.Text('-'*100)],
              [sg.Text("一人目 カードをめくってください",k="txt", size=(100,1), justification="center",pad=((0,0), (0,0)))],
              [sg.Text('-'*100)],
              [sg.Button(k="card", size=(100,100), image_filename='./pic2.gif',pad=((left, right), (top, bottom)))],
              [sg.Text('-'*100)]]
    win = sg.Window("カードをめくる", layout,
                font=(None,20), size=(1000,700), keep_on_top=True)
'''

def make5_theme_select():
    # ----------テーマを決める------------
    global win
    layout = [[sg.T("テーマを決めてください")],[sg.B("決定", k = "next6")]]
    win = sg.Window("テーマ決め", layout,
                font=(None,14), size=(700,300), keep_on_top=True)

#--------------議論時間ウィンドウ------------------
def make6_discussion():
    global win
    layout = [[sg.T("20:00", font=("Arial",40), k="txt",
            size=(30,1), justification="center")],
            [sg.Push(), sg.B("スタート", k="btn_start"), sg.Push()],
            [sg.Push(), sg.B("議論を終了して意図をたしかめる", k="next8"), sg.Push()]]
    win = sg.Window("ディスカッションタイム", layout,
                    font=(None,14), size=(700,300), keep_on_top=True)
#--------------議論終了ウィンドウ----------------------
# 時間終了前にbtn_answerを押したらこのWindowは表示されない
def make7_discussion_end():
    global win
    left=10
    right=20
    top=100
    bottom=40
    layout = [[sg.Push(), sg.B("意図をたしかめる", k="next8"), sg.Push()],
              [sg.Text("ディスカッションタイム終了!", size=(60,60), justification="center",pad=((left, right), (top, bottom)))]]
    win = sg.Window("ディスカッションタイム終了", layout,
                font=(None,30), size=(700,300), keep_on_top=True)

#---------------数字が小さいと思う人からカードをめくってくださいのウィンドウ---------------------
def make8_answer():
    global win
    name1 ="いぬうさぎ"
    cardFrame = sg.Frame(name1,[
        [sg.Button(k="answerCard", size=(100,100), image_filename='./pic2.gif')]
    ])
    cardFrame2 = sg.Frame("card2",[
        [sg.Button(k="answerCard", size=(100,100), image_filename='./pic2.gif')]
    ])
    cardFrame3 = sg.Frame("card3",[
        [sg.Button(k="answerCard", size=(100,100), image_filename='./pic2.gif')]
    ])
    cardFrame4 = sg.Frame("card4",[
        [sg.Button(k="answerCard", size=(100,100), image_filename='./pic2.gif')]
    ])
    cardFrame5 = sg.Frame("card5",[
        [sg.Button(k="answerCard", size=(100,100), image_filename='./pic2.gif')]
    ])
    cardFrame6 = sg.Frame("card6",[
        [sg.Button(k="answerCard", size=(100,100), image_filename='./pic2.gif')]
    ])
    cardFrame7 = sg.Frame("card7",[
        [sg.Button(k="answerCard", size=(100,100), image_filename='./pic2.gif')]
    ])
    cardFrame8 = sg.Frame("card8",[
        [sg.Button(k="answerCard", size=(100,100), image_filename='./pic2.gif')]
    ])
    left=0
    right=0
    top=0
    bottom=0
    num = 8
    if num ==3:  
        layout = [
            [sg.Text("数字が小さいと思う人からカードをめくってください",k ="txt", size=(100,1), justification="center",pad=((left, right), (top, bottom)))],
            [cardFrame,cardFrame2,cardFrame3]]
    if num==4:
        layout = [
            [sg.Text("数字が小さいと思う人からカードをめくってください",k ="txt", size=(100,1), justification="center",pad=((left, right), (top, bottom)))],
            [cardFrame,cardFrame2,cardFrame3],
            [cardFrame4]]
    if num==5:
        layout = [
            [sg.Text("数字が小さいと思う人からカードをめくってください",k ="txt", size=(100,1), justification="center",pad=((left, right), (top, bottom)))],
            [cardFrame,cardFrame2,cardFrame3],
            [cardFrame4,cardFrame5]]
    if num==6:
        layout = [
            [sg.Text("数字が小さいと思う人からカードをめくってください",k ="txt", size=(100,1), justification="center",pad=((left, right), (top, bottom)))],
            [cardFrame,cardFrame2,cardFrame3],
            [cardFrame4,cardFrame5,cardFrame6]] 
    if num==7:
        layout = [
            [sg.Text("数字が小さいと思う人からカードをめくってください",k ="txt", size=(100,1), justification="center",pad=((left, right), (top, bottom)))],
            [cardFrame,cardFrame2,cardFrame3],
            [cardFrame4,cardFrame5,cardFrame6],
            [cardFrame7]]        
    if num==8:
        layout = [
            [sg.Text("数字が小さいと思う人からカードをめくってください",k ="txt", size=(100,1), justification="center",pad=((left, right), (top, bottom)))],
            [cardFrame,cardFrame2,cardFrame3],
            [cardFrame4,cardFrame5,cardFrame6],
            [cardFrame7,cardFrame8]]          
    #layout=[[sg.Text('-'*100)]]
        #        [sg.Text("数字が小さいと思う人からカードをめくってください",k ="txt", size=(100,1), justification="center",pad=((left, right), (top, bottom)))],
                #[sg.Frame("()さんのカード",card), sg.Frame("()さんのカード",card)],
         ##      [sg.Button(k="answerCard", size=(100,100), image_filename='./pic2.gif',pad=((left, right), (top, bottom))),sg.Button(k="answerCard", size=(100,100), image_filename='./pic2.gif',pad=((left, right), (top, bottom)))],
           #     [sg.Text('-'*100)]]
    win = sg.Window("意図をたしかめる", layout,
                    font=(None,20), size=(1000,700), keep_on_top=True)

        
###カードをめくる###

def make9_pera():
    win["card"].update(image_filename='./pic.gif')
    
 

# ------制限時間に関する関数-----
###20分間-経過時間(更新し続ける)###
def timeflag():
    global t3, endTime, time2, window, startFlag
    if startFlag == True:
        t2 = datetime.datetime.now()        #現在の時間
        time = t2-t1                        #経過時間
        t3 = t1.replace(hour=0, minute=0, second=5) - time
        win["txt"].update(f"{t3: %M:%S}")
        endTime = datetime.time(23,59,59)
        time2 = t3.time()
        if time2 > endTime:
            win.close()
            window = end()
            startFlag = False
        
#議論時間スタートボタンを押したとき      
def startStop():
    global start, startFlag
    if startFlag == True:
        startFlag = False
    else:
        startFlag = True  

#answerCardをめくる
def peraAnswer():
    win["answerCard"].update(image_filename='./pic2.png')
        
#初期   
window = make1_select_number()
startFlag = False


# 画面遷移
while True:
    e, v = win.read(timeout=50)
    timeflag()

    if e == sg.WIN_CLOSED:
        break
    elif e == "select_number" and v[0]:
        # 人数を変数に代入
        select_number = v[0][0]
        ## カード表示説明画面へ
        win.close()
        window = make2_showdown_card()
    elif e == "next3":
        win.close()
        window = make3_show_number_next()
    elif e == "next4":
        win.close()
        window = make4_show_number()
    elif e == "next5":
        win.close()
        window = make5_theme_select()
    elif e == "next6":
        win.close()
        window = make6_discussion()
    elif e == "btn_start":
        # 会議のタイマーを開始する      
        startStop()
        t1 = datetime.datetime.now() 
    elif e == "next8":
        win.close()
        window = make8_answer()
    if e == "answerCard":
        peraAnswer()
    if e == None:
        break
win.close()