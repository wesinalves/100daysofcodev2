# Python Journey - Chapter 21
# Rename filenames with american dates to european dates format

import shutil, os, re

# Create a regex that matches files with the American date format.
date_pattern = re.compile(r"""^(.*?)    # all text before the date
                ((0|1)?\d)-             # one or two digits for the month
                ((0|1|2|3)?\d)-         # one or two digits for the day
                ((19|20)\d\d)           # fpur digits for year
                (.*?)$                  # all text after date
                """, re.VERBOSE)

# TODO: Loop over the files in the working directory.
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    # TODO: Skip files without a date.
    if mo == None:
        continue

    # TODO: Get the different parts of the filename.
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)
    
    # TODO: Form the European-style filename.
    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part
    
    # TODO: Get the full, absolute file paths.
    abs_working_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)
    
    # TODO: Rename the files.
    print('Renaming "%s" to "%s"...' % (amer_filename, euro_filename))
    #shutil.move(amerFilename, euroFilename) # uncomment after testing