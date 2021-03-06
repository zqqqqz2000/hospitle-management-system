import hashlib
from tkinter import *
from tkinter import messagebox
from global_var import DBSession
from view.menu import ChoiceMenu
from view.register import Register
from view.tor import Tor
from dao.login import Login as Login_dao


class Login:
    def __init__(self, root: Tk):
        self.root = root
        self.page = Frame(self.root)
        self.page.pack()

        self.root.title('登录')
        self.root.geometry('240x110')

        # 上方空出20px
        padding_top = Frame(self.page, height=20)
        padding_top.pack(side=TOP)

        # 账号Frame
        username_frame = Frame(self.page)
        username_frame.pack(side=TOP)
        username_label = Label(username_frame, text='账号')
        username_label.pack(side=LEFT)
        self.username_var = StringVar()
        username_entry = Entry(username_frame, textvariable=self.username_var)
        username_entry.pack(side=LEFT)

        # 密码Frame
        password_frame = Frame(self.page)
        password_frame.pack(side=TOP)
        password_label = Label(password_frame, text='密码')
        password_label.pack(side=LEFT)
        self.password_var = StringVar()
        password_entry = Entry(password_frame, textvariable=self.password_var, show='*')
        password_entry.pack(side=LEFT)

        # 按钮Frame
        btn_frame = Frame(self.page)
        btn_frame.pack(side=TOP)
        # 注册按钮
        register_btn = Button(btn_frame, text='注册', command=self.register)
        register_btn.pack(side=LEFT, padx=5)
        # 登录按钮
        login_btn = Button(btn_frame, text='登录', command=self.login)
        login_btn.pack(side=LEFT, padx=5)
        # 游客按钮
        tor_btn = Button(btn_frame, text='游客查询', command=self.redirect2tor)
        tor_btn.pack(side=LEFT, padx=5)

    def register(self):
        self.page.destroy()
        Register(self.root)

    def login(self):
        username: str = self.username_var.get()
        password: str = self.password_var.get()
        m = hashlib.md5()
        m.update(password.encode())
        pass_hash = m.hexdigest()
        session = DBSession()
        u = session.query(Login_dao).filter_by(
            username=username,
            password=pass_hash
        ).first()
        if u:
            self.page.destroy()
            ChoiceMenu(self.root)
        else:
            messagebox.showwarning('用户名或密码错误', '请核对用户名或密码!')
        session.close()

    def redirect2tor(self):
        self.page.destroy()
        Tor(self.root)
