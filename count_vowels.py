# built with python 2.7.5

countforvowels = raw_input("? ")
countforvowels = countforvowels.lower()
numberofvowels = (countforvowels.count('a') + countforvowels.count('e') +
				 countforvowels.count('i') + countforvowels.count('o') +
				 countforvowels.count('u'))
print numberofvowels