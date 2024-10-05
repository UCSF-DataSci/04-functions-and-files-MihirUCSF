#!/usr/bin/env python3
# Mihir Kalyanthaya
# 10/5/24
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""
# You're on your own for this one. Good luck!

import argparse

def check_prime(num):
	if num <=1:
		return False
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			return False
	return True

def fib_generator(limit):
	fib_nums=[]
	a,b=0,1
	while a < limit:
		fib_nums.append(a)
		a,b=b,a+b
	return fib_nums

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Larget prime Fibonacci number.")
	parser.add_argument("limit", type=int, help="Fibonacci number upper limit.")
	
	args = parser.parse_args()
	limit = args.limit

	fibonacci_numbers = fib_generator(limit)

	largest_prime = None
	for number in fibonacci_numbers:
		if check_prime(number):
			if largest_prime is None or number > largest_prime:
				largest_prime = number
		
	if largest_prime is not None:
		print(f"Largest prime number less than {limit} is: {largest_prime}.")
	else:
		print(f"No prime fibonacci numbers less than {limit}.")

# terminal input
PS C:\Users\mihir> python "C:\Users\mihir\OneDrive\Desktop\DataSci217\Assignment4 P2.py" 50000
#output 
Largest prime number less than 50000 is: 28657.
