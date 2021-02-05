import re

with open('to_scrape.txt') as f:
    content = f.read()

"""
ToDos

regex for phone numbers
regex for email addresses
text off the clipboard
extract email/phone from the text

"""

phoneRegex = re.compile(r"""
                        ()\d{3})

                        """, re.VERBOSE)
