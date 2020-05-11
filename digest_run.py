import pandas as pd
import xlsxwriter
from digest_parse import df

# Write df to_excel with xlsxwriter
writer = pd.ExcelWriter('./output/new_output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='April 2020', startrow=1, index=False)

# Add in template header
	##TODO

# Get the xlsxwriter objects from the dataframe writer object.
workbook  = writer.book
worksheet = writer.sheets['April 2020']

#format column widths and row eights
worksheet.set_row(1, 40)

worksheet.set_column(0, 0, 25)   # Column B width set to 20
worksheet.set_column(1, 2, 12)   # Column C & D width set to 12
worksheet.set_column(3, 4, 9)   # etc.
worksheet.set_column(5, 5, 10.5)
worksheet.set_column(6, 6, 8)
worksheet.set_column(7, 10, 6)

# Set Formats
_account_info = workbook.add_format()
_account_info.set_bg_color('#D9D9DA')
_account_info.set_bold()
_account_info.set_border()
worksheet.write('A2', 'Account Name', _account_info)
worksheet.write('B2', 'Account Code', _account_info)
worksheet.write('C2', 'Account Monthly Quota', _account_info)

# Save File
writer.save()