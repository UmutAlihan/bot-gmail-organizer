import sys
import click

#(1)Source: https://stackoverflow.com/questions/20063/whats-the-best-way-to-parse-command-line-arguments
#(2)Source: https://www.youtube.com/watch?v=SDyHLG2ltSY (click watch)
#(3)Source: https://www.youtube.com/watch?v=gR73nLbbgqY (tools for cli)
#(4)Source: https://www.youtube.com/watch?v=hJhZhLg3obk

#print(len(sys.argv))
#print()

args = sys.argv[1:]
#args = sys.argv

"""if(len(args) > 0):
	print("ok")
else:
	print("not enough args")"""

#print(type(args[0]))

#for arg in args:
#	print(arg)


print("username: " + args[0])
print("queries: " + "".join(args[1:-1]))
print("labelname: " + "".join(args[-1]))
