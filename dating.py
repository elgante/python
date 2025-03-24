years = 0
months = 7
days = 25

# Let's write some code to generate
# a gift recommendation!
#
# The variables above give the length of the relationship in
# number of years, months, and days. Add some code below to
# print a gift recommendation based on these values:
#
# - If you've been dating for at least 4 years, give them a
#   dog ("dog").

# - If you've been dating for at least 1 year but less than
#   4 years, give them a watch ("watch").

# - If you've been dating for at least 6 months but less than
#   1 year, give them concert tickets ("concert tickets").

# - If you've been dating for at least a day but less than 6
#   months, give them candy ("candy").

# - If aren't actually dating, go big or go home: give them
#   a yacht to sail away together ("yacht").
#
# Note that no matter what, you should only print one gift.


# Add your code here!
# - If you've been dating for at least a day but less than 6
#   months, give them candy ("candy").

if years >= 4:
    print("dog")

elif years < 4 and years >= 1:
    print("watch")

elif months >= 6 and years < 1:
    print("concert tickets")

elif (months < 6 and months > 0) or days > 0:
    if not years:
        print("candy")

elif months == 0 and years == 0 and days == 0:
    print("yacht")
