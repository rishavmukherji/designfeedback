import csv

with open('results2.csv', 'r') as rfile:
	reader = csv.DictReader(rfile)

	rows = [r for r in reader]

rows = sorted(rows, key = lambda r : len(r['comment']), reverse = True )

print '\n'.join(map(lambda r : r['comment'], rows))