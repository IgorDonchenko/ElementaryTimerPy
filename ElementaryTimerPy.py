# # Import asctime and sleep modules from time library
import time
import os

def foo():
	aggr = '#'

	while True:
		print(time.asctime())
		time.sleep(1)
		os.system('cls')

foo()