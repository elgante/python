cafe = "Octane"
balance = 7.5

#The variables above will
#contain a balance and a cafe name. Below are the prices of
#a cup of coffee at each of three locations:
#
# - Octane: $6
# - Galloway: $5
# - Starbucks: $4
# - Revelator: $3
# - Dunkin: $2
#
#Add some code above that will print one of the following
#two messages depending on whether the value of balance is
#high enough to buy a cup of coffee at the given cafe.
#
# - If it is sufficient, print "With [balance] dollars, I
#   can buy coffee at [cafe]"
# - If it is not sufficient, print "With [balance] dollars,
#   I cannot buy coffee at [cafe]"

if cafe=="Octane" and balance>=6:
 print ("With"+" "+str(balance)+" "+"dollars, I can buy coffee at"+" "+cafe)
elif cafe=="Galloway" and balance>=5:
 print ("With"+" "+str(balance)+" "+"dollars, I can buy coffee at"+" "+cafe)
elif cafe=="Starbucks" and balance>=4:
 print ("With"+" "+str(balance)+" "+"dollars, I can buy coffee at"+" "+cafe)
elif cafe=="Revelator" and balance>=3:
 print ("With"+" "+str(balance)+" "+"dollars, I can buy coffee at"+" "+cafe)
elif cafe=="Dunkin" and balance>=2:
 print ("With"+" "+str(balance)+" "+"dollars, I can buy coffee at"+" "+cafe)

else:
  print ("With"+" "+str(balance)+" "+"dollars, I cannot buy coffee at"+" "+cafe)
