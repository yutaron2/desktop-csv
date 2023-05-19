import csv
import tkinter as tk
from tkinter import ttk
class CSVTable:
    
    ## メンバ変数
    master = None
    filename = None
    table_frame = None
    
    ## コンストラクタ
    def __init__(self, master, filename):
        self.master = master
        self.filename = filename
        # フレームを作成する
        self.table_frame = tk.Frame(self.master)
        # フレームを表示する pack()はフレームを表示するためのコード
        self.table_frame.pack(fill="both", expand=True)
        # CSVファイルを読み込む
        self.load_csv()

    def load_csv(self):
        # CSVファイルを読み込む
        with open(self.filename, "r") as f:
            # csv.reader()はCSVファイルを読み込むためのコード
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                # enumerate()はリストの要素を取り出すためのコード
                for j, cell in enumerate(row):
                    # tk.Label()はラベルを作るためのコード
                    label = tk.Label(self.tabid(row=i, column=j))

    def defineTree(root):
        column = ('keys', 'action')
        root.title("CSV Table")
        root.geometry("600x400")
        tree = ttk.Treeview(root, columns=column, show='headings')

        tree.column('#0',width=0, stretch='no')
        tree.column('keys', anchor='center', width=80)
        tree.column('action',anchor='w', width=100)
        
        tree.heading('keys', text='keys')
        tree.heading('action', text='action',anchor='center')
        
        tree.insert(parent='', index='end', iid=0 ,values=('h', 'カーソルを左に移動する'))
        tree.insert(parent='', index='end', iid=1 ,values=('j', 'カーソルを下に移動する'))
        tree.insert(parent='', index='end', iid=2 ,values=('k', 'カーソルを上に移動する'))
        tree.insert(parent='', index='end', iid=3 ,values=('l', 'カーソルを右に移動する'))
        
        # ウィジェットの配置
        tree.pack(pady=10)
        
        # root.mainloop()はrootを表示するためのコード
        root.mainloop()
        

class CSVTableMaker:

    CSVFile = None
    CSVTable = None

    def __init__(self, CSVFileName):
        self.CSVFile = CSVFileName

    # 外から呼び出すコード。
    def instantiateCSVTable(self):
        #　root を開発者に入力させたくないのでここで決め打ち
        self.CSVTable = CSVTable(root, self.CSVFile)
        
        return self.CSVTable
        
class AppCore:

    # インスタンス化と同時に、ライブラリのオブジェクトを作成する
    def __init__(self):
        self.root = self.initializeTK()

    # メインウィンドウのインスタンスを作成する。
    def initializeTK(self):
        root = tk.Tk()
        root.geometry("600x400")
        root.title("CSV Table")

        return root

def makeTableFromCSV(root, csvinput):
    column = ('keys', 'action')
    root.title("CSV Table")
    root.geometry("300x400")
    tree = ttk.Treeview(root, columns=column, show='headings')

    tree.column('#0',width=0, stretch='yes')
    tree.column('keys', anchor='center', width=100)
    tree.column('action',anchor='w', width=200)
    
    tree.heading('keys', text='keys')
    tree.heading('action', text='action',anchor='center')
    
    # csvinputから取り出したデータをfor文で入れる
    with open('command.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader:
            key = row['key']
            value = row['action']
            tree.insert(parent='', index='end', iid=i ,values=(key, value))
            i += 1
        # ウィジェットの配置
        tree.pack(pady=0)
        
        # root.mainloop()はrootを表示するためのコード
        # root.mainloop()

if __name__ == "__main__":
    # rootという変数にtk.Tk()を代入する
    core = AppCore()
    csvInput = 'command.csv'
    print('csvInput')
    
    # テーブルを定義
    makeTableFromCSV(core.root, csvInput)
    
    # 画面表示
    core.root.mainloop()


