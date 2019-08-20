# Import asctime and sleep modules from time library

from time import asctime, sleep

# Display current time on screen

while True:
    print(asctime())
	sleep(1)              #
	print('\u001b[2A')    #
	