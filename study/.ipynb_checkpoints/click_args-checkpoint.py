import sys
import click

#(1)Source: https://stackoverflow.com/questions/20063/whats-the-best-way-to-parse-command-line-arguments
#(2)Source: https://www.youtube.com/watch?v=SDyHLG2ltSY (click watch)
#(3)Source: https://www.youtube.com/watch?v=gR73nLbbgqY (tools for cli)
#(4)Source: https://www.youtube.com/watch?v=hJhZhLg3obk
#(5)Source - Useful: http://zetcode.com/python/click/

#print(len(sys.argv))

#args = sys.argv[1:]

"""if(len(args) > 0):
	print("ok")
else:
	print("not enough args")"""

#print(type(args[0]))

#for arg in args:
#	print(arg)


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', multiple=True, help='The person to greet.')

def hello(count, name):
	"""Simple program that greets NAME for a total of COUNT times."""
	for x in range(count):
		#click.echo('Hello %s!' % name)
		#click.echo(name)
		print(list(name))


if __name__ == '__main__':
	hello()

