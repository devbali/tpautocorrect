with open("wordsbyfrequency","r") as f:
	allwords = f.read().split("\n")

allalph = list("aeiounwtpsjklm")
vowels = list("aeiou")
consonants = list("wtpsjklm")

# This is a dictionary for a list of toki pona keys each key could be a mistake
# in place of. So r: e,t means a person entering r could actually mean e or t
horizontals = {
	"q":["w"],
	"w":["e"],
	"e":["w"],
	"r":["e","t"],
	"t":[],
	"y":["u","t"],
	"u":["i"],
	"i":["u","o"],
	"o":["p","i"],
	"p":["o"],
	"a":["s"],
	"s":["a"],
	"d":["s"],
	"f":[],
	"g":[],
	"h":["j"],
	"j":["k"],
	"k":["l","j"],
	"l":["k"],
	"z":[],
	"x":[],
	"c":[],
	"v":[],
	"b":["n"],
	"n":["m"],
	"m":["n"]
	}

# Recursive function that returns an array of all word combos a word could mean
def possible_strs (string,prev="n"):
	if string == "": return [""] # Base case for recursion
	if len(string) > 7: string = string[:7] # Dont want to end up with massive arrays

	letters = [] # What the first letter could mean
	hor = horizontals[string[0]]

	# Letters likelihood is the letter entered, horizontals, or nothing
	if string[0] in allalph:
		letters.append(string[0])
	for i in hor:
		if i in vowels and prev not in vowels or prev not in consonants and i not in vowels:
			letters.append(i)
	letters.append("") # current letter might be a mistake

	strings = []
	for letter in letters:
		for s in possible_strs(string[1:],prev=letter):
			strings.append(letter+s)
	return strings

# Looks for toki pona words in those possible strings
def autocorrect (string):
	words = possible_strs(string)
	suggestions = []
	for word in words:
		# First choice is if the string is an exact match
		# Second is if the string exactly starts a toki pona word
		if word in allwords and word not in suggestions:
			suggestions.append(word)
			continue

		for tpword in allwords:
			if len(tpword) > len(word) and tpword[:len(word)] == word and tpword not in suggestions:
				suggestions.append(tpword)
		if len(suggestions) >= 3: break
	return suggestions[:3]

# MAIN function provides console based testing for the algorithm
while True:
	searchtext = input("Enter a phrase (quit for quit): ")
	if searchtext == "quit": break
	else: print(",".join(autocorrect(searchtext)))
