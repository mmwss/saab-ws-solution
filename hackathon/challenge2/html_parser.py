from tag_parser import parse_tag, close_tag, process_self_closing_tag
from text_parser import parse_text_content
from comment_parser import parse_comment
from attr_parser import parse_attributes

class HTMLParser:
    def __init__(self, html):
        self.html = html
        self.position = 0
        self.tags_stack = []
        self.output = {
            "title": "",
            "headers": [],
            "paragraphs": [],
            "links": [],
            "comments": []
        }

    def parse(self):
        while self.position < len(self.html):
            if self.html[self.position:].startswith("<!--"):
                parse_comment(self)
            elif self.html[self.position:].startswith("<"):
                parse_tag(self)
            else:
                parse_text_content(self)

        return self.output
