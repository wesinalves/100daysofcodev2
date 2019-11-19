# Python Journey - Chapter 23
# Tabulates population and number of census tracts for
# each county.

import openpyxl, pprint
print('Opening workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
county_data = {}

# TODO: Fill in countyData with each county's population and tracts.
