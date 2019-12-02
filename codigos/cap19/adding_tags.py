# Python Journey - Chapter 19
# Phone and email extractor from clipboard

import pyperclip
import re


# match all lines in clipboad text
text = str(pyperclip.paste())
lines = text.split("\n")

print(len(lines))
print()

# copy results to clipboard
if len(lines) > 0:
    pyperclip.copy("<br>".join(lines))
    print("Copied para o clipboard")
    print("<br>".join(lines))
else:
    print("No phone or emails are found!")