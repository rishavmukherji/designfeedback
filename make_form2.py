
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

questions = {
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


cat_header = "<h3> [cat] </h3> <hr> "
question = """
   <div>
   		<h4> [q] </h4>
        <ul class="likert">
            <li class="likert"> <label for = "[id]-1"> Strongly disagree</label> <input id = "[id]-1" name="[id]" type="radio" value="1" />
            <li class="likert"> <label for = "[id]-2"> Disagree</label> <input id = "[id]-2" name="[id]" type="radio" value="2" />
            <li class="likert"> <label for = "[id]-3"> Neutral</label> <input id = "[id]-3" name="[id]" type="radio" value="3" />
            <li class="likert"> <label for = "[id]-4"> Agree</label> <input id = "[id]-4" name="[id]" type="radio" value="4" />
            <li class="likert"> <label for = "[id]-5"> Strongly agree</label> <input id = "[id]-5" name="[id]" type="radio" value="5" />
        </ul>
    </div>
"""

counter = 0
s = ''
for cat, ids in categories.iteritems():
	s += cat_header.replace('[cat]', cat)
	for qid in ids:
		s += question.replace('[q]', questions[qid]).replace('[id]', 'el%s' % counter)
		s += '</br>'
		counter += 1
	s += '</br>'

print s


