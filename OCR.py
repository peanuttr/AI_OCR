import tkinter as tk
from tkinter import filedialog
import requests


root=tk.Tk()
root.title("Optical Character Recognition")

canvas = tk.Canvas(root,height=500,width=500)
canvas.pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

textstatus = tk.StringVar()
textword = tk.StringVar()

def on_click():
    global textw
    filename = filedialog.askopenfilename(initialdir='c:/desktop', title="Select File",
                                          filetypes=(("png", "*.png"), ("all file", "*.*"), ("jpg", "*.jpg")))
    url = "https://api.aiforthai.in.th/ocr"
    
    files = {'uploadfile':open(filename, 'rb')}
    
    headers = {
    'Apikey': "OK0DQ3hFQJhLxknHjhhKMGxcEfCV0WNe",
    }
    response = requests.post(url, files=files, headers=headers)
    response_json = response.json()['Original']
    print(response_json)
    textword.set(response_json)
    textstatus.set("Succes")

choosebtn = tk.Button(root,text="Choose File",command=on_click)
choosebtn.pack()
txtlabel = tk.Label(frame,textvariable=textword)
txtlabel.pack()
statuslabel = tk.Label(root,textvariable=textstatus)
statuslabel.pack()
root.mainloop()




