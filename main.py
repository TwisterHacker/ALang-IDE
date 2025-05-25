from tkinter import *
from tkinter import Text, filedialog, messagebox, simpledialog, ttk

import pygments.lexers as lex
from pygments.token import Token


def get_text_coord(s: str, i: int):
    """
    Из индекса символа получить "координату" в виде "номер_строки_текста.номер_символа_в_строке"
    """
    for row_number, line in enumerate(s.splitlines(keepends=True), 1):
        if i < len(line):
            return f'{row_number}.{i}'

        i -= len(line)


class ide(object):
    def on_yscrollcommand(self, *args):
        self.scroll.set(*args)  # Синхронизация скролбара с текстовым полем
        self.numbers.yview_moveto(args[0])  # Синхронизация поля с номерами с текстовым полем

    def scroll_command(self, *args):
        # Движение скролбара управляет отображением текста в обоих текстовых полях
        self.text.yview(*args)
        self.numbers.yview(*args)

    def insert_numbers(self):
        count_of_lines = self.text.get(1.0, END).count('\n') + 1

        self.numbers.config(state=NORMAL)
        self.numbers.delete(1.0, END)
        self.numbers.insert(1.0, '\n'.join(map(str, range(1, count_of_lines))))
        self.numbers.config(state=DISABLED)

    def closeWin(self):
        if messagebox.askyesno("File saving", "Save data?"):
            self.save_file()
            self.win1.destroy()
        else:
            self.win1.destroy()

    def newFile_e(self, event):
        if messagebox.askyesno("File saving", "Save data?"):
            self.saveFile()
            self.text.delete(1.0, END)
        else:
            self.text.delete(1.0, END)

    def newFile(self):
        if messagebox.askyesno("File saving", "Save data?"):
            self.saveFile()
            self.text.delete(1.0, END)
        else:
            self.text.delete(1.0, END)

    def new_file_e(self, event):
        self.newFile()

    def openFile(self):
        if messagebox.askyesno("File saving", "Save data?"):
            self.saveFile()
            self.text.delete(1.0, END)
        else:
            self.text.delete(1.0, END)
        try:
            file = filedialog.askopenfilename()
            f = open(file)
            filetext = f.read()
            self.text.insert(1.0, filetext)
            conf2 = open("/last_opened.txt", "w")
            conf2.write(file)
            conf2.close()
            global file1_1_read
            file1_1 = open('/last_opened.txt')  # this var is for last menu bar
            file1_1_read = file1_1.read()
        except:
            messagebox.showerror("Error", "File read error")

    def open_file_e(self, event):
        self.openFile()

    def saveFileAs(self):
        try:
            global save_as
            save_as = filedialog.asksaveasfilename()
            print(save_as)
            txt = self.text.get(1.0, END)
            f = open(save_as, "w")
            f.write(txt)
            f.close()
        except:
            pass

    def save_file_as_e(self, event):
        self.saveFileAs()

    def saveFile(self):
        txt = self.text.get(1.0, END)
        try:
            f = open(save_as, "w")
            f.write(txt)
            f.close()
        except:
            self.saveFileAs()

    def save_file_e(self, event):
        self.saveFile()

    def find(self):  # find text
        edit = simpledialog.askstring("Find", "Search string")
        self.text.tag_remove("found", "1.0", END)
        if edit:
            idx = "1.0"
            while 1:
                idx = self.text.search(edit, idx, nocase=1, stopindex=END)
                if not idx:
                    break
                lastidx = "%s+%dc" % (idx, len(edit))

                self.text.tag_add("found", idx, lastidx)
                idx = lastidx
            self.text.tag_config("found", background="#898989")

    def change_font_size_plus(self, event):
        self.font_size += 1
        self.text.config(font=self.font + " " + str(self.font_size))
        self.numbers.config(font=self.font + " " + str(self.font_size))

    def change_font_size_minus(self, event):
        self.font_size -= 1
        self.text.config(font=self.font + " " + str(self.font_size))
        self.numbers.config(font=self.font + " " + str(self.font_size))

        if self.font_size <= 3:
            self.font_size = 4

    def change_font_style_bold(self, event):
        self.font_style = " bold"

        self.text.config(font=self.font + " " + str(self.font_size) + self.font_style)
        self.numbers.config(font=self.font + " " + str(self.font_size) + self.font_style)

    def change_font_style_normal(self, event):
        self.font_style = " normal"

        self.text.config(font=self.font + " " + str(self.font_size) + self.font_style)
        self.numbers.config(font=self.font + " " + str(self.font_size) + self.font_style)

    def change_font_1(self):
        font = "Arial"
        self.text.config(font=font + " " + str(self.font_size))
        self.numbers.config(font=font + " " + str(self.font_size))

    def change_font_2(self):
        font = '"Times New Roman"'
        self.text.config(font=font + " " + str(self.font_size))
        self.numbers.config(font=font + " " + str(self.font_size))

    def change_font_3(self):
        font = 'Cubest'
        self.text.config(font=font + " " + str(self.font_size))
        self.numbers.config(font=font + " " + str(self.font_size))

    def theme_conf(self, theme):
        conf1 = open("/theme.txt", "w")
        conf1.write(theme)
        conf1.close()

    def light_t(self):
        self.text.tag_config("Keywords", foreground="#006699")
        self.text.tag_config("Punctuation", foreground="#000")
        self.text.tag_config("Text", foreground="#000")
        self.text.tag_config("String", foreground="#D14E22")
        self.text.tag_config("Operator", foreground="#000")
        self.text.tag_config("Comment", foreground="#97D1F7")
        self.text.tag_config("Var", foreground="#CC00FF")
        self.text.tag_config("Bool", foreground="#00CCFF")
        self.text.tag_config("Numbers", foreground="#f76200")
        self.text.tag_config("Keyword", foreground="#AE82FE")

        self.text.config(fg="#000")
        self.numbers.config(fg="gray25")
        self.console.config(fg="#000")
        self.console.config(bg="#F0F3F3", insertbackground="#000")
        self.text.config(bg="#F0F3F3", insertbackground="#000")
        self.numbers.config(bg="#F0F3F3")
        self.theme_conf("light")

        self.win1.config(bg='#F0F3F3')

    def dark_t1(self):
        self.text.tag_config("Keywords", foreground="#5EC4D6")
        self.text.tag_config("Punctuation", foreground="#ddd")
        self.text.tag_config("Text", foreground="#F8F8F2")
        self.text.tag_config("String", foreground="#E6DB74")
        self.text.tag_config("Operator", foreground="#F92672")
        self.text.tag_config("Comment", foreground="#76705E")
        self.text.tag_config("Var", foreground="#67D7EB")
        self.text.tag_config("Bool", foreground="#A6E22E")
        self.text.tag_config("Numbers", foreground="#9D75E5")
        self.text.tag_config("Keyword", foreground="#AE82FE")

        self.text.config(fg="#F8F8F2")
        self.numbers.config(fg="#ecf0f1")
        self.console.config(fg="#F8F8F2")
        self.console.config(bg="#272822", insertbackground="#f8f8f2")
        self.text.config(bg="#272822", insertbackground="#f8f8f2")
        self.numbers.config(bg="#272822")
        self.theme_conf("dark1")
        self.win1.config(bg='#272822')

    def winter_t(self):
        self.text.tag_config("Keywords", foreground="#000080")
        self.text.tag_config("Punctuation", foreground="#000")
        self.text.tag_config("Text", foreground="#000")
        self.text.tag_config("String", foreground="#0000FF")
        self.text.tag_config("Operator", foreground="#000")
        self.text.tag_config("Comment", foreground="#62B562")
        self.text.tag_config("Var", foreground="#000")
        self.text.tag_config("Bool", foreground="#000")
        self.text.tag_config("Numbers", foreground="#5050FF")
        self.text.tag_config("Keyword", foreground="#AE82FE")

        self.text.config(fg="#000")
        self.numbers.config(fg="cornflower blue")
        self.console.config(fg="#000")
        self.console.config(bg="#fff", insertbackground="#000")
        self.text.config(bg="#fff", insertbackground="#000")
        self.numbers.config(bg="#fff")
        self.theme_conf("winter")
        self.win1.config(bg='#fff')

    def material(self):
        self.text.tag_config("Keywords", foreground="#BB80B3 ")
        self.text.tag_config("Punctuation", foreground="#78C0DE")
        self.text.tag_config("Text", foreground="#fff")
        self.text.tag_config("String", foreground="#C3E88D")
        self.text.tag_config("Operator", foreground="#78C0DE")
        self.text.tag_config("Comment", foreground="#76705E")
        self.text.tag_config("Var", foreground="#67D7EB")
        self.text.tag_config("Bool", foreground="#78C0DE")
        self.text.tag_config("Numbers", foreground="#E48367")

        self.text.config(fg="#fff")
        self.numbers.config(fg="#fff")
        self.console.config(fg="#fff")
        self.console.config(bg="#263238", insertbackground="#fff")
        self.text.config(bg="#263238", insertbackground="#fff")
        self.numbers.config(bg="#263238")
        self.theme_conf("material")
        self.win1.config(bg='#263238')

    def vim(self):
        self.text.tag_config("Keywords", foreground="#CDCD00")
        self.text.tag_config("Punctuation", foreground="#3399CC")
        self.text.tag_config("Text", foreground="#777")
        self.text.tag_config("String", foreground="#CD0000")
        self.text.tag_config("Operator", foreground="#3399CC")
        self.text.tag_config("Comment", foreground="#000080")
        self.text.tag_config("Var", foreground="#67D7EB")
        self.text.tag_config("Bool", foreground="#AE82FE")
        self.text.tag_config("Numbers", foreground="#CD00CD")
        self.text.tag_config("Keyword", foreground="#AE82FE")

        self.text.config(fg="#fff")
        self.text.config(bg="#000", insertbackground="#fff")
        self.console.config(fg="#fff")
        self.console.config(bg="#000", insertbackground="#fff")
        self.numbers.config(bg="#000")
        self.numbers.config(fg="#fff")

        self.theme_conf("vim")
        self.win1.config(bg='#000')

    def on_edit(self, event):
        # Удалить все имеющиеся теги из текста
        for tag in self.text.tag_names():
            self.text.tag_remove(tag, 1.0, END)

        # Разобрать текст на токены
        s = self.text.get(1.0, END)
        tokens = self.lexer.get_tokens_unprocessed(s)

        for i, token_type, token in tokens:
            print(i, token_type, repr(token))  # Отладочный вывод - тут видно какие типы токенов выдаются
            j = i + len(token)
            if token_type in self.token_type_to_tag:
                self.text.tag_add(self.token_type_to_tag[token_type], get_text_coord(s, i), get_text_coord(s, j))

        # Срабатывает при изменениях в текстовом поле
        self.insert_numbers()

        self.text.edit_modified(0)  # Сбрасываем флаг изменения текстового поля

        # Сбросить флаг редактирования текста
        self.text.edit_modified(0)


    def __init__(self):
        self.font_size = 13
        self.font_style = 'bold'
        self.font = 'Arial'

        self.win1 = Tk()
        self.win1.geometry("800x600+0+0")
        self.win1.title("ALang IDE 5")
        self.win1.minsize(width=1280, height=728)
        self.win1.rowconfigure(0, weight=1)

        self.win1.grid_rowconfigure(0, weight=1)
        self.win1.grid_rowconfigure(1, weight=999)
        self.win1.grid_rowconfigure(2, weight=2)
        self.win1.grid_columnconfigure(1, weight=1)

        # win1.iconbitmap('ico.ico')

        self.numbers = Text(self.win1, width=4, bg='lightgray', state=DISABLED, relief=FLAT)
        self.numbers.grid(row=1, column=0, sticky='NS')

        self.scroll = ttk.Scrollbar(self.win1)
        self.scroll.grid(row=1, column=2, sticky='NS')
        self.scroll.config(command=self.scroll_command)

        self.console = Text(height=12)  # console widget
        self.console.grid(column=1, row=2, sticky='NSWE')

        self.text = Text(self.win1, yscrollcommand=self.on_yscrollcommand, wrap=NONE)
        self.text.grid(row=1, column=1, sticky='NSWE')

        self.toolbar = Frame(height=25)
        self.toolbar.grid(columnspan=3, column=0, row=0, sticky='NWE')

        self.start_img=PhotoImage(file="images/start.png")
        self.stop_img=PhotoImage(file="images/stop.png")
        self.debug_img=PhotoImage(file="images/debug.png")
        self.search_img=PhotoImage(file="images/search.png")

        self.start = Button(self.toolbar, bg='#fff', bd=0, image=self.start_img).grid(row=0, column=0)
        self.stop = Button(self.toolbar, bg='#fff', bd=0, image=self.stop_img).grid(row=0, column=1)
        self.debug = Button(self.toolbar, bg='#fff', bd=0, image=self.debug_img).grid(row=0, column=2)
        self.search = Button(self.toolbar, bg='#fff', bd=0, image=self.search_img).grid(row=0, column=3)

        self.search_entry = ttk.Entry(self.toolbar)
        self.search_entry.grid(row=0, column=4)

        self.lexer = lex.load_lexer_from_file('alang.py', 'ALang')

        # Создаем теги с разными свойствами, которые будем присваивать соответствующим типам токенов
        self.text.tag_config('Keywords', foreground='#E03270')
        self.text.tag_config("Punctuation", foreground="#ddd")
        self.text.tag_config("Text", foreground="#777")
        self.text.tag_config("String", foreground="#545441")
        self.text.tag_config("Operator", foreground="#F72870")
        self.text.tag_config("Comment", foreground="#76705E")
        self.text.tag_config("Var", foreground="#67D7EB")
        self.text.tag_config("Bool", foreground="#AE82FE")
        self.text.tag_config("Numbers", foreground="#AE82FE")
        self.text.tag_config("Keyword", foreground="#AE82FE")
        # Прописываем соответствие типа токена тегу подсветки
        self.token_type_to_tag = {
            Token.Name.Builtin: "Keywords",
            Token.Punctuation: "Punctuation",
            Token.String: "String",
            Token.Text: "Text",
            Token.Operator: "Operator",
            Token.Comment: "Comment",
            Token.Name.Variable: "Var",
            Token.Name.Variable.Bool: "Bool",
            Token.Number: "Numbers",
            Token.Keyword: "Keyword",
        }

        self.insert_numbers()

        self.menu = Menu(self.win1)

        self.win1.config(menu=self.menu)

        self.firstMenu = Menu(self.menu)
        self.secondMenu = Menu(self.menu)
        self.thirdMenu = Menu(self.menu)

        self.menu.add_cascade(label=" File ", menu=self.firstMenu)
        self.firstMenu.add_command(label="New file", command=self.newFile)
        self.firstMenu.add_command(label="Open file", command=self.openFile)
        self.firstMenu.add_command(label="Save file as", command=self.saveFileAs)
        self.firstMenu.add_command(label="Save file", command=self.saveFile)
        self.firstMenu.add_command(label="Exit", command=self.closeWin)

        self.menu.add_cascade(label=" Edit ", menu=self.secondMenu)
        self.secondMenu.add_command(label="Copy", accelerator="Ctrl+C",
                                    command=lambda: self.text.event_generate('<<Copy>>'))
        self.secondMenu.add_command(label="Cut", accelerator="Ctrl+X",
                                    command=lambda: self.text.event_generate('<<Cut>>'))
        self.secondMenu.add_command(label="Paste", accelerator="Ctrl+V",
                                    command=lambda: self.text.event_generate('<<Paste>>'))
        self.secondMenu.add_command(label="Undo", accelerator="Ctrl+Z",
                                    command=lambda: self.text.event_generate('<<Undo>>'))
        self.secondMenu.add_command(label="Redo", accelerator="Ctrl+Y",
                                    command=lambda: self.text.event_generate('<<Redo>>'))
        self.secondMenu.add_command(label="Find", accelerator="Ctrl+F", command=self.find)

        self.menu.add_cascade(label=" Viev ", menu=self.thirdMenu)
        self.thirdMenu.add_command(label="Arial", command=self.change_font_1)
        self.thirdMenu.add_command(label="Times New Roman", command=self.change_font_2)
        self.thirdMenu.add_command(label="Cubest", command=self.change_font_3)
        self.thirdMenu.add_command(label="Light Theme", command=self.light_t)
        self.thirdMenu.add_command(label="Dark Theme", command=self.dark_t1)
        self.thirdMenu.add_command(label="Winter Theme", command=self.winter_t)
        self.thirdMenu.add_command(label="Material Theme", command=self.material)
        self.thirdMenu.add_command(label="Vim Theme", command=self.vim)

        conf = open("theme.txt")

        theme_f = conf.read()

        if theme_f == "light":
            self.light_t()
        elif theme_f == "dark1":
            self.dark_t1()
        elif theme_f == "winter":
            self.winter_t()
        elif theme_f == "material":
            self.material()
        elif theme_f == "vim":
            self.vim()
        else:
            self.material()

        self.win1.bind("<Control-o>", self.open_file_e)
        self.win1.bind("<Control-n>", self.new_file_e)
        self.win1.bind("<Control-s>", self.save_file_e)
        self.win1.bind("<Control-S>", self.save_file_as_e)
        self.win1.bind("<Control-Up>", self.change_font_size_plus)
        self.win1.bind("<Control-Down>", self.change_font_size_minus)
        self.win1.bind("<Control-b>", self.change_font_style_bold)
        self.win1.bind("<Control-r>", self.change_font_style_normal)
        # self.win1.bind("<F5>", self.run_e)
        # self.win1.bind("<Control-f>", self.find_e)


        self.text.bind('<<Modified>>', self.on_edit)

        self.win1.mainloop()


IDE = ide()
