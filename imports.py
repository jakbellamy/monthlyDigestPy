import pandas as pd

collection = pd.read_csv('./extensions/ARCHIVE_Supreme_Collection_DE20200506.csv')
counts = pd.read_csv('./extensions/Archive_CountsByUser20200506.csv')
locations = pd.read_csv('./extensions/Supreme_Locations20200508.csv')

#	method to determine what kind of mail the record is
def is_dm(record): #	seems to be working but throws error if record doesn't have att. 'Address1'
	if record['Address1']:
		return True
	else:
		return 'Sorry'

def parse_dates(df):
	for ind in df.index:
		sp_date = df['DateAdded'][ind].split(' ')[0].split('/')
		month = '0' + sp_date[0] if len(sp_date[0]) < 2 else sp_date[0]
		year = sp_date[2]
		df['DateAdded'][ind] = year + month
	return df

#fil_collection = parse

print(parse_dates(collection.head()))


