# Append the joke to the csv file
def append(question, punchline):
    # Open the file named 'myfile.txt' in the same directory. The mode is 'a' and tells python that we want to append text to the file.
    # If the file does not exist then python will create a new one.
    file = open('jokes.csv', 'a')

    # Add joke with comma between. Also add new line which is important
    file.write(question + ',' + punchline + '\n')

    # Close the file as we are done using it
    file.close()

print('Adding a new joke!')

question = raw_input('Enter the question part of the joke: ')
punchline = raw_input('Ok, now the punchline: ')

print('Ha, ha. Very good.')
print('I\'m adding that now...')

append(question, punchline)