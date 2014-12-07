import csv
import json
import numpy as np
from scipy.stats import sem
from collections import defaultdict


scores = {}
with open('../analyze/worker_scores.csv', 'r') as rfile:
	sreader = csv.reader(rfile)
	sreader.next()
	for row in sreader:
		scores[row[0]] = int(row[1])


rows = []
with open('../analyze/results.csv', 'r') as rfile:
	rreader = csv.DictReader(rfile)

	for r in rreader:
		hit_worker = r['site'] + str(r['hit']) + '-' + r['worker']
		score = scores[hit_worker] if hit_worker in scores else 0
		r.update({'wscore' : score})

		r['hit'] = int(r['hit'])
		r['worktime'] = int(r['worktime'])
		r['answer'] = int(r['answer'])

		rows.append(r)

open('results.json', 'w').write(json.dumps(rows, indent = 4))



for experiment in ['andrew']:#, 'conference', 'scratchpad']:

	data = {"xScale": "ordinal", "yScale": "linear", 'xMin' : 0, 'xMax' : 5}
	categories = defaultdict(list)

	for row in rows:
		if row['site'] == experiment:
			categories[row['category']].append(row['answer'])

		
		comp = {''}
		points = []
		for c, answers in categories.items():
			points.append({'x' : c, 'y' : np.mean(answers), 'e' : sem(answers) })

		main = [{'className' : '.errorExample', 'data' : points}]
		comp = [{'type' : 'error', 'className' : '.comp.errorBar', 'data' : points}]

	data.update({'main' : main, 'comp' : comp})

	print data




# var data = {

#     "main": [
#       {
#         "className": ".errorExample",
#         "data": [
#           {
#             "x": "Consistency and Standards",
#             "y": 12
#           },
#           {
#             "x": "Unicorns",
#             "y": 23
#           },
#           {
#             "x": "Trolls",
#             "y": 5
#           }
#         ]
#       }
#     ],
#     "comp": [
#       {
#         "type": "error",
#         "className": ".comp.errorBar",
#         "data": [
#           {
#             "x": "Consistency and Standards",
#             "y": 12,
#             "e": 5
#           },
#           {
#             "x": "Unicorns",
#             "y": 23,
#             "e": 2
#           },
#           {
#             "x": "Trolls",
#             "y": 5,
#             "e": 1
#           }
#         ]
#       }
#     ]
#   };