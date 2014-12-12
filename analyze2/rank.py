import csv, json
from collections import defaultdict

names = {
	'Aesthetic and Minimalist Design' : 'Aesthetic',
	'Consistency and Standard' : 'Consistency',
	'Error Prevention' : 'Error Prevention',
	'Help Users Recognize, Diagnose, and Recover from Errors' : 'Error Recovery',
	'Help and Documentation' : 'Documentation',
	'Match between System and the Real World' : 'Match to Real World',
	'Recognition rather than recall' : 'Recognition',
	'User control and Freedom' : 'User Control',
	'Visibility of System Status' : 'Visibility' 
	}

with open('cricket_comments.csv', 'r') as rfile:
	reader = csv.DictReader(rfile)
	rows = [r for r in reader]


sites = defaultdict(list)
for r in rows:
	r['site'] = r['site'][1:].replace('.csv', '')
	sites[r['site']].append(r)


for site, rows in sites.items():
	rows = sorted(rows, key = lambda r : len(r['comment']), reverse = True )
	print site
	print json.dumps(rows)

#print '\n'.join(map(lambda r : r['comment'], rows))

