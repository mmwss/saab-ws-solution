import re
from html import unescape

def parse_text_content(parser):
    text_match = re.match(r"[^<]+", parser.html[parser.position:])
    if text_match:
        text_content = unescape(text_match.group(0)).strip()
        if parser.tags_stack and text_content:
            current_tag = parser.tags_stack[-1]
            handle_text_content(parser, current_tag, text_content)
        parser.position += text_match.end()

def handle_text_content(parser, current_tag, text_content):
    if current_tag == "h1" or current_tag == "h2":
        parser.output['headers'].append(text_content)
    elif current_tag == "p":
        parser.output['paragraphs'].append(text_content)
    elif isinstance(current_tag, dict) and "a" in current_tag:
        parser.output['links'].append({
            "href": current_tag["a"].get("href", ""),
            "text": text_content
        })
