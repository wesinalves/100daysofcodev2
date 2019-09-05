# Python Journey - Chapter 19
# Phone and email extractor from clipboard

import pyperclip
import re

# create a phone regex
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #area code
    (\s|-|\.)?                      #separator
    (\d{3})                         #first 3 digits
    (\s|-|\.)                       #separator
    (\d{4})                         #last 4 digits
    (\s*(ext|x|ext)\s*(\d{2,5}))?   #extension       

)''', re.VERBOSE)  

# create a email regex

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               #username
    @                               #symbol
    [a-zA-Z0-9.-]+                  #domain name
    (\.[a-zA-Z]{2,4})               #dot-something    
)''', re.VERBOSE)

# match all cases in clipboad text
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone += ' x' + groups[8]
    matches.append(phone)

for groups in email_regex.findall(text):
    matches.append(groups[0])

# copy results to clipboard
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied para o clipboard")
    print("\n".join(matches))
else:
    print("No phone or emails are found!")
