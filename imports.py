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

def filter_dates(df, period):
	for i, row in df.iterrows():
		if type(df.at[i, 'DateAdded']) == str:
			sp_date = df.at[i, 'DateAdded'].split(' ')[0].split('/')
			mon_yr = sp_date[0] + sp_date[2]
			df.at[i, 'DateAdded'] = mon_yr
	return df[df['DateAdded'] == period]

#cur_col = filter_dates(collection, '52020')
#print(cur_col)

###COUNTS###

def build_new_df():
	column_names = ['Account Name']
	new_df = pd.DataFrame(columns = column_names)
	for i, row in counts.iterrows():
		location = locations[locations['UserName'] == counts.at[i, 'UserName']]
		new_row = { # end early in order to self ref
			'Account Name': location['Account'],
			'Account Code': counts.at[i, 'UserName'],
			'Account Monthly Quota': location['Quota'],
			'Total Leads Submitted': int(counts.at[i, 'ArchiveTotal']),
			'Email Leads Submitted': int(counts.at[i, 'ArchiveEmailTotal']),
			'Email Duplicates': 'TODO',
			'CASS Failure': 'TODO',
			'Internal Duplicate': 'TODO',
			'Dupe with Prior Batch': 'TODO'
		}
		new_row['DM Leads Submitted'] = new_row['Total Leads Submitted'] - new_row['Email Leads Submitted']
		new_row['Emails Deployed'] = int(counts.at[i, 'SentTotal']) if type(counts.at[i, 'SentTotal']) == int else 0
		new_row['Email Opens'] = int(counts.at[i, 'OpenTotal']) if type(counts.at[i, 'OpenTotal']) == int else 0
		new_row['Email Clicks'] = int(counts.at[i, 'ClickTotal']) if type(counts.at[i, 'ClickTotal']) == int else 0
		new_row['Email Bounces'] = int(counts.at[i, 'BounceTotal']) if type(counts.at[i, 'BounceTotal']) == int else 0
		new_row['Unsubscribes'] = int(counts.at[i, 'UnsubTotal']) if type(counts.at[i, 'UnsubTotal']) == int else 0
		new_row['Email Complaints'] = int(counts.at[i, 'ComplaintTotal']) if type(counts.at[i, 'ComplaintTotal']) == int else 0

		new_df = new_df.append(new_row, ignore_index=True)
		
	return new_df

df = build_new_df()
df.to_excel("output.xlsx") 
print(df)