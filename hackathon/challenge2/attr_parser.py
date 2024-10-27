import re
from html import unescape

def parse_attributes(attributes_string):
    attr_matches = re.findall(r'([a-zA-Z]+)="(.*?)"', attributes_string)
    # Added: Capture unquoted attributes like checked or disabled
    attr_matches += re.findall(r'([a-zA-Z]+)(?=\s|$)', attributes_string)
    return {key: unescape(value) if value else key for key, value in attr_matches}
