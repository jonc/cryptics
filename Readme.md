# Required python packages:

	nose
	web
	nltk

# Other requirements:

	python (tested with 2.7)
	rake
	git

# Installation:

Add the cryptics folder to your PYTHONPATH. Then generate the n-grams and synonyms datasets by running

	rake data

in the main cryptics folder (this will take a few minutes to finish). 

# Usage:

Web interface: http://localhost:8080/

	rake server

Test cases (requires the python nose package):

	rake test

# Clue format:

Clue:

	Initially babies are naked (4)

Answer:

	BARE

Clue: 

	Lees horse galloping to dangerous_coasts (3,6) l.....r..

Answer: 

	LEE_SHORES

You can give the solver a hint that a set of words form a phrase (and need not be treated separately) by combining them with an underscore (as in 'dangerous_coasts' above). 

