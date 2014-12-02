hits = {'andrew3' : [
'I found myself in situations where I could not go back to a previous state',
"Similar websites I've used before for the same purpose have helped me understand how to use this one.",
"This website was very different from some others I've used to do the same thing, so it was hard to understand how to do things.",
"The website used very technical terminology that I had trouble understanding",
"The information was presented logically, and I could understand what it meant",
"The website used vocabulary familiar to me",
"The website's information was convoluted and too technical for me to understand",
],
'andrew2' : [
"I was asked if I was sure about doing something that would make a change",
"I could understand what the website was doing",
"I found it difficult to understand what was going on",
"The website was cluttered, and I often had difficulty figuring out what to do next",
"I could navigate the website easily, and didn't see anything unnecessary",
"I ran into problems, and the website did not help me figure out how to fix it",
"I was able to easily navigate the website, undoing actions if necessary",
],
'andrew1' : [
"I had to give the website the same information multiple times to get it to do something",
"I could understand how to do what I wanted to without trouble",
"I could not figure out how to do something, and the website would not help me",
"If I needed help, the website presented it to me in a way that I could understand",
"I could find helpful information on the website if I couldn't understand something",
"The website often did not act as I thought it would",
"I found I could navigate the website without any problems"
],

"conference1" : [
"I had to give the website the same information multiple times to get it to do something",
"I could understand how to do what I wanted to without trouble",
"I could not figure out how to do something, and the website would not help me",
"If I needed help, the website presented it to me in a way that I could understand",
"I could find helpful information on the website if I couldn't understand something",
"The website often did not act as I thought it would",
"I found I could navigate the website without any problems"
],

"conference3" : [
"I found myself in situations where I could not go back to a previous state",
"Similar websites I've used before for the same purpose have helped me understand how to use this one.",
"This website was very different from some others I've used to do the same thing, so it was hard to understand how to do things.",
"The website used very technical terminology that I had trouble understanding",
"The information was presented logically, and I could understand what it meant",
"The website used vocabulary familiar to me",
"The website's information was convoluted and too technical for me to understand"
],

'conference2' : [
"I was asked if I was sure about doing something that would make a change",
"I could understand what the website was doing",
"I found it difficult to understand what was going on",
"The website was cluttered, and I often had difficulty figuring out what to do next",
"I could navigate the website easily, and didn't see anything unnecessary",
"I ran into problems, and the website did not help me figure out how to fix it",
"I was able to easily navigate the website, undoing actions if necessary",
],

'scratchpad1' : [
"I found myself in situations where I could not go back to a previous state",
"Similar websites I've used before for the same purpose have helped me understand how to use this one.",
"This website was very different from some others I've used to do the same thing, so it was hard to understand how to do things.",
"The website used very technical terminology that I had trouble understanding",
"The information was presented logically, and I could understand what it meant",
"The website used vocabulary familiar to me",
"The website's information was convoluted and too technical for me to understand"
],

'scratchpad3' : [
"I was asked if I was sure about doing something that would make a change",
"I could understand what the website was doing",
"I found it difficult to understand what was going on",
"The website was cluttered, and I often had difficulty figuring out what to do next",
"I could navigate the website easily, and didn't see anything unnecessary",
"I ran into problems, and the website did not help me figure out how to fix it",
"I was able to easily navigate the website, undoing actions if necessary",
],

'scratchpad2' : [
"I had to give the website the same information multiple times to get it to do something",
"I could understand how to do what I wanted to without trouble",
"I could not figure out how to do something, and the website would not help me",
"If I needed help, the website presented it to me in a way that I could understand",
"I could find helpful information on the website if I couldn't understand something",
"The website often did not act as I thought it would",
"I found I could navigate the website without any problems"
]
}


categories = {
"Visibility of System Status" : [0,1],
"Match between System and the Real World" : [2,3,4,5],
"User control and Freedom" : [6,7],
"Error Prevention" : [8,9,10,11],
"Recognition rather than recall" : [12,13,14,15],
"Aesthetic and Minimalist Design" : [16,17],
"Help Users Recognize, Diagnose, and Recover from Errors" : [18,19],
"Help and Documentation" : [20,21,22,23],
"Consistency and Standard" : [24, 25],
}

def get_cat(qid):
	for cat, ids in categories.iteritems():
		if qid in ids:
			return cat

question_ids = {
0 : "I could understand what the website was doing ",
1 : "I found it difficult to understand what was going on ",
2 : "The website used very technical terminology that I had trouble understanding",
3 : "The information was presented logically, and I could understand what it meant",
4 : "The website used vocabulary familiar to me ",
5 : "The website's information was convoluted and too technical for me to understand",
6 : "I was able to easily navigate the website, undoing actions if necessary",
7 : "I found myself in situations where I could not go back to a previous state",
8 : "The website often did not act as I thought it would",
9 : "I found I could navigate the website without any problems",
10 : "I was asked if I was sure about doing something that would make a change",
11 : "The website changed my information without asking me about it",
12 : "I had to give the website the same information multiple times to get it to do something",
13 : "The website remembered the information I gave it, so I didn't have to input it again",
14 : "I could understand how to do what I wanted to without trouble",
15 : "I could not figure out how to do something, and the website would not help me ",
16 : "The website was cluttered, and I often had difficulty figuring out what to do next ",
17 : "I could navigate the website easily, and didn't see anything unnecessary",
18 : "If I had a problem, the website helped me fix it quickly and efficiently",
19 : "I ran into problems, and the website did not help me figure out how to fix it",
20 : "If I needed help, the website presented it to me in a way that I could understand ",
21 : "I could find helpful information on the website if I couldn't understand something ",
22 : "I needed help with something, but I didn't see a way for the website to help me ",
23 : "I could not understand what the website was telling me to do when I needed help ",
24 : "Similar websites I've used before for the same purpose have helped me understand how to use this one.",
25 : "This website was very different from some others I've used to do the same thing, so it was hard to understand how to do things."
}
question_ids = {v.strip().lower() : k for k, v in question_ids.items()}

reverse =  {
"The website used vocabulary familiar to me" : 1,
"The website's information was convoluted and too technical for me to understand" : -1,
"I was asked if I was sure about doing something that would make a change" : 1,
"The website used very technical terminology that I had trouble understanding" : -1,
"I found I could navigate the website without any problems" : 1,
"I ran into problems, and the website did not help me figure out how to fix it" : -1,
"I found it difficult to understand what was going on" : -1,
"I was able to easily navigate the website, undoing actions if necessary" : 1,
"I had to give the website the same information multiple times to get it to do something" : -1,
"Similar websites I've used before for the same purpose have helped me understand how to use this one." : 1,
"I found myself in situations where I could not go back to a previous state" : -1,
"The information was presented logically, and I could understand what it meant" : 1,
"This website was very different from some others I've used to do the same thing, so it was hard to understand how to do things." : -1,
"I could understand how to do what I wanted to without trouble" : 1,
"I could not figure out how to do something, and the website would not help me" : -1,
"I could find helpful information on the website if I couldn't understand something" : 1,
"I could understand what the website was doing" : 1,
"If I needed help, the website presented it to me in a way that I could understand" : 1,
"The website often did not act as I thought it would" : -1, 
"I could navigate the website easily, and didn't see anything unnecessary" : 1,
"The website was cluttered, and I often had difficulty figuring out what to do next" : -1
}



