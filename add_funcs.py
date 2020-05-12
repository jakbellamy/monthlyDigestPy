import pandas as pd
import xlsxwriter
from add_styles import format_sheet

total_cols = ['C', 'D', 'E', 'F', 'G', 'H', 'J', 'L', 'M', 'O', 'Q', 'S', 'T', 'U', 'V']

def build_table(workbook, sheet, data_len):
	def total_style():
		style = workbook.add_format()
		style.set_top()
		style.set_bold()
		return style

	format_sheet(workbook, sheet, data_len)

	sheet.write(f'A{data_len + 3}', 'Total')

	def insert_total(col):
		formula = f'=SUM({col}{3}:{col}{data_len + 2})'
		row_pos = f'{col}{data_len + 3}'
		sheet.write_formula(row_pos, formula)

	for col in total_cols:
		insert_total(col)

	percent_fmt = workbook.add_format({'num_format': '0%'})

	def calc_percent(col, row, top_var, bottom_var):
		top = f'{top_var}{row}'
		bot = f'{bottom_var}{row}'
		pos = f'{col}{row}'
		formula = f'=IF({bot}=0,{top},{top}/{bot})'
		sheet.write_formula(pos, formula, percent_fmt)


	for row in range(3, data_len+4):
		calc_percent('I', row, 'J', 'H')
		calc_percent('K', row, 'L', 'J')
		calc_percent('N', row, 'M', 'H')
		calc_percent('P', row, 'O', 'H')
		calc_percent('R', row, 'Q', 'H')


	t_row = data_len + 2
	sheet.set_row(t_row, 15, total_style())