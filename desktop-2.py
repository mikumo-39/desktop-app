#tkinterを取り込む
from tkinter import*
import tkinter.messagebox as mb

#ボタンが押された時の動作を巻数として定義
def say_hello():
    mb.showinfo("10連ガチャ結果", "大爆死です")

#メインウィンドウを作製
root = Tk()
root.title('10連ガチャ　SSRもでる')

#ラベル作成
desc_label = Label(text = '10連ガチャを回す？')
desc_label.pack()

#挨拶ボタン作成
hello_button = Button(
    text = "10連ガチャ",
    width = 10, height = 3,
    command = say_hello
)
hello_button.pack()

root.mainloop()
