import tkinter as tk

class Edit:
    def __init__(self, top,screen):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.top=top
        self.screen = width, height = screen
        w, h = 355, 302
        top.geometry("%dx%d+%d+%d" % (w, h, (width - w) / 2, (height - h) / 2))
        top.minsize(180, 10)
        top.maxsize(1924, 1050)
        top.resizable(0, 0)
        top.title("图书编辑")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.056, rely=0.066, relheight=0.745
                , relwidth=0.887)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Entry_Bookname = tk.Entry(self.Frame1)
        self.Entry_Bookname.place(relx=0.286, rely=0.089, height=34
                , relwidth=0.616)
        self.Entry_Bookname.configure(background="white")
        self.Entry_Bookname.configure(disabledforeground="#a3a3a3")
        self.Entry_Bookname.configure(font="-family {黑体} -size 13")
        self.Entry_Bookname.configure(foreground="#000000")
        self.Entry_Bookname.configure(highlightbackground="#d9d9d9")
        self.Entry_Bookname.configure(highlightcolor="black")
        self.Entry_Bookname.configure(insertbackground="black")
        self.Entry_Bookname.configure(selectbackground="#c4c4c4")
        self.Entry_Bookname.configure(selectforeground="black")

        self.Entry_Author = tk.Entry(self.Frame1)
        self.Entry_Author.place(relx=0.286, rely=0.356, height=34
                                , relwidth=0.616)
        self.Entry_Author.configure(background="white")
        self.Entry_Author.configure(disabledforeground="#a3a3a3")
        self.Entry_Author.configure(font="-family {黑体} -size 13")
        self.Entry_Author.configure(foreground="#000000")
        self.Entry_Author.configure(highlightbackground="#d9d9d9")
        self.Entry_Author.configure(highlightcolor="black")
        self.Entry_Author.configure(insertbackground="black")
        self.Entry_Author.configure(selectbackground="#c4c4c4")
        self.Entry_Author.configure(selectforeground="black")

        self.Entry_inventory = tk.Entry(self.Frame1)
        self.Entry_inventory.place(relx=0.286, rely=0.622, height=34
                , relwidth=0.616)
        self.Entry_inventory.configure(background="white")
        self.Entry_inventory.configure(disabledforeground="#a3a3a3")
        self.Entry_inventory.configure(font="-family {黑体} -size 13")
        self.Entry_inventory.configure(foreground="#000000")
        self.Entry_inventory.configure(highlightbackground="#d9d9d9")
        self.Entry_inventory.configure(highlightcolor="black")
        self.Entry_inventory.configure(insertbackground="black")
        self.Entry_inventory.configure(selectbackground="#c4c4c4")
        self.Entry_inventory.configure(selectforeground="black")

        self.Label_Bookname = tk.Label(self.Frame1)
        self.Label_Bookname.place(relx=0.095, rely=0.089, height=40, width=52)
        self.Label_Bookname.configure(activebackground="#f9f9f9")
        self.Label_Bookname.configure(activeforeground="black")
        self.Label_Bookname.configure(background="#d9d9d9")
        self.Label_Bookname.configure(disabledforeground="#a3a3a3")
        self.Label_Bookname.configure(font="-family {Microsoft YaHei UI} -size 10")
        self.Label_Bookname.configure(foreground="#000000")
        self.Label_Bookname.configure(highlightbackground="#d9d9d9")
        self.Label_Bookname.configure(highlightcolor="black")
        self.Label_Bookname.configure(text='''图书名''')

        self.Label_inventory = tk.Label(self.Frame1)
        self.Label_inventory.place(relx=0.095, rely=0.578, height=50, width=42)
        self.Label_inventory.configure(activebackground="#f9f9f9")
        self.Label_inventory.configure(activeforeground="black")
        self.Label_inventory.configure(background="#d9d9d9")
        self.Label_inventory.configure(disabledforeground="#a3a3a3")
        self.Label_inventory.configure(font="-family {Microsoft YaHei UI} -size 10")
        self.Label_inventory.configure(foreground="#000000")
        self.Label_inventory.configure(highlightbackground="#d9d9d9")
        self.Label_inventory.configure(highlightcolor="black")
        self.Label_inventory.configure(text='''库存''')

        self.Label_Author = tk.Label(self.Frame1)
        self.Label_Author.place(relx=0.095, rely=0.356, height=40, width=42)
        self.Label_Author.configure(activebackground="#f9f9f9")
        self.Label_Author.configure(activeforeground="black")
        self.Label_Author.configure(background="#d9d9d9")
        self.Label_Author.configure(disabledforeground="#a3a3a3")
        self.Label_Author.configure(font="-family {Microsoft YaHei UI} -size 10")
        self.Label_Author.configure(foreground="#000000")
        self.Label_Author.configure(highlightbackground="#d9d9d9")
        self.Label_Author.configure(highlightcolor="black")
        self.Label_Author.configure(text='''作者''')

        self.Button_Edit = tk.Button(top)
        self.Button_Edit.place(relx=0.338, rely=0.828, height=40, width=105)
        self.Button_Edit.configure(activebackground="#ececec")
        self.Button_Edit.configure(activeforeground="#000000")
        self.Button_Edit.configure(background="#d9d9d9")
        self.Button_Edit.configure(disabledforeground="#a3a3a3")
        self.Button_Edit.configure(font="-family {Microsoft YaHei UI} -size 10")
        self.Button_Edit.configure(foreground="#000000")
        self.Button_Edit.configure(highlightbackground="#d9d9d9")
        self.Button_Edit.configure(highlightcolor="black")
        self.Button_Edit.configure(pady="0")
        self.Button_Edit.configure(text='''修改''')