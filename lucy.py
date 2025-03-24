mystery_string = "Lucy"

# Above we've created a variable called mystery_string. Write
# some code that will print the first letter of the string on
# the first line, the first two letters on the second line,
# the first three letters on the third line, etc., until it
# prints the entire string on the last line.
#
# For example, if the string was "Lucy", then the output would
# be:
#
# L
# Lu
# Luc
# Lucy
#
# Hint: to print without automatically starting a new line,
# include the text end="" inside the print statement's
# parentheses. For example, print("Hello", end="") will print
# the word "Hello" without starting a new line afterward. So,
# calling it twice would print "HelloHello" on one line
# instead of two lines.

for i in range(len(mystery_string)):
    print(mystery_string[:i + 1])
