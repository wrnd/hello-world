#-*-coding:utf-8-*- 
import tkinter as tk
from tkinter import messagebox
import DBoperator as db
class Regist:
    def __init__(self,top,screen):
        width, height = screen
        w, h = 355,390
        top.geometry("%dx%d+%d+%d" % (w, h, (width - w) / 2, (height - h) / 2))

        top.minsize(180, 10)
        top.maxsize(1924, 1050)
        top.resizable(0, 0)
        top.title("用户注册")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.top=top
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.056, rely=0.051, relheight=0.808
                , relwidth=0.887)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Entry_Username = tk.Entry(self.Frame1)
        self.Entry_Username.place(relx=0.286, rely=0.063, height=34
                , relwidth=0.616)
        self.Entry_Username.configure(background="white")
        self.Entry_Username.configure(disabledforeground="#a3a3a3")
        self.Entry_Username.configure(font="-family {黑体} -size 13")
        self.Entry_Username.configure(foreground="#000000")
        self.Entry_Username.configure(highlightbackground="#d9d9d9")
        self.Entry_Username.configure(highlightcolor="black")
        self.Entry_Username.configure(insertbackground="black")
        self.Entry_Username.configure(selectbackground="#c4c4c4")
        self.Entry_Username.configure(selectforeground="black")

        self.Entry_Name = tk.Entry(self.Frame1)
        self.Entry_Name.place(relx=0.286, rely=0.254,height=34, relwidth=0.616)
        self.Entry_Name.configure(background="white")
        self.Entry_Name.configure(disabledforeground="#a3a3a3")
        self.Entry_Name.configure(font="-family {黑体} -size 13")
        self.Entry_Name.configure(foreground="#000000")
        self.Entry_Name.configure(highlightbackground="#d9d9d9")
        self.Entry_Name.configure(highlightcolor="black")
        self.Entry_Name.configure(insertbackground="black")
        self.Entry_Name.configure(selectbackground="#c4c4c4")
        self.Entry_Name.configure(selectforeground="black")

        self.Entry_Pwd = tk.Entry(self.Frame1)
        self.Entry_Pwd.place(relx=0.286, rely=0.444,height=34, relwidth=0.616)
        self.Entry_Pwd.configure(background="white")
        self.Entry_Pwd.configure(disabledforeground="#a3a3a3")
        self.Entry_Pwd.configure(font="-family {黑体} -size 13")
        self.Entry_Pwd.configure(foreground="#000000")
        self.Entry_Pwd.configure(highlightbackground="#d9d9d9")
        self.Entry_Pwd.configure(highlightcolor="black")
        self.Entry_Pwd.configure(insertbackground="black")
        self.Entry_Pwd.configure(selectbackground="#c4c4c4")
        self.Entry_Pwd.configure(selectforeground="black")
        self.Entry_Pwd.configure(show="*")

        self.Label_Username = tk.Label(self.Frame1)
        self.Label_Username.place(relx=0.095, rely=0.063, height=40, width=52)
        self.Label_Username.configure(activebackground="#f9f9f9")
        self.Label_Username.configure(activeforeground="black")
        self.Label_Username.configure(background="#d9d9d9")
        self.Label_Username.configure(disabledforeground="#a3a3a3")
        self.Label_Username.configure(font="-family {Microsoft YaHei UI} -size 10")
        self.Label_Username.configure(foreground="#000000")
        self.Label_Username.configure(highlightbackground="#d9d9d9")
        self.Label_Username.configure(highlightcolor="black")
        self.Label_Username.configure(text='''用户名''')

        self.Label_Name = tk.Label(self.Frame1)
        self.Label_Name.place(relx=0.095, rely=0.254, height=40, width=42)
        self.Label_Name.configure(activebackground="#f9f9f9")
        self.Label_Name.configure(activeforeground="black")
        self.Label_Name.configure(background="#d9d9d9")
        self.Label_Name.configure(disabledforeground="#a3a3a3")
        self.Label_Name.configure(font="-family {Microsoft YaHei UI} -size 10")
        self.Label_Name.configure(foreground="#000000")
        self.Label_Name.configure(highlightbackground="#d9d9d9")
        self.Label_Name.configure(highlightcolor="black")
        self.Label_Name.configure(text='''姓名''')

        self.Label_Pwd = tk.Label(self.Frame1)
        self.Label_Pwd.place(relx=0.095, rely=0.413, height=50, width=42)
        self.Label_Pwd.configure(activebackground="#f9f9f9")
        self.Label_Pwd.configure(activeforeground="black")
        self.Label_Pwd.configure(background="#d9d9d9")
        self.Label_Pwd.configure(disabledforeground="#a3a3a3")
        self.Label_Pwd.configure(font="-family {Microsoft YaHei UI} -size 10")
        self.Label_Pwd.configure(foreground="#000000")
        self.Label_Pwd.configure(highlightbackground="#d9d9d9")
        self.Label_Pwd.configure(highlightcolor="black")
        self.Label_Pwd.configure(text='''密码''')

        self.Label_Pwd_Comfirm = tk.Label(self.Frame1)
        self.Label_Pwd_Comfirm.place(relx=0.063, rely=0.603, height=50, width=62)

        self.Label_Pwd_Comfirm.configure(activebackground="#f9f9f9")
        self.Label_Pwd_Comfirm.configure(activeforeground="black")
        self.Label_Pwd_Comfirm.configure(background="#d9d9d9")
        self.Label_Pwd_Comfirm.configure(disabledforeground="#a3a3a3")
        self.Label_Pwd_Comfirm.configure(font="-family {Microsoft YaHei UI} -size 10")
        self.Label_Pwd_Comfirm.configure(foreground="#000000")
        self.Label_Pwd_Comfirm.configure(highlightbackground="#d9d9d9")
        self.Label_Pwd_Comfirm.configure(highlightcolor="black")
        self.Label_Pwd_Comfirm.configure(text='''确认密码''')

        self.Entry_Pwd_Comfirm = tk.Entry(self.Frame1)
        self.Entry_Pwd_Comfirm.place(relx=0.286, rely=0.635, height=34
                , relwidth=0.616)
        self.Entry_Pwd_Comfirm.configure(background="white")
        self.Entry_Pwd_Comfirm.configure(disabledforeground="#a3a3a3")
        self.Entry_Pwd_Comfirm.configure(font="-family {黑体} -size 13")
        self.Entry_Pwd_Comfirm.configure(foreground="#000000")
        self.Entry_Pwd_Comfirm.configure(highlightbackground="#d9d9d9")
        self.Entry_Pwd_Comfirm.configure(highlightcolor="black")
        self.Entry_Pwd_Comfirm.configure(insertbackground="black")
        self.Entry_Pwd_Comfirm.configure(selectbackground="#c4c4c4")
        self.Entry_Pwd_Comfirm.configure(selectforeground="black")
        self.Entry_Pwd_Comfirm.configure(show="*")

        self.Label_PW = tk.Label(self.Frame1)
        self.Label_PW.place(relx=0.026, rely=0.825, height=40, width=130)
        self.Label_PW.configure(activebackground="#f9f9f9")
        self.Label_PW.configure(activeforeground="black")
        self.Label_PW.configure(background="#d9d9d9")
        self.Label_PW.configure(disabledforeground="#a3a3a3")
        self.Label_PW.configure(font="-family {Microsoft YaHei UI} -size 10")
        self.Label_PW.configure(foreground="#000000")
        self.Label_PW.configure(highlightbackground="#d9d9d9")
        self.Label_PW.configure(highlightcolor="black")
        self.Label_PW.configure(text='''管理员码（用户为空）''')

        self.Entry_PW = tk.Entry(self.Frame1)
        self.Entry_PW.place(relx=0.47, rely=0.825,height=34, relwidth=0.437)
        self.Entry_PW.configure(background="white")
        self.Entry_PW.configure(disabledforeground="#a3a3a3")
        self.Entry_PW.configure(font="-family {黑体} -size 13")
        self.Entry_PW.configure(foreground="#000000")
        self.Entry_PW.configure(highlightbackground="#d9d9d9")
        self.Entry_PW.configure(highlightcolor="black")
        self.Entry_PW.configure(insertbackground="black")
        self.Entry_PW.configure(selectbackground="#c4c4c4")
        self.Entry_PW.configure(selectforeground="black")
        
        self.Button_Register = tk.Button(top)
        self.Button_Register.place(relx=0.338, rely=0.872, height=40, width=105)
        self.Button_Register.configure(activebackground="#ececec")
        self.Button_Register.configure(activeforeground="#000000")
        self.Button_Register.configure(background="#d9d9d9")
        self.Button_Register.configure(disabledforeground="#a3a3a3")
        self.Button_Register.configure(font="-family {Microsoft YaHei UI} -size 10")
        self.Button_Register.configure(foreground="#000000")
        self.Button_Register.configure(highlightbackground="#d9d9d9")
        self.Button_Register.configure(highlightcolor="black")
        self.Button_Register.configure(pady="0")
        self.Button_Register.configure(command=self.regist)
        self.Button_Register.configure(text='''注册''')
        self.Entry_Username.focus()
    def regist(self):
        DB=db.Db()
        flag=True
        info={'uname':self.Entry_Username.get(),'name':self.Entry_Name.get()
                ,'pwd':self.Entry_Pwd.get(),'pwdre':self.Entry_Pwd_Comfirm.get()}
        for i in info.values():
            if i=='':
                flag=False
        if flag==False:
            tk.messagebox.showinfo('错误',message='信息不能为空',parent=self.top)
            self.Entry_Username.focus()
        elif info['pwd'] != info['pwdre']:
            tk.messagebox.showinfo('错误',message='两次密码不一致',parent=self.top)
            self.Entry_Pwd_Comfirm.focus()

        else:
            type=''
            if self.Entry_PW.get() == "123":
                type='admin'
            elif self.Entry_PW.get() != "":
                tk.messagebox.showinfo('错误', message='请填写正确的注册码', parent=self.top)
                self.Entry_PW.focus()
            else:
                type='user'
            user=info['uname'],info['name'],info['pwd']
            if DB.regist(user,type)== False:
                tk.messagebox.showinfo('错误',message='用户名已存在',parent=self.top)
                self.Entry_Username.focus()
            else:
                print('用户',user[0],'注册成功')
                tk.messagebox.showinfo('成功',message='注册成功')
                self.top.destroy()
