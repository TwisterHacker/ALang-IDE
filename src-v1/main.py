import os
import time
from tkinter import *
from tkinter import filedialog, Text
from tkinter import messagebox
from tkinter import ttk

import pygments.lexers as lex
from pygments.token import Token

win1 = Tk()
win1.geometry("800x600+100+100")
win1.title("ALang IDE 5")
win1.minsize(width=800, height=600)

# win1.iconbitmap('ico.ico')


numbers = Text(win1, width=4, bg='lightgray', state=DISABLED, relief=FLAT)
numbers.grid(row=0, column=0, sticky='NS')

scroll = ttk.Scrollbar(win1)
scroll.grid(row=0, column=2, sticky='NS')


def on_yscrollcommand(*args):
    scroll.set(*args)  # Синхронизация скролбара с текстовым полем
    numbers.yview_moveto(args[0])  # Синхронизация поля с номерами с текстовым полем


text: Text = Text(win1, yscrollcommand=on_yscrollcommand, wrap=NONE)
text.grid(row=0, column=1, sticky='NSWE')

text.insert(END, 'START')


def scroll_command(*args):
    # Движение скролбара управляет отображением текста в обоих текстовых полях
    text.yview(*args)
    numbers.yview(*args)


scroll.config(command=scroll_command)


def insert_numbers():
    count_of_lines = text.get(1.0, END).count('\n') + 1

    numbers.config(state=NORMAL)
    numbers.delete(1.0, END)
    numbers.insert(1.0, '\n'.join(map(str, range(1, count_of_lines))))
    numbers.config(state=DISABLED)


insert_numbers()

# Нужно чтобы текстовое поле автоматически меняло размер при изменении размера окна
win1.grid_columnconfigure(1, weight=1)
win1.grid_rowconfigure(0, weight=1)

try:
    conf2 = open("/last_opened.txt", "r")
    file1 = conf2.read()
    try:
        file2 = open(file1)
        fileText2 = file2.read()
        text.insert(1.0, fileText2)
    except:
        pass
except:
    pass

###################################

menu = Menu(win1)

win1.config(menu=menu)

first_menu = Menu(menu)


def new_file_e(event):
    if messagebox.askyesno("File saving", "Save data?"):
        save_file()
        text.delete(1.0, END)
    else:
        text.delete(1.0, END)


def new_file():
    if messagebox.askyesno("File saving", "Save data?"):
        save_file()
        text.delete(1.0, END)
    else:
        text.delete(1.0, END)


def open_file():
    if messagebox.askyesno("File saving", "Save data?"):
        save_file()
        text.delete(1.0, END)
    else:
        text.delete(1.0, END)
    try:
        file = filedialog.askopenfilename()
        f = open(file)
        filetext = f.read()
        text.insert(1.0, filetext)
        conf2 = open("/last_opened.txt", "w")
        conf2.write(file)
        conf2.close()
        time.sleep(1)
        global file1_1_read
        file1_1 = open('/last_opened.txt')  # this var is for last menu bar
        file1_1_read = file1_1.read()
    except:
        messagebox.showerror("Error", "File read error")


def save_file_as():
    try:
        global save_as
        save_as = filedialog.asksaveasfilename()
        print(save_as)
        txt = text.get(1.0, END)
        f = open(save_as, "w")
        f.write(txt)
        f.close()
    except:
        pass


def save_file():
    txt = text.get(1.0, END)
    try:
        f = open(save_as, "w")
        f.write(txt)
        f.close()
    except:
        save_file_as()


def save_file_e(event):
    save_file()


def open_file_e(event):
    open_file()


def save_file_as_e(event):
    txt = text.get(1.0, END)
    try:
        f = open(save_as, "w")
        f.write(txt)
        f.close()
    except:
        save_file_as()


def close_win():
    if messagebox.askyesno("File saving", "Save data?"):
        save_file()
        win1.destroy()
    else:
        win1.destroy()


menu.add_cascade(label=" File ", menu=first_menu)
first_menu.add_command(label="New file", command=new_file)
first_menu.add_command(label="Open file", command=open_file)
first_menu.add_command(label="Save file as", command=save_file_as)
first_menu.add_command(label="Save file", command=save_file)
first_menu.add_command(label="Exit", command=close_win)

###################################

fourth_menu = Menu(menu)


def undo():
    try:
        text.edit_undo()
    except:
        pass


def redo():
    try:
        text.edit_redo()
    except:
        pass


menu.add_cascade(label=" Edit ", menu=fourth_menu)
fourth_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: text.event_generate('<<Copy>>'))
fourth_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: text.event_generate('<<Cut>>'))
fourth_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: text.event_generate('<<Paste>>'))
fourth_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=lambda: text.event_generate('<<Undo>>'))
fourth_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=lambda: text.event_generate('<<Redo>>'))

###################################

second_menu = Menu(menu)
menu.add_cascade(label=" Viev ", menu=second_menu)


def change_font():
    text.config(font="Arial 13")
    numbers.config(font="Century 13")


def change_font_1():
    text.config(font="Algerian 13")
    numbers.config(font="Century 13")


def change_font_2():
    text.config(font="Century 13")
    numbers.config(font="Century 13")


def light_t():
    text.config(fg="gray25")
    numbers.config(fg="gray25")
    text.config(bg="light gray")
    conf4 = open("/theme.txt", "w")
    numbers.config(bg="light gray")
    conf4.write("light")
    conf4.close()


def dark_t1():
    text.config(fg="#ecf0f1")
    numbers.config(fg="#ecf0f1")
    text.config(bg="#222")
    conf3 = open("/theme.txt", "w")
    numbers.config(bg="#333")
    conf3.write("dark1")
    conf3.close()


def winter_t():
    text.config(fg="cornflower blue")
    numbers.config(fg="cornflower blue")
    text.config(bg="alice blue")
    conf6 = open("/theme.txt", "w")
    numbers.config(bg="alice blue")
    conf6.write("winter")
    conf6.close()


def brown():
    text.config(fg="#f4f4f4")
    numbers.config(fg="#f4f4f4")
    text.config(bg="#303020")
    numbers.config(bg="#332")
    conf5 = open("/theme.txt", "w")
    conf5.write("brown")
    conf5.close()


def black():
    text.config(fg="#fff")
    text.config(bg="#000")
    numbers.config(bg="#000")
    numbers.config(fg="#fff")
    conf1 = open("/theme.txt", "w")
    conf1.write("black")
    conf1.close()


second_menu.add_command(label="Font Arial 13", command=change_font)
second_menu.add_command(label="Font Algerian 13", command=change_font_1)
second_menu.add_command(label="Font Century 13", command=change_font_2)
second_menu.add_command(label="Light Theme", command=light_t)
second_menu.add_command(label="Dark Theme", command=dark_t1)
second_menu.add_command(label="Winter Theme", command=winter_t)
second_menu.add_command(label="Brown Theme", command=brown)
second_menu.add_command(label="Black Theme", command=black)


#

def run():
    this_file = open("/last_opened.txt")
    this_file_text = this_file.read()
    try:
        try:
            os.system("cls")
        except:
            os.system("clear")
        os.system("alang0.1.exe " + this_file_text)
    except:
        messagebox.showerror("Error", "ALang not installed")
    this_file.close()


def run_e(event):
    run()


run_menu = Menu(menu)
menu.add_cascade(label="Run", accelerator="F5", menu=run_menu)
run_menu.add_command(label="Run", command=run)


#
def doc():
    messagebox.showinfo("ALang IDE Documentation",
                        "Ctrl+S - Save\nCtrl+O - Open\nCtrl+N - New file\nThemes : Light, Dark, Winter, Black, Brown, \nFonts : Arial, Algerian, Century")


def email():
    messagebox.showinfo("E-Mail", "Not Aviable")


def other():
    messagebox.showinfo("TextEdit", "Not Aviable")


third_menu = Menu(menu)
menu.add_cascade(label=" Documentation ", menu=third_menu)
third_menu.add_command(label="Documentation", command=doc)
third_menu.add_command(label="E-Mail", command=email)
third_menu.add_command(label="Other programs", command=other)

win1.bind("<Control-o>", open_file_e)
win1.bind("<Control-n>", new_file_e)
win1.bind("<Control-s>", save_file_e)
win1.bind("<Control-S>", save_file_as_e)
win1.bind("<Control-z>", undo)
win1.bind("<Control-y>", redo)
win1.bind("<F5>", run_e)

conf = open("/theme.txt", "r")

theme_f = conf.read()

if theme_f == "light":
    light_t()
if theme_f == "dark1":
    dark_t1()
if theme_f == "winter":
    winter_t()
if theme_f == "brown":
    brown()
if theme_f == "black":
    black()

# Last menu

file1_1 = open('/last_opened.txt')

file_name = Menu(menu)
menu.add_cascade(label=" Last opened : " + file1_1.read(), menu=file_name)

# Last menu

# PYTHON

lexer = lex.load_lexer_from_file('alang.py', 'ALang')

# Создаем теги с разными свойствами, которые будем присваивать соответствующим типам токенов
text.tag_config('Keywords', foreground='#E03270')
text.tag_config("Punctuation", foreground="#ddd")
text.tag_config("Text", foreground="#777")
text.tag_config("String", foreground="#545441")
text.tag_config("Operator", foreground="#F72870")
text.tag_config("Comment", foreground="#76705E")
text.tag_config("Var", foreground="#67D7EB")
text.tag_config("Bool", foreground="#AE82FE")
text.tag_config("Numbers", foreground="#AE82FE")
text.tag_config("Keyword", foreground="#AE82FE")
# Прописываем соответствие типа токена тегу подсветки
token_type_to_tag = {
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


# PYTHON

def get_text_coord(s: str, i: int):
    """
    Из индекса символа получить "координату" в виде "номер_строки_текста.номер_символа_в_строке"
    """
    for row_number, line in enumerate(s.splitlines(keepends=True), 1):
        if i < len(line):
            return f'{row_number}.{i}'

        i -= len(line)


def on_edit(event):
    # Удалить все имеющиеся теги из текста
    for tag in text.tag_names():
        text.tag_remove(tag, 1.0, END)

    # Разобрать текст на токены
    s = text.get(1.0, END)
    tokens = lexer.get_tokens_unprocessed(s)

    for i, token_type, token in tokens:
        j = i + len(token)
        if token_type in token_type_to_tag:
            text.tag_add(token_type_to_tag[token_type], get_text_coord(s, i), get_text_coord(s, j))
    # Срабатывает при изменениях в текстовом поле
    insert_numbers()
    text.edit_modified(0)  # Сбрасываем флаг изменения текстового поля

    # Сбросить флаг редактирования текста
    text.edit_modified(0)


# OTHER

text.bind('<<Modified>>', on_edit)

text.grid(row=0, column=1, sticky='NSWE')

win1.mainloop()
