import csv
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def generateView(self, root):
        pass

class CsvTableView(View):
    def generateView(self, root):
      column = ('key', 'action')

      root.title("CSV Table")
      root.geometry("300x400")
      tree = ttk.Treeview(root, columns=column, show='headings')

      tree.column('#0',width=0, stretch='yes')
      tree.column('key', anchor='center', width=100)
      tree.column('action',anchor='w', width=200)

      tree.heading('key', text='key')
      tree.heading('action', text='action',anchor='center')
      
      # 同じディテクトリないのcsvファイルを読み込む。getCsvでファイルの入力を受け付ける
      # csvInput = getCsv()
      with open('command.csv', 'r', encoding='utf-8') as csvfile:
          reader = csv.DictReader(csvfile)
          i = 0

          for row in reader:
              values = []
              for j in range(len(column)):
                  values.append(row[column[j]])
              tree.insert(parent='', index='end', iid=i ,values=values)
              i += 1

          tree.pack(pady=0)
    
class AppCore:
    # インスタンス化と同時に、ライブラリのオブジェクトを作成する
    def __init__(self):
        self.root = self.initializeTK()
    # メインウィンドウのインスタンスを作成する。 ウィンドウサイズは固定で600×400
    def initializeTK(self):
        root = tk.Tk()
        root.geometry("600x400")
        root.title("CSV Table")

        return root

#rootと、Viewクラスを継承したクラスを引数に取る
def finalize(root, view: View):
    view.generateView(root)
    root.mainloop()
    
if __name__ == "__main__":
    core = AppCore()
    view = CsvTableView()
    finalize(core.root, view)

