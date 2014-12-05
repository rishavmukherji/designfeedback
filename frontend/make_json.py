import csv
import json


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



