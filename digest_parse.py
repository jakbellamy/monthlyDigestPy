import pandas as pd
import math

column_titles = [
 	'Account Name', 'Account Code', 'Account Monthly Quota', 'Total Leads Submitted', 'DM Leads Submitted', 'DM Leads Submitted', 
 	'Email Leads Submitted', 'Emails Deployed', 'Open Rate', 'Email Opens', 'CTR', 'Email Clicks', 'Email Bounces', 'Bounce Rate', 
 	'Unsubscribes', 'Unsubscribe Rate', 'Email Complaints', 'Email Duplicates', 'CASS Failure', 'Internal Duplicate', 'Dupe with Prior Batch'
]

def hanlde_NaN(val):
	return int(val) if math.isnan(val) == False else 0

def parse_dfs(counts, locations):
	column_names = ['Account Name']
	new_df = pd.DataFrame(columns = column_names)
	for i, row in counts.iterrows():
		location = locations[locations['UserName'] == counts.at[i, 'UserName']]
		new_row = {
			'Account Name': location['Account'].values[0] if len(location['Account'].values) > 0 else 'EMPTY VALUE',
			'Account Code': counts.at[i, 'UserName'],
			'Account Monthly Quota': location['Quota'].values[0] if len(location['Quota'].values) > 0 else 0,
			'Total Leads Submitted': int(counts.at[i, 'ArchiveTotal']),
			'Email Leads Submitted': int(counts.at[i, 'ArchiveEmailTotal']),
			'Emails Deployed': hanlde_NaN(counts.at[i, 'SentTotal']),
			'Email Opens': hanlde_NaN(counts.at[i, 'OpenTotal']),
			'Email Clicks': hanlde_NaN(counts.at[i, 'ClickTotal']),
			'Email Bounces': hanlde_NaN(counts.at[i, 'BounceTotal']),
			'Unsubscribes': hanlde_NaN(counts.at[i, 'UnsubTotal']),
			'Email Complaints': hanlde_NaN(counts.at[i, 'ComplaintTotal']),
			'DM Leads Submitted': int(counts.at[i, 'ArchiveTotal']) - int(counts.at[i, 'ArchiveEmailTotal']),
			'Email Duplicates': 'TODO',  #  Need to be sent the new data extension first
			'CASS Failure': 'TODO',  #  Need to be sent the new data extension first
			'Internal Duplicate': 'TODO',  #  Need to be sent the new data extension first
			'Dupe with Prior Batch': 'TODO'  #  Need to be sent the new data extension first
		}

		new_df = new_df.append(new_row, ignore_index=True)
		
	return new_df.reindex(columns=column_titles)
