#-*-coding:utf-8-*- 
import sys
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import filedialog
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
from openpyxl import load_workbook
from tkinter import messagebox
import DBoperator as db
from Edit import Edit
class Manager:
    def __init__(self,top,user,screen):
        self.root=top
        self.screen=screen
        self.graph_init(top,user,screen)
        self.book_list()
        self.user_list()
    def book_edit(self):
        if str(self.Option.select()) == str(self.Option_t1):
            tk.messagebox.showinfo('错误', message='请到图书管理界面进行修改')
            return
        item = self.BookList.selection()
        book = self.BookList.item(item, 'values')
        print('修改图书-->', book)
        if type(book) != tuple:
            tk.messagebox.showinfo('错误', message='请选中修改图书')
            return
        etop=tk.Toplevel(self.root)
        self.editer=Edit(etop,self.screen)
        etop.title("图书编辑")
        self.editer.Button_Edit.configure(text='''修改''')
        self.editer.Entry_Bookname.insert('0',book[1])
        self.editer.Entry_Author.insert('0',book[2])
        self.editer.Entry_inventory.insert('0',book[3])
        self.editer.Button_Edit.configure(command=lambda *p:self.book_dbop(book[0]))
        etop.mainloop()
        del self.editer
    def book_add(self):
        if str(self.Option.select()) == str(self.Option_t1):
            tk.messagebox.showinfo('错误', message='请到图书管理界面进行修改')
            return
        etop = tk.Toplevel(self.root)
        self.editer = Edit(etop, self.screen)
        etop.title("图书添加")
        self.editer.Button_Edit.configure(text='''添加''')
        self.editer.Button_Edit.configure(command=self.book_dbadd)
        etop.mainloop()
    def book_dbadd(self):
        bookname = self.editer.Entry_Bookname.get()
        author = self.editer.Entry_Author.get()
        inventory = self.editer.Entry_inventory.get()
        book = (bookname, author, inventory)
        d = db.Db()
        d.book_add(book)
        tk.messagebox.showinfo('消息', message='添加成功')
        self.editer.top.destroy()
        self.book_list()
        del self.editer
    def book_dbop(self,bookid):
        bookname=self.editer.Entry_Bookname.get()
        author=self.editer.Entry_Author.get()
        inventory=self.editer.Entry_inventory.get()
        book=(bookid,bookname,author,inventory)
        d=db.Db()
        d.book_edit(book)
        tk.messagebox.showinfo('消息', message='修改成功')
        self.editer.top.destroy()
        self.book_list()
        del self.editer
    def book_del(self):
        if str(self.Option.select()) == str(self.Option_t1):
            tk.messagebox.showinfo('错误', message='请到图书管理界面进行删除')
            return
        item = self.BookList.selection()
        book = self.BookList.item(item, 'values')
        if type(book)!=tuple:
            tk.messagebox.showinfo('错误', message='请选中删除图书')
            return
        if tk.messagebox.askokcancel('提示', '要执行此操作吗')==False:
            return
        print('删除图书-->',book)
        d = db.Db()
        d.book_del(book)
        tk.messagebox.showinfo('消息', message='删除成功')
        self.book_list()
        del d
    def open_file(self):
        filename = tk.filedialog.askopenfilename()
        if filename != '':
            print("您选择的文件是：" + filename)
            self.book_list_add(filename)
        else:
            print("您没有选择任何文件")
    def book_list_add(self,filename):
        try:
            wb = load_workbook(filename)
        except:
            tk.messagebox.showinfo('错误', message='文件读取错误，请导入正确的文件')
            return
        ws1 = wb.active
        d=db.Db()
        for i, j, k in ws1.rows:
            d.book_add((i.value, j.value, k.value))
        tk.messagebox.showinfo('消息', message='导入成功')
        self.book_list()
        del d
    def book_list_cls(self):
        x=self.BookList.get_children()
        for i in x:
            self.BookList.delete(i)
    def book_list(self):
        self.book_list_cls()
        d=db.Db()
        for line in d.book_list():
            self.BookList.insert('','end',values=line)
        del d
    def user_del(self):
        if str(self.Option.select()) == str(self.Option_t0):
            tk.messagebox.showinfo('错误', message='请到用户管理界面进行删除')
            return
        item=self.UserList.selection()
        user = self.UserList.item(item, 'values')
        if type(user)!=tuple:
            tk.messagebox.showinfo('错误', message='请选中删除用户')
            return
        if tk.messagebox.askokcancel('提示', '要执行此操作吗')==False:
            return
        print('删除用户-->', user)
        d = db.Db()
        d.user_del(user)
        tk.messagebox.showinfo('消息', message='删除成功')
        self.user_list()
        del d
    def user_list_cls(self):
        x = self.UserList.get_children()
        for i in x:
            self.UserList.delete(i)
    def user_list(self):
        self.user_list_cls()
        d = db.Db()
        for line in d.user_list():
            self.UserList.insert('', 'end', values=line)
        del d
    def db_cls(self):
        if tk.messagebox.askokcancel('提示', '确认初始化数据库么')==False:
            return
        d = db.Db()
        d.db_cls()
        del d
        self.root.destroy()
    def graph_init(self,top,user,screen):

        self.screen = width, height = screen
        w, h = 990,513
        top.geometry("%dx%d+%d+%d" % (w, h, (width - w) / 2, (height - h) / 2))
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])
        top.minsize(180, 1)
        top.maxsize(1000, 600)
        top.resizable(0, 0)
        top.title("图书管理系统")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.sub_menu = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 font="TkMenuFont",
                                 foreground="#000000",
                                 label="菜单")
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="导入图书",
            command=self.open_file)
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="退出系统",
            command=self.root.quit)
        self.sub_menu1 = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 font="TkMenuFont",
                                 foreground="#000000",
                                 label="编辑")
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="添加图书",
            command=self.book_add)
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="编辑图书",
            command=self.book_edit)
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="删除图书",
            command=self.book_del)
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="删除用户",
            command=self.user_del)

        self.sub_menu2 = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu2,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 font="TkMenuFont",
                                 foreground="#000000",
                                 label="初始化")
        self.sub_menu2.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="清空数据库",
            command=self.db_cls)

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
        [('selected', _compcolor), ('active', _ana2color)])
        self.Option = ttk.Notebook(top)
        self.Option.place(relx=0.04, rely=0.156, relheight=0.77, relwidth=0.923)
        self.Option.configure(takefocus="")
        self.Option_t0 = tk.Frame(self.Option)
        self.Option.add(self.Option_t0, padding=3)
        self.Option.tab(0, text="图书管理", compound="left", underline="-1", )
        self.Option_t0.configure(background="#d9d9d9")
        self.Option_t0.configure(highlightbackground="#d9d9d9")
        self.Option_t0.configure(highlightcolor="black")
        self.Option_t1 = tk.Frame(self.Option)
        self.Option.add(self.Option_t1, padding=3)
        self.Option.tab(1, text="用户管理", compound="left", underline="-1", )
        self.Option_t1.configure(background="#d9d9d9")
        self.Option_t1.configure(highlightbackground="#d9d9d9")
        self.Option_t1.configure(highlightcolor="black")

        self.style.configure('Treeview', font="TkDefaultFont")
        self.BookList = ScrolledTreeView(self.Option_t0)
        self.BookList.place(relx=0.0, rely=0.0, relheight=1.008, relwidth=0.996)
        self.BookList.configure(columns="Col1 Col2 Col3 Col4")
        # build_treeview_support starting.
        self.BookList.heading("#0", text="图书编号")
        self.BookList.heading("#0", anchor="center")
        self.BookList.column("#0", width="0")
        self.BookList.column("#0", minwidth="20")
        self.BookList.column("#0", stretch="0")
        self.BookList.column("#0", anchor="center")
        self.BookList.heading("Col1", text="图书编号")
        self.BookList.heading("Col1", anchor="center")
        self.BookList.column("Col1", width="182")
        self.BookList.column("Col1", minwidth="20")
        self.BookList.column("Col1", stretch="1")
        self.BookList.column("Col1", anchor="center")
        self.BookList.heading("Col2", text="图书名称")
        self.BookList.heading("Col2", anchor="center")
        self.BookList.column("Col2", width="334")
        self.BookList.column("Col2", minwidth="20")
        self.BookList.column("Col2", stretch="1")
        self.BookList.column("Col2", anchor="center")
        self.BookList.heading("Col3", text="作者")
        self.BookList.heading("Col3", anchor="center")
        self.BookList.column("Col3", width="183")
        self.BookList.column("Col3", minwidth="20")
        self.BookList.column("Col3", stretch="1")
        self.BookList.column("Col3", anchor="center")
        self.BookList.heading("Col4", text="库存")
        self.BookList.heading("Col4", anchor="center")
        self.BookList.column("Col4", width="170")
        self.BookList.column("Col4", minwidth="20")
        self.BookList.column("Col4", stretch="1")
        self.BookList.column("Col4", anchor="center")

        self.UserList = ScrolledTreeView(self.Option_t1)
        self.UserList.place(relx=0.0, rely=0.0, relheight=1.008, relwidth=0.996)
        self.UserList.configure(columns="Col1 Col2 Col3 Col4")
        # build_treeview_support starting.
        self.UserList.heading("#0", text="user")
        self.UserList.heading("#0", anchor="center")
        self.UserList.column("#0", width="0")
        self.UserList.column("#0", minwidth="20")
        self.UserList.column("#0", stretch="0")
        self.UserList.column("#0", anchor="w")
        self.UserList.heading("Col1", text="用户ID")
        self.UserList.heading("Col1", anchor="center")
        self.UserList.column("Col1", width="139")
        self.UserList.column("Col1", minwidth="20")
        self.UserList.column("Col1", stretch="1")
        self.UserList.column("Col1", anchor="center")
        self.UserList.heading("Col2", text="用户名")
        self.UserList.heading("Col2", anchor="center")
        self.UserList.column("Col2", width="260")
        self.UserList.column("Col2", minwidth="20")
        self.UserList.column("Col2", stretch="1")
        self.UserList.column("Col2", anchor="center")
        self.UserList.heading("Col3", text="姓名")
        self.UserList.heading("Col3", anchor="center")
        self.UserList.column("Col3", width="291")
        self.UserList.column("Col3", minwidth="20")
        self.UserList.column("Col3", stretch="1")
        self.UserList.column("Col3", anchor="w")
        self.UserList.heading("Col4", text="用户类型")
        self.UserList.heading("Col4", anchor="center")
        self.UserList.column("Col4", width="193")
        self.UserList.column("Col4", minwidth="20")
        self.UserList.column("Col4", stretch="1")
        self.UserList.column("Col4", anchor="w")

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.04, rely=0.039, relheight=0.127
                               , relwidth=0.919)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''用户信息''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Labelframe1)
        self.Label1.place(relx=0.055, rely=0.462, height=30, width=66
                          , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''用户名：''')

        self.Label_Username = tk.Label(self.Labelframe1)
        self.Label_Username.place(relx=0.143, rely=0.462, height=30, width=102
                                  , bordermode='ignore')
        self.Label_Username.configure(activebackground="#f9f9f9")
        self.Label_Username.configure(activeforeground="black")
        self.Label_Username.configure(background="#d9d9d9")
        self.Label_Username.configure(disabledforeground="#a3a3a3")
        self.Label_Username.configure(foreground="#000000")
        self.Label_Username.configure(highlightbackground="#d9d9d9")
        self.Label_Username.configure(highlightcolor="black")
        self.Label_Username.configure(text=user[0])

        self.Label1_1 = tk.Label(self.Labelframe1)
        self.Label1_1.place(relx=0.297, rely=0.462, height=30, width=78
                            , bordermode='ignore')
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''姓名：''')

        self.Label1_2 = tk.Label(self.Labelframe1)
        self.Label1_2.place(relx=0.549, rely=0.462, height=30, width=108
                            , bordermode='ignore')
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''用户类型：''')

        self.Label_Name = tk.Label(self.Labelframe1)
        self.Label_Name.place(relx=0.374, rely=0.462, height=30, width=102
                              , bordermode='ignore')
        self.Label_Name.configure(activebackground="#f9f9f9")
        self.Label_Name.configure(activeforeground="black")
        self.Label_Name.configure(background="#d9d9d9")
        self.Label_Name.configure(disabledforeground="#a3a3a3")
        self.Label_Name.configure(foreground="#000000")
        self.Label_Name.configure(highlightbackground="#d9d9d9")
        self.Label_Name.configure(highlightcolor="black")
        self.Label_Name.configure(text=user[1])

        self.LabelUserType = tk.Label(self.Labelframe1)
        self.LabelUserType.place(relx=0.659, rely=0.462, height=30, width=92
                                 , bordermode='ignore')
        self.LabelUserType.configure(activebackground="#f9f9f9")
        self.LabelUserType.configure(activeforeground="black")
        self.LabelUserType.configure(background="#d9d9d9")
        self.LabelUserType.configure(disabledforeground="#a3a3a3")
        self.LabelUserType.configure(foreground="#000000")
        self.LabelUserType.configure(highlightbackground="#d9d9d9")
        self.LabelUserType.configure(highlightcolor="black")
        self.LabelUserType.configure(text=user[2])


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        # self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')