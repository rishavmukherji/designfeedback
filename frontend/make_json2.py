import csv, json
import numpy as np
import pylab as plt
from scipy.stats import sem
from collections import defaultdict
from questions import *

def main():
	check_mean()

vquestions = {
	'conference-q1' : 'Who is the president of the Executive Board?',
	'conference-q2' : 'When was the last event organized by this organization?',
	'conference-q4' : 'Try and register for the upcoming conference in India. What is the "Form Name" shown when you try to register? (Don\'t worry, your registrations for the conference won\'t be accepted):',

	'scratchpad-q1' : 'Who is the faculty advisor of the Harvard Cricket Club?',
	'scratchpad-q2' :'How many people are listed in the alumni section of the club?',
	'scratchpad-q4' :'Who scored more runs in the Harvard vs UPenn game on Saturday, Sep 21?',

	'andrew-q1' : 'Who is the publisher for The Success Equation',
	'andrew-q2' : 'What email address should send any questions or feedback relating to the site to?',
	'andrew-q4' : 'If player 1 has a 51% chance of winning one point, what is the probability they will win a five set match (use the tennis simulation page)?',
}


def check_mean():
	with open('../analyze/results.csv', 'rU') as rfile:
		reader = csv.DictReader(rfile)
		rows = [r for r in reader]
	workers = defaultdict(list)
	for r in rows:
		workers[r['worker']].append(int(r['answer']))

	means = [np.mean(v) for v in workers.values()]
	print len(means)
	print np.std(means)
	print len([m for m in means if m >= 2.5 and m <= 3.5])
	plt.hist(means, bins = 20, color = '#262626')
	plt.show()

def verification():
	with open('../analyze/verification_results.csv', 'r') as rfile:
		vreader = csv.DictReader(rfile)
		rows = [r for r in vreader]

	questions = defaultdict(list)
	for r in rows:
		questions[r['site'] + '-' + r['question']].append(int(r['correct']))

	aggregate = defaultdict(list)

	for q,responses in questions.items():

		aggregate[q.split('-')[0]].append({'question' : vquestions[q], 'correct' : float('%.2f' % np.mean(responses)), 'total' : len(responses)})

	print json.dumps(aggregate)



def first_chart():

	min_score = 1

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

				if score >= min_score:
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

		

main()





