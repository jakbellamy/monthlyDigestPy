import pandas as pd
import xlsxwriter
from parse_extensions import ex_parser
from add_funcs import build_table

counts = pd.read_csv('./extensions/Archive_CountsByUser20200506.csv') #  Should eventually be supplied in req or queried by FTP
locations = pd.read_csv('./extensions/Supreme_Locations20200508.csv') #  Should eventually be supplied in req or queried by FTP
df = ex_parser(counts, locations)

#split df into asa and asa lite
a_df = df[df['Account Code'].str.contains('SL', na=False)].sort_values(by=['Account Name'])
l_df = df[df['Account Code'].str.contains('QL', na=False)].sort_values(by=['Account Name'])

# Write df to_excel with xlsxwriter
writer = pd.ExcelWriter('./output/new_output.xlsx', engine='xlsxwriter')
a_df.to_excel(writer, sheet_name='ASA', startrow=1, index=False)
l_df.to_excel(writer, sheet_name='ASA Lite', startrow=1, index=False)
workbook  = writer.book

worksheet_asa = writer.sheets['ASA']
worksheet_lite = writer.sheets['ASA Lite']

# format sheets
build_table(workbook, worksheet_asa, len(a_df))
build_table(workbook, worksheet_lite, len(l_df))

#save file and fin.
writer.save()
