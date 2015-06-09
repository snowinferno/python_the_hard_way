from random import randint
from random import choice

# randomly select a truth table to work on
# then randomly select an expression to prevent rote answering

NOT_TABLE = {
	"not False": True,
	"not True": False
}

OR_TABLE = {
	"True or False": True or False,
	"True or True": True or True,
	"False or True": False or True,
	"False or False": False or False
}

AND_TABLE = {
	"True and False": True and False,
	"True and True": True and True,
	"False and True": False and True,
	"False and False": False and False
}

NOT_OR_TABLE = {
	"not (True or False)": not (True or False),
	"not (True or True)": not (True or True),
	"not (False or True)": not (False or True),
	"not (Flase or False)": not (False or False)
}

NOT_AND_TABLE = {
	"not (True and False)": not (True and False),
	"not (True and True)": not (True and True),
	"not (False and True)": not (False and True),
	"not (False and False)": not (False and False)

}

NOT_EQUAL_TABLE = {
	"1 != 0": 1 != 0,
	"1 != 1": 1 != 1,
	"0 != 1": 0 != 1,
	"0 != 0": 0 != 0
}

EQUAL_TABLE = {
	"1 == 0": 1 == 0,
	"1 == 1": 1 == 1,
	"0 == 1": 0 == 1,
	"0 == 0": 0 == 0
}

TABLES = [NOT_TABLE, OR_TABLE, AND_TABLE, NOT_OR_TABLE, NOT_AND_TABLE, NOT_EQUAL_TABLE, EQUAL_TABLE]

correct = 0
total = len(NOT_TABLE) + len(OR_TABLE) + len(AND_TABLE) + len(NOT_OR_TABLE) + len(NOT_AND_TABLE) + len(NOT_EQUAL_TABLE) + len(EQUAL_TABLE)

while len(TABLES) > 0:
	index = randint(0,len(TABLES)-1)
	table = TABLES[index]
	expression = choice(list(table.keys()))
	answer = raw_input("What is the value of `%s`? " % expression)
	if answer.lower() == str(table[expression]).lower():
		correct += 1
		print "Very good! `%s` is indeed `%s`." % (expression, table[expression])
	else:
		print "Incorrect. `%s` is actually `%s`." % (expression, table[expression])
	print ""
	del table[expression]
	if len(table) < 1:
		del TABLES[index]
#	while len(table) > 0:
#		expression = choice(list(table.keys()))
#		answer = raw_input("What is the value of `%s`? " % expression)
#		if answer.lower() == str(table[expression]).lower():
#			correct += 1
#			print "Very good! `%s` is indeed `%s`." % (expression, table[expression])
#		else:
#			print "Incorrect. `%s` is actually `%s`" % (expression, table[expression])
#		print ""
#		del table[expression]
##	for expression in table:
##		answer = raw_input("What is the value of `%s`? " % expression)
##		if answer.lower() == str(table[expression]).lower():
##			correct += 1
##			print "Very good! `%s` is indeed `%s`." % (expression, table[expression])
##		else:
##			print "Incorrect. `%s` is actually `%s`" % (expression, table[expression])
##		print ""
#	del TABLES[index]
else:
	print "Your socre is %d / %d: %f%%" % (correct, total, (float(correct) / float(total) * 100))
