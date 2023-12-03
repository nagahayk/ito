import PySimpleGUI as sg

"""
プレイ人数: select_people
人数選択画面: make1_select_number
カード閲覧説明: make2_showdown_card(プレイ人数)
"""

def make1_select_number():
    # ------------ 人数選択画面の作成 ------------
    member = [1,2,3,4,5,6,7,8]
    select_number_layout = [[sg.T("何人で遊びますか",k="in", justification="center")],
          [sg.Listbox(values = member, size = (20,4)), sg.Button("次へ", k="select_number")]]
    return sg.Window("人数選択", select_number_layout,font=(None,14), size=(300,120),finalize=True)


def make2_showdown_card():
    # ------------ カードを見る説明画面 ------------
    showdown_card_layout = [[sg.Button("Close")]]
    return sg.Window("サブウィンドウ", showdown_card_layout, font=(None,14), size=(300,120), finalize=True)

# 最初に表示するウィンドウの指定
window = make1_select_number()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    ## 人数選択が終了して次へを押したとき
    elif event == "select_people" and values[0]:
        # 人数を変数に代入
        select_number = values[0][0]
        ## カード表示説明画面へ
        window.close()
        window = make2_showdown_card()

    elif event == "Close":
        # サブウィンドウを閉じて、メインウィンドウを作成して表示する
        window.close()
        window = make1_select_number()
    

# ウィンドウを終了する
window.close()