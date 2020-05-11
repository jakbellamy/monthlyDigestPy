def format_sheet(workbook, sheet):
	#format column widths and row eights
	sheet.set_row(1, 40)

	sheet.set_column(0, 0, 25)   # Account name
	sheet.set_column(1, 2, 12)   # Account code and Quota
	sheet.set_column(3, 4, 9)   # Total Leads and DM Leads
	sheet.set_column(5, 6, 10.5)	# DM Pieces and Email Leads
	sheet.set_column(7, 7, 8)	# emails deployed
	sheet.set_column(8, 10, 6)	# open rate - ctr
	sheet.set_column(11, 11, 5)	# email clicks
	sheet.set_column(12, 13, 7.2) 	# email bounces - bounce rate
	sheet.set_column(14, 14, 6) 	# unsubscribes
	sheet.set_column(15, 17, 10) 	# unsubscribe rate - complaint rate
	sheet.set_column(18, 21, 9) 	# unsubscribe rate - complaint rate

	# Set Formats
	_account_info = workbook.add_format()
	_account_info.set_bg_color('#D9D9DA')
	_account_info.set_bold()
	_account_info.set_border()

	sheet.write('A2', 'Account Name', _account_info) # written before center align and wrap
	_account_info.set_align('center')
	_account_info.set_text_wrap()
	sheet.write('B2', 'Account Code', _account_info)
	sheet.write('C2', 'Account Monthly Quota', _account_info)

	_stats_1 = workbook.add_format()
	_stats_1.set_bg_color('#BFBFBF')
	_stats_1.set_bold()
	_stats_1.set_border()
	_stats_1.set_text_wrap()
	_stats_1.set_align('center')
	sheet.write('D2', 'Total Leads Submitted', _stats_1)
	sheet.write('E2', 'DM Leads Submitted', _stats_1)
	sheet.write('F2', 'DM Pieces Deployed', _stats_1)

	_stats_2 = workbook.add_format()
	_stats_2.set_bg_color('#808080')
	_stats_2.set_bold()
	_stats_2.set_border()
	_stats_2.set_text_wrap()
	_stats_2.set_align('center')
	sheet.write('G2', 'Email Leads Submitted', _stats_2)
	sheet.write('H2', 'Emails Deployed', _stats_2)
	sheet.write('I2', 'Open Rate', _stats_2)
	sheet.write('J2', 'Email Opens', _stats_2)
	sheet.write('K2', 'CTR', _stats_2)
	sheet.write('L2', 'Email Clicks', _stats_2)
	sheet.write('M2', 'Email Bounces', _stats_2)
	sheet.write('N2', 'Bounce Rate', _stats_2)
	sheet.write('O2', 'Unsub-\nscribes', _stats_2)
	sheet.write('P2', 'Unsubscribe Rate', _stats_2)
	sheet.write('Q2', 'Email Complaints', _stats_2)
	sheet.write('R2', 'Email Duplicates', _stats_2)
	sheet.write('S2', 'CASS Failure', _stats_2)
	sheet.write('T2', 'Internal Duplicates', _stats_2)
	sheet.write('U2', 'Dupe with Prior Batch', _stats_2)
	