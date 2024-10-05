#!/usr/bin/env python3
# Mihir Kalyanthaya
# 10/5/24
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

def fib_generator(limit):
	fib_nums=[]
	a,b=0,1
	while a < limit:
		fib_nums.append(a)
		a,b=b,a+b
	return fib_nums
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Generate Fibonacci numbers with specified limits.")
	parser.add_argument("limit", type=int, help="Upper number limit")
	parser.add_argument("output_file", type=str, help="Output file")

	args = parser.parse_args()
	limit = args.limit
	output_file = args.output_file

	fibonacci_numbers = fib_generator(limit)
	
	try:
		with open(output_file, 'w') as f: 
			for number in fibonacci_numbers:
				f.write(f"{number}\n")
	except IOError as e:
		print(f"I/O Error: {e}.")
