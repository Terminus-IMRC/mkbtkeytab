#!/usr/bin/env python3
import sys

table=[[-1 for y in range(2)]for x in range(0xE7+1)]

def outputTable():
	for f in range(0xE7+1):
		print('\t{%d,\t%d},\t/* %02d */'%(table[f][0], table[f][1], f))
	print('\t{%d,\t%d}\t/* %02d */'%(table[0xE7][0], table[0xE7][1], 0xE7))

def processNormalKeyLine(l):
	table[l[0]][0]=l[1]
	table[l[0]][1]=l[2]

def main():
	while True:
		try:
			s=input()
		except EOFError:
			break

		if len(s) == 0 or s[0] == '#':
			continue

		l=s.split()
		if len(l) != 3:
			print("Error. len of the line \"%s\" is not 3. Skipping"%(s), file=sys.stderr)
		else:
			try:
				l[0]=int(l[0], base=10)
				l[1]=int(l[1], base=10)
				l[2]=int(l[2], base=10)
			except ValueError:
				print("On line \"%s\""%(s), file=sys.stderr)
				print("There are some invalid value.", file=sys.stderr)
				exit(1)

			processNormalKeyLine(l)

	print('int8_t table_normal_keys[%d][2]={'%(0xE7+2))
	print('\t/* rows and columns */')
	print('\t/* Note that -1 means not-implemented */')
	outputTable()
	print('};')

if __name__=='__main__':
	main()
