
import csv
from questions import *
from os import listdir
clean = lambda s : ''.join([c for c in s.strip() if c.isalpha() or c == ' '])

results_file = 'results.csv'

files = [f for f in listdir('.') if f.endswith('.csv') and f != results_file]

wrows = [['site', 'question', 'category', 'answer']]

for f in files:
	qlookup = hits[f.replace('.csv', '')]
	questions = [(q, get_cat(question_ids[q.lower()])) for q in qlookup] 
	with open(f, 'r') as rfile:
		reader = csv.DictReader(rfile)
		for row in reader:
			answers = [i for i in row.items() if i[0].startswith('Answer.el')]
			answers = sorted(answers, key = lambda a : int(a[0].replace('Answer.el', '')) )
			for q, a in zip (questions, answers):
				a = int(a[1]) if len(a[1]) > 0 else 0

				wrows.append([clean(f.replace('.csv', '')), q[0], q[1], a ])

with open(results_file ,'w') as wfile:
	writer = csv.writer(wfile)
	for r in wrows:
		writer.writerow(r)

