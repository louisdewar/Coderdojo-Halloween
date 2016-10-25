import sys

def get_jokes():
    try:
        # Opening 'jokes.txt'. The mode is 'r' and tells python that we want to read.
        file = open('jokes.txt', 'r')
    except IOError: # If there is an error opening the file
        # Print a message to our users
        print('Could not find the jokes.txt file')
        # Exit the program
        sys.exit()

    # Read the file and get the lines
    lines = file.read().splitlines()

    # Loop through each line of the file
    for line in lines:
        # Split the line into columns (which are defined by commas if you remember back to CSV formatting)
        columns = line.split(',')

        # Do some error checking to ensure that the columns are set up right
        if len(columns) == 2:


    # Close the file as we are done using it
    file.close()

# Loop through the jokes making the variable joke become each element of the array
for joke in jokes:
    # Print the question
    print(joke['question'])

    # Wait for user to hit enter
    raw_input()

    print(joke['punchline'])

    # Again wait for user to hit enter
    raw_input()

    # Print two blank lines to seperate the jokes
    print('\n\n')
