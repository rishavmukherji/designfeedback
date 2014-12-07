import csv, json
import numpy as np
from scipy.stats import sem
from collections import defaultdict
from questions import *

def verification():
	with open('../analyze/worker_scores.csv', 'r') as rfile:

	
def first_chart():

	scores = {}
	with open('../analyze/worker_scores.csv', 'r') as rfile:
		sreader = csv.reader(rfile)
		sreader.next()
		for row in sreader:
			scores[row[0]] = int(row[1])


	with open('../analyze/results.csv', 'rU') as rfile:
		reader = csv.DictReader(rfile)
		rows = [r for r in reader]

	questions = defaultdict(list)
	categories = {}
	cdata = defaultdict(list)

	experiments = ['andrew']#, 'conference', 'scratchpad' ]

	for e in experiments:

		for r in rows:
			if r['site'].startswith(e):
				hit_worker = r['site'] + str(r['hit']) + '-' + r['worker']
				score = scores[hit_worker] if hit_worker in scores else 0

				if score >= 1:
					questions[r['question']].append(int(r['answer']))
					categories[r['question']] = r['category']

		for q, v in questions.items():
			to_reverse = reverse[q] < 0
			# avg = np.mean([a for a in v if a > 0])
			# avg = 6 - avg if to_reverse else avg

			for a in v:
				cdata[categories[q]].append(6 - a if to_reverse else a)

			#cdata[categories[q]].append(avg)


		data = {"xScale": "ordinal", "yScale": "linear", 'xMin' : 0, 'xMax' : 5}
		categories = defaultdict(list)


		comp = {''}
		points = []
		for c, answers in cdata.items():
			print answers
			points.append({'x' : c, 'y' : np.mean(answers), 'e' : sem(answers) })

		main = [{'className' : '.errorExample', 'data' : points}]
		comp = [{'type' : 'error', 'className' : '.comp.errorBar', 'data' : points}]

		data.update({'main' : main, 'comp' : comp})

		open('%s.json' % e, 'w').write(json.dumps(data))

		













