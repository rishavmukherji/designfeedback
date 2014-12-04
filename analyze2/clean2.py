import csv
from os import listdir
clean = lambda s : ''.join([c for c in s.strip() if c.isalpha() or c == ' '])

results_file = 'results2.csv'
exclude = ['comments.csv']

files = [f for f in listdir('.') if f.endswith('.csv') and f != results_file and f not in exclude]

wrows = [['site', 'category', 'comment']]


site_comments = {}

for f in files:
	comments = []
	with open(f, 'r') as rfile:
		reader = csv.DictReader(rfile)
		for row in reader:
			answers = [i for i in row.items() if i[0].startswith('Answer.') and i[0] != 'Answer.comments' and len(i[0].replace('Answer.', '')) > 5]
			for a in answers:
				if len(a[1]) > 3:
					wrows.append([f, a[0].replace('Answer.', ''), a[1]])


			if 'Answer.comments' in row and row['Answer.comments']:
				comments.append(row['Answer.comments'])

			
	site_comments[f.replace('.csv', '')] = comments


with open(results_file ,'w') as wfile:
	writer = csv.writer(wfile)
	for r in wrows:
		writer.writerow(r)

with open('comments.csv', 'w') as wfile:
	writer = csv.writer(wfile)
	for k, all_comments in site_comments.items():
		for c in all_comments:
			writer.writerow([k, c])