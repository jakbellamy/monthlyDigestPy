
def format_sheet(workbook, sheet, data_len):
	
	# Set Column styles
	col_one_style = workbook.add_format()
	col_one_style.set_bold()
	sheet.set_column(0, 0, 25, col_one_style)

	col_heights = [ [1, 2, 12], [3, 4, 9], [5, 6, 10.5], [7, 7, 8], [8, 10, 6], [11, 11, 5], [12, 13, 7.2], [14, 14, 6], [15, 16, 10], [17, 17, 8.3], [18, 21, 9] ]
	for col_ran in col_heights: # loops through defined column ranges and width values and sets to sheet
		sheet.set_column(col_ran[0], col_ran[1], col_ran[2])
		

	#Set Row Styles
	sheet.set_row(1, 40)

	def header_style(color, align="center"):
		style = workbook.add_format()
		style.set_bg_color(color)
		style.set_bold()
		style.set_border()
		style.set_text_wrap()
		style.set_align(align)
		return style

	#Row One Headers
	sheet.merge_range('A1:D1', '', header_style('#FFFFFF'))
	sheet.merge_range('E1:F1', 'Direct Mail', header_style('#FE0300'))
	sheet.merge_range('G1:S1', 'Email', header_style('#91D04F'))
	sheet.merge_range('T1:V1', 'Direct Mail Rejects', header_style('#8DB4E1'))

	#Row Two Group One Headers
	sheet.write('A2', 'Account Name', header_style('#D9D9DA', 'left'))
	sheet.write('B2', 'Account Code', header_style('#D9D9DA'))
	sheet.write('C2', 'Account Monthly Quota', header_style('#D9D9DA'))

	#Row Two Group Three Headers
	sheet.write('D2', 'Total Leads Submitted', header_style('#BFBFBF'))
	sheet.write('E2', 'DM Leads Submitted', header_style('#BFBFBF'))
	sheet.write('F2', 'DM Pieces Deployed', header_style('#BFBFBF'))

	#Row Two Group Four Headers
	sheet.write('G2', 'Email Leads Submitted', header_style('#808080'))
	sheet.write('H2', 'Emails Deployed', header_style('#808080'))
	sheet.write('I2', 'Open Rate', header_style('#808080'))
	sheet.write('J2', 'Email Opens', header_style('#808080'))
	sheet.write('K2', 'CTR', header_style('#808080'))
	sheet.write('L2', 'Email Clicks', header_style('#808080'))
	sheet.write('M2', 'Email Bounces', header_style('#808080'))
	sheet.write('N2', 'Bounce Rate', header_style('#808080'))
	sheet.write('O2', 'Unsub-\nscribes', header_style('#808080'))
	sheet.write('P2', 'Unsubscribe Rate', header_style('#808080'))
	sheet.write('Q2', 'Email Complaints', header_style('#808080'))
	sheet.write('R2', 'Complaint Rate', header_style('#808080'))
	sheet.write('S2', 'Email Duplicates', header_style('#808080'))
	sheet.write('T2', 'CASS Failure', header_style('#808080'))
	sheet.write('U2', 'Internal Duplicates', header_style('#808080'))
	sheet.write('V2', 'Dupe with Prior Batch', header_style('#808080'))
