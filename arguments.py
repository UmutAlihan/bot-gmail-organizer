import sys


#(1)Source: https://stackoverflow.com/questions/20063/whats-the-best-way-to-parse-command-line-arguments

#print(len(sys.argv))

args = sys.argv[1:]


"""if(len(args) > 0):
	print("ok")
else:
	print("not enough args")"""

print(type(args[0]))