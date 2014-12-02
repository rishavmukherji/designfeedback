import csv
import numpy as np
from collections import defaultdict
from questions import *

with open('results.csv', 'rU') as rfile:
	reader = csv.DictReader(rfile)
	rows = [r for r in reader]

questions = defaultdict(list)
categories = {}
cdata = defaultdict(list)

experiments = ['andrew', 'conference', 'scratchpad' ]

for e in experiments:
	print e

	for r in rows:
		if r['site'].startswith(e):
			questions[r['question']].append(int(r['answer']))

			categories[r['question']] = r['category']

	for q, v in questions.items():
		to_reverse = reverse[q] < 0
		avg = np.mean([a for a in v if a > 0])
		avg = 6 - avg if to_reverse else avg

		print '"%s","%s",%.2f' % (categories[q], q, avg)
		cdata[categories[q]].append(avg)


	for k, v in cdata.items():
		print '"%s","%s",%.2f' % (k, 'Mean', np.mean(v))












