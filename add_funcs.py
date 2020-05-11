import pandas as pd
import xlsxwriter
from add_styles import format_sheet

def build(book, sheet):
	format_sheet(book, sheet)
	last_row = len(sheet) + 2
	total_row = last_row + 1
	sheet.write_formula('A{total_row}', '=SUM(A3:A{last_row})')