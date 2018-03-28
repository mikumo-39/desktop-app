#ダイアログを表示するために必要なモジュール
import tkinter.messagebox as mb

#ダイアログを表示
ans = mb.askyesno("質問", "アニメが好きですか？")
if ans == True:
    #OK
    mb.showinfo("同意", "ガルパンはいいぞ" )
else:
    mb.showinfo("本当？", "悲しい( ；∀；)")
