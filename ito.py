import PySimpleGUI as sg

"""
プレイ人数: select_people
人数選択画面: make1_select_number
カード閲覧説明: make2_showdown_card(プレイ人数)
"""

def make1_select_number():
    # ------------ 人数選択画面の作成 ------------
    member = [3,4,5,6,7,8]
    select_number_layout = [[sg.T("何人で遊びますか",size = (100,10), justification="center")],
    [sg.Listbox(values = member, size = (50,6))],
    [sg.Button("次へ", k="select_number")]]
    
    return sg.Window("人数選択", select_number_layout,font=(None,14), size=(1000,700),finalize=True)


def make2_showdown_card():
    # ------------ カードを見る説明画面 ------------
    showdown_card_layout = [[sg.Button("次へ")],
                            [sg.Text(select_number)]]               
    return sg.Window("サブウィンドウ", showdown_card_layout, font=(None,14), size=(1000,700), finalize=True)

def make3_show_number():
    # -------------実際にカードを見る画面-------------
    show_number =

def make4_show_number_next():
# 最初に表示するウィンドウの指定
window = make1_select_number()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    ## 人数選択が終了して次へを押したとき
    elif event == "select_number" and values[0]:
        # 人数を変数に代入
        select_number = values[0][0]
        ## カード表示説明画面へ
        window.close()
        window = make2_showdown_card()

    if event == "次へ":
        # サブウィンドウを閉じて、メインウィンドウを作成して表示する
        window.close()
        window = make1_select_number()
    

# ウィンドウを終了する
window.close()