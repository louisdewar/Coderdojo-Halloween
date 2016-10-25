#Python Joker

###Overview

In this tutorial you will make a python programme that will print out halloween themed jokes.

###Requirements

We would advise that you have done at least a little bit of python before. If you have already done a lot then there are more advance extensions later on.

- You must have `python 2` installed
- You should either have the python IDLE or a suitable text editor (see list below). Using a text editor that is not the python IDLE will require that you know how to run python files preferably from the command line (more information below).

####Running from the commandline

**NOTE:** Skip this section if you have not used the command line before.

Running python from the command line will be useful for the very advance tutorials and it will help you get a better understanding of the CLI (command line interface) which will be useful to anyone interested in computers.

You will need a decent text editor such as these:

- [Sublime text](https://www.sublimetext.com/3) (Cross platform)
- [Brackets](https://brackets.io) (Cross Platform)
- [Atom](https://atom.io/) (Cross Platform)
- [Notepad++](https://notepad-plus-plus.org/download/v7.1.html) (Windows only)

You will also need `python 2` installed and in the system `PATH`. On the installer there is an option to enable this and on mac `python 2` comes pre-installed.

To check open up your systems CLI. On mac/linux it is called terminal and on windows it is called command prompt.

To check what version you are running type:
```
python -V
```

You will hopefully get an output of `Python 2.` then a few other numbers. If the first number is 3 that you might have an issue and you should ask a mentor for help.

When you want to run a python file type `python ` followed by the relative path to that file. If you are unsure of how to do this just ask someone around you or a mentor.

####Running from the IDLE

**NOTE:** Skip this section if you are comfortable using the command line.

1. Create a new file
2. Place this code into it: `print('Hello World')`
3. Look for `Run --> Run Module` in the toolbar.
4. Save the file as prompted.
5. Check the output to ensure that it says `Hello World`.

###Getting started

Place this code into your python file and run it:

```python
input = raw_input('What is your name? ')
print('Hello ' + input)
```

**If you get an error** then you are probably running the wrong python version and you should ask for help.

###Understanding lists

When we store lists of items in computers we store them in what are called `arrays`.

Here is an example:

```python
myarray = ['a', 'b', 'c']
```

`myarray` is now a list containing three items.

**Terminology:** an item in an array is called an `element`.

###Looping over lists:

Now we have a list, so what can we do with it?

We can loop over the list which means that we go through each item in it one at a time.

The easy syntax for this is:

```python
for element in array:
    # Do something with element
```

Each time we loop around, the variable called `element` becomes the next element in the array.

Let's look at this example:

```python
# We create a list called `greetings` with these three elements
greetings = ['Hi.', 'How are you?', 'Good morning.']

# We loop over every element in `greetings` and each time the variable `greeting` (no 's' at the end) becomes one of the greetings in the list.
for greeting in greetings:
    print('Loop!')
    print(greeting)
```

Copy this code into a python file and run it.

####Extensions

Try these extensions:
1. Change the program to not print `Loop!` each time and only print the greeting
2. Add another greeting such as `Hi` or `Good afternoon`.

##Putting it all together:

####One last thing:
You will find that when putting text in quotes (`'random text'`) it is difficult when there is lots of text than goes onto more than one line.
Fortunately python has you covered with the use of tripple quotation marks.
See this example:
```python
some_other_text = '''Long winded
text that is difficult to store in just single quotes.'''

mylist = ['''text that goes onto
more than
one line''', '''Some more text that is in another element
of the list''']
```
####Back to the coding

1. Search the web for halloween themed jokes or just look at [this website] (http://www.enchantedlearning.com/jokes/topics/halloween.shtml Halloween Jokes)

2. Copy and paste two or three of the best ones into an array called `jokes`
3. Loop through each element of that array and print them out.

If you get stuck or have finished and want to look at the finished code [click here] (joker-stuck-1.py)

###Evaluation:

So you now have a method of getting jokes printed out onto a screen!
*But* there are some issues:
1. All the jokes are displayed at once, there is no time to let any sink in (comedic timing is important).
- It can be difficult to tell when a joke starts or stops.
- There is no time to let people think of the answer as they are printed at the same time.

####So how can we fix these issues?

1. We can put `raw_input()` after we print out each joke. This will require the user to hit enter before the code will continue so they can decided when they are ready to go on.
- We can place a few lines once the joke has finished. If you have never done this before it might seem a bit confusing as the code is `print('\n')`. What `\n` essentially means is `go onto a new line please...`. If we wanted more lines then we just add more `\n`. *Make sure that the `\n` goes inside quotes. It is still text, just not text that we read.*
- Finally this is the most complicated of the issues to solve. As it works currently we have an array called `jokes` and each element of that array contains both the joke and the answer. A solution would be to put the joke and answer as different elements in the array but this isn't neat.
If you asked a programmer about this solution they probably wouldn't like it as the array `jokes` should contain a bunch of `joke` elements not some combination of the joke and it's punchline. So we can use something in python called a `dictionary` which will allow us to neatly contain both the joke and the punchline seperately but as the same element in the array. If this sounds confusing try to read ahead into the next section.

###Dictionaries:

In python there is a type of object called a `dictionary`. When you think of a dictionary you think of a book where you can search for a word and then find a bunch of text about it (A.K.A. the definition of the word).

Python dictionaries work in a similar way we have a bunch of words and each one has a definition associated with it.

For example, let's say we had a `dictionary` in which we defined the word `question` as `What position does a ghost play in soccer?` and then in the same dictionary we defined the word `punchline` as `Ghoulie`. This dictionary now contains two items, `question` and `punchline`. These are called `keys` and the data they relate to (the definition) are called `values`.

Here is some code to express the dictionary we just talked about:

```python
joke = {
    'question': 'What position does a ghost play in soccer?',
    'punchline': 'Ghoulie'
}
```

Our variable `joke` is now a dictionary that contains the two items of `question` and `punchline`.

Let's abstract this a bit...

So any dictionary has the format:
```python
my_dictionary = {
    'key': 'value',
    'another_key': 'another_value',
    ...
}
```

Another thing to note is that the `value` can be any python object. It can be a number or even another dictionary the possibilities are endless.

####Accessing the data:

So now we have a dictionary called `joke` and we want to print out the punchline, how would we do that?

To access any value of the dictionary we use this format:
```python
my_dictionary['my_key']
```

Where `my_dictionary` is the name of your dictionary variable and `my_key` is the name of the key.

Let's look at one final example:

```python
jokes = [{
    'question': 'Why didn\'t the mummy have any friends?',
    'punchline': '(Because he was wrapped up in himself!)'
},{
    'question': 'What road has the most ghosts haunting it?',
    'punchline': '(A dead end)'
}]
```

The variable jokes is now an `array` of two `dictionaries`. If we wanted to get the question of the first joke we can use the code `jokes[0]['question']`. So `jokes[0]` is the first element of the array which happens to be a dictionary. That dictionary has the key `question`.

Another thing to note in that example above is the line:
```python
    'question': 'Why didn\'t the mummy have any friends?'
```
You might notice the `\'` in the middle there. You might think back to the `\n` and wonder if there is some correlation and there is. They are both called `escape characters`. By putting the `\` (backslash) infront of defined characters we can change their meaning and in the case of `\'` we are saying that we don't want to end the string there, and that we want the `'` character to be printed out how it is.

As a side note if you want to print a `\` as it is you need to "escape" it, e.g:

```python
print('\\ <- This is a backslash')
```
This will print: `\ <- This is a backslash`.

##More Coding:

So, with this information and the use of the internet can you try to fix the issues mentioned above?

If you get stuck you can look at the source code [here] (joker-stuck-2.py)

##Advance

Right now you have a static variable called `jokes` which contains all of your jokes.

When you want to add more you have to format the object correctly and it can become quite messy especially the more jokes you add.

Let's extract the issues here:
- You have to manually add each joke which is messy
- It is easy to make a formatting mistake
- It doesn't look nice in your main file

So we need a system to easily add more questions.
Can we easily add line of code to our python file to make our `jokes` dictionary bigger or smaller?

Probably not.

So where else can we store this information? In a seperate file?

What about a CSV file!

CSV stands for Comma Seperated Values and you can think of them like spreadsheets (in fact most spreadsheet programmes do, try opening a csv file in excel and it will work). All we need to do is have a new line for each element or `row` in this case and each `column` will be seperated by a comma.

Let's see an example file:

```
some joke,some punch line
another joke,another punch line
```

This represents a table like this:

Column 1 | Column 2
--- | --- | ---
some joke|some punch line
another joke|another punch line

Another thing to note is that in real CSV files there would be a line at the top that would indicate the column headers, but we don't need to worry about that.

###Creating files in python

The python syntax for creating and editing a file is:
```python
# Open the file named 'myfile.txt' in the same directory. The mode is 'a' and tells python that we want to append text to the file.
# If the file does not exist then python will create a new one.
file = open('myfile.txt', 'a')

# Append user input to the text variable

input = raw_input('What do you want to write to the file? ')

# Append the input from the user to the file and add a new line at the end
file.write(input + '\n')

# Close the file as we are done using it

file.close()
```

The next thing we need to know how to do is to read the file and then extract the csv rows and columns.

So to read the file we use:

```python
# Opening 'myfile.txt'. The mode is 'r' and tells python that we want to read.
file = open('myfile.txt', 'r')

# Read the file and print out the contents
print(file.read())

# Close the file as we are done using it
file.close()
```

So we can use this information to figure out how to use files to store and access the jokes.

This would be perfect if it wasn't for the issue that the file might not exist.
If that happens we need to handle the error otherwise python will crash and it won't be very helpful to the user.

We should print out a message like: `Could not find the jokes.txt file`

Let's see this:
```python
# We need this to nicely stop our program
# Imports typically go at the top of the file
import sys

try:
    # Opening 'jokes.txt'. The mode is 'r' and tells python that we want to read.
    file = open('jokes.txt', 'r')
except IOError: # If there is an error opening the file
    # Print a message to our users
    print('Could not find the jokes.txt file')
    # Exit the program
    sys.exit()

# Read the file and print out the contents
print(file.read())

# Close the file as we are done using it
file.close()
```

###A few more things

Before you're ready to move on to creating this yourself there are two more things we need to cover.

The first are functions.

Here is an example:

```python
# Define a function called hello() that prints out 'Hello World'
def hello():
    print('Hello World')

#Call our function called 'hello()'
hello()
```

Functions are essentially contianers for code that can be access whenever they are required. We have already used many without realising exactly what they are.

They can also take in variables called `parameters`:

```python
# Define a function called say(something) that takes in a variable and prints it out
def say(something):
    print("[COMPUTER]: " + something)

say('Hey!')
say('How are you!')
```

The paramters are seperate by commas in the brackets such as `param1, param2...`.

####Split

The next thing you need to know before you start working on your project again is the `split(string)` and `splitlines` functions.

Here is an example of both:

```python
# Define a csv formatted string.
csv_file_text = '''a,b
dsad,gas
d,23'''

# Get the lines of the file
lines = csv_file_text.splitlines()

# Loop through each line of the file
for line in lines:
    # Print out the line
    print('Line: ' + line)
    # Split the line into columns (which are defined by commas if you remember back to CSV formatting)
    columns = line.split(',')

    for column in columns:
        print('Column: ' + column)
```

Copy this code into a new python file and run it.
Make sure you understand exactly why everything is outputted the way it is.

**Bonus:**

What type of variable does `split` and `splitlines` produce?

##Back to the coding

###Task:
1. Make another python file called `add_joke.py` or something similar
    1. The file needs to ask the user to type in the question and then the punch line
    2. It should store these in variables then combine them into one called something like `joke`, there needs to be a comma seperating them
    3. Finally append the joke varialbe to a file (Make sure that there is a new line between each joke)
2. Update the origional python file
    1. It needs to read the csv file
    2. Get the lines
    3. Get the individual columns
    4. Add each column to an array called jokes
    5. Print them out as before

###Thing to keep in mind

- The CSV file should end in '.csv'. So it's full name would be something like `jokes.csv`
- The python files need to be in the same folder
- Try to seperate parts of your project into functions, but remember to not overdo it!
- If you get an issue when you try to add a joke, make sure you have only copied one line. If you add more than one line then the `raw_input` function will move on as soon as it sees one line.
- Make sure that the jokes that you are adding **do not contain commas**. Remember CSV files depend on commas, there are ways to get around this but we don't really have time to work on that.
- If you get stuck then double check the information I gave earlier and then ask others, if you get **really** stuck then you can look at the source code as mentioned below

####Source Code

If you get stuck or have finished you can take a look at the code here:
- [add_joker.py] (add_joke-stuck.py)
- [joker.py] (joker-stuck-3.py)

##Finishing off:

You have managed to get through this enourmous document and apparently still have time left, so I will set you some difficult tasks which you can choose a few to research and attempt to implement.

First things first **BACKUP EVERYTHING**. Up to this point you have done a lot of work and you might end up breaking your code so create a copy of everything you have done.

Ideas:
1. Move `add_joke.py` into the main python file.
    1. When you run the main python file it will run normally but when you run `python joker.py add` it will switch to add mode
    2. Research:
        1. You will need to look up system arguments in python.
        2. You can look up the `if __name__=='__main__':` syntax although it won't really affect what you are doing, it is just interessting.
    3. **Variation:** As a variation on that idea you can try to make `add_joke` a module which your main python file imports.
2. Add a method for allowing commas in your jokes
    1. Either have an `escape sequence` that will ignore `\,` but that can get quite difficult
    2. Look into importing a csv module that does this for you
        1. If you go down this route you should update every part of your CSV creation to use this module so there is a standard.
3. Allow adding multiple jokes at once
    1. Each time the user enters the question and the punchline, they are asked if they want to enter another `[y]es or [n]` type question
4. Add more error checking
    1. Ensure that every part of your code will know when there is an error and tell the user nicely about it. This is good practise when you are developing programs for users who don't want to deal with a big long error message with a *stack trace* (You can look that up aswell).
5. Make the software more user friendly
    1. Add some friendly messages to instruct the user how to use you tool.
6. Add an option to allow the user to make a guess to what the answer is, then tell them if they get it right.