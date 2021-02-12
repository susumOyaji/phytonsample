import tkinter as tk
#from tkinter import ttk, scrolledtext



   


class Circle(): #円オブジェクト
    def __init__(self,canvas,x,y,r,color,tag):
        self.canvas = canvas
        self.x = x #中心のx座標
        self.y = y #中心のy座標
        self.r = r #円の半径
        self.color = color
        self.tag = tag

    def createCircle(self): #円を作るメソッド
        self.canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill=self.color,tag=self.tag)
        self.canvas.create_text(self.x,self.y,text=self.tag,font=("Helvetica", 18, "bold"),fill="black",tag=self.tag)

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        
        # メインウィンドウ    
        self.width=450
        self.height=400
        master.geometry(str(self.width)+"x"+str(self.height)) #ウィンドウの作成
        master.title("StackCard Python Edition") #タイトル
        self.master.config(bg="black") #ウィンドウの背景色

          





        self.createCanvas() #キャンバスの作成

    def createCanvas(self): #キャンバスの作成
        self.canvas = tk.Canvas(self.master,width=self.width,height=self.height,bg="blue") #キャンバスの作成
        self.canvas.pack()

        self.circle1 = Circle(self.canvas,225,60,50,"red","circle1") #インスタンスcircle1の生成
        self.circle1.createCircle() #円の作成

        #多角形の作成
        self.canvas.create_polygon(10,10,60,10,35,60,fill="purple")
        self.canvas.create_polygon(390,10,440,10,440,60,390,60,fill="orange")
        self.canvas.create_polygon(390,340,440,340,415,390,fill="green")
        self.canvas.create_polygon(10,340,60,340,60,390,10,390,fill="yellow")


class StackCard(tk.Frame):
    # メインウィンドウ
    main_window = Tk()
    main_window.title('mo22comi')
    main_window.geometry('600x830')
    
    # メインフレーム
    main_frame = tk.Frame(main_window)
    main_frame.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

    text_frame = ttk.Frame(main_window)
    text_frame.grid(column=0, row=1, sticky=tkinter.NSEW, padx=5, pady=10)

    # ログフレーム
    log_frame = ttk.Frame(main_window)
    log_frame.grid(column=0, row=2, sticky=tkinter.NSEW, padx=5, pady=10)

    # ウィジェット作成
    file_label = ttk.Label(main_frame, text='データ')
    file_box = ttk.Entry(main_frame)
    file_btn = ttk.Button(main_frame, text='参照')
    entry_label = ttk.Label(main_frame, text='エントリー')
    entry_box = ttk.Entry(main_frame)

    text_label = ttk.Label(text_frame, text='テキスト')
    text_box = scrolledtext.ScrolledText(text_frame)

    log_label = ttk.Label(log_frame, text='ログ')
    log_box = scrolledtext.ScrolledText(log_frame)

    # ウィジェットの配置
    file_label.grid(column=0, row=0, pady=10, padx=5)
    file_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
    file_btn.grid(column=2, row=0, padx=5)

    entry_label.grid(column=0, row=1)
    entry_box.grid(column=1, row=1, sticky=tkinter.EW, pady=10, padx=5)

    text_label.grid(column=0, row=0, sticky=tkinter.NW, padx=5)
    text_box.grid(column=0, row=1, pady=5, padx=5)

    log_label.grid(column=0, row=0, sticky=tkinter.NW, padx=5)
    log_box.grid(column=0, row=1, pady=10, padx=5)

    # 配置設定
    main_window.columnconfigure(0, weight=1)
    main_window.rowconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)

    #main_window.mainloop()



def main():
    #win = tk.Tk()
    #win.resizable(width=False, height=False) #ウィンドウを固定サイズに
   
    app = MainScreen(master=win)
    #app.mainloop()
    main_window.mainloop()

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
      

        self.title = 'Python to Iphone App'
        self.text = 'start'

if __name__ == "__main__":
    TestApp(App).run()