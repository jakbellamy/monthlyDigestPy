import pandas as pd
import xlsxwriter
from digest_parse import df

writer = pd.ExcelWriter('new_output.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='April 2020')

writer.save()