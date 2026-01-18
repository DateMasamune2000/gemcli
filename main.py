import gem_connection
import os
from rich.markdown import Markdown
from rich.console import Console
from rich.prompt import Prompt

conn = gem_connection.GeminiConnection(url=os.getenv("GEMURL"), key=os.getenv("GEMKEY"))
console = Console(color_system="standard")

while True:
    p = Prompt.ask()
    if p == '':
        break
    elif p[0] == '/':
        if p[1:] == "quit":
            break

    md = Markdown(conn.prompt(p)['text'])
    console.print(md)

