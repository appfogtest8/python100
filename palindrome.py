# built with python 2.7.5

usersays = raw_input("? ")

s = usersays.replace(' ', '')

slist = list(s)


if len(s) % 2 != 0:
	del slist[len(slist) / 2]


if slist[len(slist):((len(slist) / 2) - 1):-1] == slist[:len(slist) / 2]:
	print("yes")
else:
	print("no")