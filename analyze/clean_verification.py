
import csv
from questions import *
from os import listdir
clean = lambda s : ''.join([c for c in s.strip() if c.isalpha() or c == ' '])

results_file = 'verification_results.csv'
exclude = ['means.csv', 'comments.csv', 'results.csv']

files = [f for f in listdir('.') if f.endswith('.csv') and f != results_file and f not in exclude]


fields = ['Answer.q1','Answer.q2','Answer.q4']
answers = { 'andrew' : ['Harvard Business Review Press','andrew@success-equation.com','63'],
'conference' : ['Disha Verma', '16', 'HUII'],
'scratchpad' : ['Blyth', '8', 'Harvard']}

def check_answer(response, answer):
	words = answer.lower().split(' ')
	response = response.lower()
	for w in words:
		if not w in response:
			return False
	return True

wrows = [['site', 'question', 'worker', 'correct']]

site_comments = {}

for f in files:

	with open(f, 'r') as rfile:
		reader = csv.DictReader(rfile)
		for row in reader:
			
			for i, field in enumerate(fields):
				if field in row:
					correct = check_answer(row[field], answers[f.replace('.csv', '')[:-1]][i])
					wrows.append([clean(f.replace('.csv', '')), field.split('.')[1], row['WorkerId'], int(correct) ])


			


with open(results_file ,'w') as wfile:
	writer = csv.writer(wfile)
	for r in wrows:
		writer.writerow(r)

