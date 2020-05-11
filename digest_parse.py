import pandas as pd

column_titles = ['Account Name', 'Account Code', 'Account Monthly Quota',
				'Total Leads Submitted', 'DM Leads Submitted', 'DM Leads Submitted',
				'Email Leads Submitted', 'Emails Deployed', 'Open Rate', 'Email Opens',
				'CTR', 'Email Clicks', 'Email Bounces', 'Bounce Rate', 'Unsubscribes',
				'Unsubscribe Rate', 'Email Complaints', 'Email Duplicates', 'CASS Failure',
				'Internal Duplicate', 'Dupe with Prior Batch'
				]


def parse_dfs(counts, locations):
	column_names = ['Account Name']
	new_df = pd.DataFrame(columns = column_names)
	for i, row in counts.iterrows():
		location = locations[locations['UserName'] == counts.at[i, 'UserName']]
		new_row = { # end early in order to self ref
			'Account Name': location['Account'].values[0] if len(location['Account'].values) > 0 else 'EMPTY VALUE',
			'Account Code': counts.at[i, 'UserName'],
			'Account Monthly Quota': location['Quota'].values[0] if len(location['Quota'].values) > 0 else 'EMPTY VALUE',
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
		
	return new_df.reindex(columns=column_titles)
