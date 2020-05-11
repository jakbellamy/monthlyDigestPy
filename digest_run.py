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

worksheet.set_column(0, 0, 25)   # Account name
worksheet.set_column(1, 2, 12)   # Account code and Quota
worksheet.set_column(3, 4, 9)   # Total Leads and DM Leads
worksheet.set_column(5, 6, 10.5)	# DM Pieces and Email Leads
worksheet.set_column(7, 7, 8)	# emails deployed
worksheet.set_column(8, 10, 6)	# open rate - ctr
worksheet.set_column(11, 11, 5)	# email clicks
worksheet.set_column(12, 13, 7.2) 	# email bounces - bounce rate
worksheet.set_column(14, 14, 6) 	# unsubscribes
worksheet.set_column(15, 17, 10) 	# unsubscribe rate - complaint rate
worksheet.set_column(18, 21, 9) 	# unsubscribe rate - complaint rate

# Set Formats
_account_info = workbook.add_format()
_account_info.set_bg_color('#D9D9DA')
_account_info.set_bold()
_account_info.set_border()
worksheet.write('A2', 'Account Name', _account_info) # written before center align and wrap
_account_info.set_align('center')
_account_info.set_text_wrap()
worksheet.write('B2', 'Account Code', _account_info)
worksheet.write('C2', 'Account Monthly Quota', _account_info)

_stats_1 = workbook.add_format()
_stats_1.set_bg_color('#BFBFBF')
_stats_1.set_bold()
_stats_1.set_border()
_stats_1.set_text_wrap()
_stats_1.set_align('center')
worksheet.write('D2', 'Total Leads Submitted', _stats_1)
worksheet.write('E2', 'DM Leads Submitted', _stats_1)
worksheet.write('F2', 'DM Pieces Deployed', _stats_1)

_stats_2 = workbook.add_format()
_stats_2.set_bg_color('#808080')
_stats_2.set_bold()
_stats_2.set_border()
_stats_2.set_text_wrap()
_stats_2.set_align('center')
worksheet.write('G2', 'Email Leads Submitted', _stats_2)
worksheet.write('H2', 'Emails Deployed', _stats_2)
worksheet.write('I2', 'Open Rate', _stats_2)
worksheet.write('J2', 'Email Opens', _stats_2)
worksheet.write('K2', 'CTR', _stats_2)
worksheet.write('L2', 'Email Clicks', _stats_2)
worksheet.write('M2', 'Email Bounces', _stats_2)
worksheet.write('N2', 'Bounce Rate', _stats_2)
worksheet.write('O2', 'Unsub-\nscribes', _stats_2)
worksheet.write('P2', 'Unsubscribe Rate', _stats_2)
worksheet.write('Q2', 'Email Complaints', _stats_2)
worksheet.write('R2', 'Email Duplicates', _stats_2)
worksheet.write('S2', 'CASS Failure', _stats_2)
worksheet.write('T2', 'Internal Duplicates', _stats_2)
worksheet.write('U2', 'Dupe with Prior Batch', _stats_2)
# Save File
writer.save()