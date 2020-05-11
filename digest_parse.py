import pandas as pd
import math

column_titles = ['Account Name', 'Account Code', 'Account Monthly Quota',
				'Total Leads Submitted', 'DM Leads Submitted', 'DM Leads Submitted',
				'Email Leads Submitted', 'Emails Deployed', 'Open Rate', 'Email Opens',
				'CTR', 'Email Clicks', 'Email Bounces', 'Bounce Rate', 'Unsubscribes',
				'Unsubscribe Rate', 'Email Complaints', 'Email Duplicates', 'CASS Failure',
				'Internal Duplicate', 'Dupe with Prior Batch'
				]

def persuade_nan(val):
	return int(val) if math.isnan(val) == False else 0


def parse_dfs(counts, locations):
	column_names = ['Account Name']
	new_df = pd.DataFrame(columns = column_names)
	for i, row in counts.iterrows():
		location = locations[locations['UserName'] == counts.at[i, 'UserName']]
		new_row = { # end early in order to self ref
			'Account Name': location['Account'].values[0] if len(location['Account'].values) > 0 else 'EMPTY VALUE',
			'Account Code': counts.at[i, 'UserName'],
			'Account Monthly Quota': location['Quota'].values[0] if len(location['Quota'].values) > 0 else 0,
			'Total Leads Submitted': int(counts.at[i, 'ArchiveTotal']),
			'Email Leads Submitted': int(counts.at[i, 'ArchiveEmailTotal']),
			'Email Duplicates': 'TODO',
			'CASS Failure': 'TODO',
			'Internal Duplicate': 'TODO',
			'Dupe with Prior Batch': 'TODO'
		}
		new_row['DM Leads Submitted'] = new_row['Total Leads Submitted'] - new_row['Email Leads Submitted']
		new_row['Emails Deployed'] = persuade_nan(counts.at[i, 'SentTotal'])
		new_row['Email Opens'] = persuade_nan(counts.at[i, 'OpenTotal'])
		new_row['Email Clicks'] = persuade_nan(counts.at[i, 'ClickTotal'])
		new_row['Email Bounces'] = persuade_nan(counts.at[i, 'BounceTotal'])
		new_row['Unsubscribes'] = persuade_nan(counts.at[i, 'UnsubTotal'])
		new_row['Email Complaints'] = persuade_nan(counts.at[i, 'ComplaintTotal'])

		new_df = new_df.append(new_row, ignore_index=True)
		
	return new_df.reindex(columns=column_titles)
