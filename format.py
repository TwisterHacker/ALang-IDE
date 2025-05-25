
from pygments.formatters import html
import pygments.lexers as lex
import pygments.styles
import pygments

lexer = lex.load_lexer_from_file('alang.py', 'ALang')
style = pygments.styles.get_style_by_name('material')
formatter_ = html.HtmlFormatter(full=True, style=style)

file_name = input("Enter file dir\n\n")

file = open(file_name)
file_text = file.read()

print(pygments.highlight(file_text, lexer, formatter_))
