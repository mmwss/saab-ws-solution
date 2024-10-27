import re

emails = """
Contact us at support@example.com or sales@company.org for inquiries. 
You can also reach out to john.doe123@personal-site.net or admin@website.co.uk.
Invalid emails like admin@website, @missingusername.com, or missingatdotcom should be ignored.
"""

# Implement a regex to extract all email addresses from the text above.
email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

phone_numbers = """
(123) 456-7890, 123-456-7890, 123.456.7890, +1-123-456-7890,
123-456-789A, 456-789-0123, (123)456-7890
"""

# Implement a regex to extract all valid phone numbers from the text above.
phone_regex = r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"

urls = """
Here are some useful links: 
- https://www.example.com/page1
- http://sub.domain.org/another-page
- https://bad-url
- http://invalid_domain/page
"""

# Implement a regex to extract all valid URLs from the text above.
url_regex = r"https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9.-]*)*"

dates = """
The following events took place on 12/05/2020, 11-11-2021, and 25-12-2019.
Invalid dates like 5/12/2020 and 12/31/20 should be ignored.
"""

# Implement a regex to extract all valid dates from the text above.
date_regex = r"\b\d{2}[-/]\d{2}[-/]\d{4}\b"

card_numbers = """
Here are some credit card numbers: 1234-5678-9876-5432, 1234567812345678, and 1111 2222 3333 4444.
Make sure to mask them appropriately!
"""

# Implement a regex to mask all credit card numbers in the text above.
card_regex = r"\b(?:\d{4}[-\s]?)\d{4}[-\s]?\d{4}[-\s]?\d{4}\b"

if __name__ == "__main__":
    print("Regex[5]")

    matches = re.findall(email_regex, emails)
    print("Emails: ", matches)

    matches = re.findall(phone_regex, phone_numbers)
    print("Phone numbers: ", matches)

    matches = re.findall(url_regex, urls)
    print("Urls: ", matches)

    matches = re.findall(date_regex, dates)
    print("Dates: ", matches)

    masked_text = re.sub(card_regex, "****-****-****-****", card_numbers)
    print("Card numbers hidden: ", masked_text)
