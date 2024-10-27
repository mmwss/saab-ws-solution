import re

def parse_comment(parser):
    comment_match = re.match(r"<!--(.*?)-->", parser.html[parser.position:], re.DOTALL)
    if comment_match:
        comment_content = comment_match.group(1).strip()
        parser.output['comments'].append(comment_content)
        parser.position += comment_match.end()
    else:
        # Added: Handling for unclosed comments
        end_of_comment = parser.html.find("-->", parser.position)
        if end_of_comment == -1:
            end_of_comment = len(parser.html)
        parser.output['comments'].append(parser.html[parser.position + 4:end_of_comment].strip())
        parser.position = end_of_comment + 3
