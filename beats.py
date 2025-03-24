beats_per_measure = 4
measures = 5

# <..> you should replace the
#number 1 with the number of the current measure. So, the first
#number in each measure will always rise.
#
#For example, instead of 1 2 3 4 1 2 3 4 1 2 3 4 (with each
#number on its own line), you'd now print 1 2 3 4 2 2 3 4 3 2 3 4,
#and so on.

#HINT: One approach would involve adding a conditional.

#Add your code here! Using the original values of the variables
#above, this will initially print the following numbers (but each
#on their own line):
#1 2 3 4 2 2 3 4 3 2 3 4 4 2 3 4 5 2 3 4

for measure in range(1, measures+1):
    print(measure)
    for beats in range(2, beats_per_measure+1):
        print(beats)
