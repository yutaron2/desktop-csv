import csv
import tkinter as tk

class CSVTable:
    def __init__(self, master, filename):
        self.master = master
        self.filename = filename
        self.table_frame = tk.Frame(self.master)
        self.table_frame.pack(fill="both", expand=True)
        self.load_csv()

    def load_csv(self):
        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                for j, cell in enumerate(row):
                    label = tk.Label(self.table_frame, text=cell, borderwidth=1, relief="solid")
                    label.grid(row=i, column=j)

# Path: main.py
# もし__nameが__main__だったら、以下のコードを実行する
if __name__ == "__main__":
    # rootという変数にtk.Tk()を代入する
    root = tk.Tk()
    root.geometry("600x400")
    root.title("CSV Table")
    table = CSVTable(root, "/Users/nishidayuutarou/Desktop/spotify_API/view_csv/command.csv")
    root.mainloop()
