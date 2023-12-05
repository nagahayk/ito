import PySimpleGUI as sg
sg.theme("DarkBrown3")
#時間
import datetime
#ランダム
import random
#thinker
import tkinter
from tkinter import messagebox


#--------------名前入力----------------------------------
def name():
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
def card():
    global win
    left=150
    right=0
    top=0
    bottom=0
    layout = [[sg.Text('-'*100)],
              [sg.Text("一人目 カードをめくってください",k="txt", size=(100,1), justification="center",pad=((0,0), (0,0)))],
              [sg.Text('-'*100)],
              [sg.Button("aaa",k="card", size=(100,100), image_filename='./pic2.gif',pad=((left, right), (top, bottom)))],
              [sg.Text('-'*100)]]
    win = sg.Window("カードをめくる", layout,
                font=(None,20), size=(1000,700), keep_on_top=True)


#--------------議論時間ウィンドウ------------------
def discussion():
    global win
    layout = [[sg.T("20:00", font=("Arial",40), k="txt",
            size=(30,1), justification="center")],
            [sg.Push(), sg.B("スタート", k="btn"), sg.Push()],
            [sg.Push(), sg.B("議論を終了して意図をたしかめる", k="btn_answer"), sg.Push()]]
    win = sg.Window("ディスカッションタイム", layout,
                    font=(None,14), size=(700,300), keep_on_top=True)
#--------------議論終了ウィンドウ----------------------
def end():
    global win
    left=10
    right=20
    top=100
    bottom=40
    layout = [[sg.Push(), sg.B("意図をたしかめる", k="btn_answer"), sg.Push()],
              [sg.Text("ディスカッションタイム終了!", size=(60,60), justification="center",pad=((left, right), (top, bottom)))]]
    win = sg.Window("ディスカッションタイム終了", layout,
                font=(None,30), size=(700,300), keep_on_top=True)

#---------------数字が小さいと思う人からカードをめくってくださいのウィンドウ---------------------
def answer():
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
randomNum = random.random()

def pera():
    win["card"].update(text="randomNum")
    
 


###20分間-経過時間(更新し続ける)###
def execute():
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
window = name()
startFlag = False

while True:
    e, v = win.read(timeout=50)
    execute()
    if e == "btn_NameNext":
        card()
    if e == "card":
        pera()
    if e == "btn":      
        startStop()
        t1 = datetime.datetime.now() 
    if e == "btn_answer":
        win.close()
        window = answer()
    if e == "answerCard":
        peraAnswer()
    if e == None:
        break
win.close()