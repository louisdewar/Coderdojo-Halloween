# Define the jokes variable with two joke dictionaries in it.
jokes = [{
    'question': 'Why didn\'t the mummy have any friends?',
    'punchline': '(Because he was wrapped up in himself!)'
},{
    'question': 'What road has the most ghosts haunting it?',
    'punchline': '(A dead end)'
}]

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
