import PySimpleGUI as sg
sg.theme("DarkBrown3")

member = [1,2,3,4,5,6,7,8]

layout = [[sg.T("何人で遊びますか",k="in", justification="center")],
          [sg.Listbox(values = member, size = (20,4)), sg.Button("次へ")]]
sg.Window("人数選択", layout,font=(None,14), size=(300,120))


while True:
    e, v = win.read()
    if e == "btn":
      # 次の画面へ進む
      execute()
    if e == None:
        break
win.close()
