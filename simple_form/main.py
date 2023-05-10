import PySimpleGUI as sg 
import pandas as pd 


#add some color to the window 

sg.theme('Kayak')

filename='app.xlsx'

layout=[
    [sg.Text('Please fill the relevant fields:')],
    [sg.Text('Name',size=(15,1)),sg.InputText(key='Name')],
    [sg.Submit(),sg.Exit()]
]

window=sg.Window('Simple app that stores names',layout)

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED or event=='Exit':
        break
    if event == 'Submit':
        try:
            df=pd.read_excel(filename)
        except  FileNotFoundError:
            df=pd.DataFrame(columns=['Name'])
        df = pd.concat([df, pd.DataFrame([values])], ignore_index=True)
        df.to_excel(filename, index=False)
       
        sg.popup("Name added!!")
window.close()