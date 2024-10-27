"""
The Journey of a Developer Handbook,
an essential resource for developers,
has been corrupted during a recent system update.
Critical content—headers, paragraphs,
and links—has been scrambled and is no longer readable
due to a broken HTML parser.

Your task is to debug the parser that was
hastily written and left with numerous bugs.
The parser struggles with self-closing tags,
nested elements, and unclosed comments,
leaving the handbook in an unusable state.

Fix the parser to restore the handbook,
making it fully readable again.
"""

GROUP_NUMBER = 1 # Change this to your group number
# To test this challenge, only run this file (main.py).
# DO NO MODIFY ANYTHING BEYOND THIS POINT

import pretty_errors
from load_html import load_html
from html_parser import HTMLParser
from utils import render

if __name__ == "__main__":
    html_content = load_html(f"data/haikus/{GROUP_NUMBER}.html")

    parser = HTMLParser(html_content)
    parsed_output = parser.parse()

    render(parsed_output)
