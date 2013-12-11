# built with python 2.7.5

eulogy = raw_input("? ")
x = int(eulogy)
print x


for i in range(1, x):
 if i % 15 == 0:
 	print("fizzbuzz")
 elif i % 3 == 0:
 	print("fizz")
 elif i % 5 == 0:
 	print("buzz")
 else:
 	print(i)