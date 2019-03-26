
data = [
{"first" : "125", "last":"168"},
{"first" : "142", "last":"120"},
{"first" : "109", "last":"108"},
{"first" : "97", "last":"89"},
{"first" : "91", "last":"20"},
{"first" : "40", "last":"45"},
{"first" : "245", "last":"249"},
{"first" : "387", "last":"386"},
{"first" : "123", "last":"247"},
{"first" : "12", "last":"6"},
{"first" : "4", "last":"17"},
]


print("First".ljust(9, " ") +  "Last".ljust(9, " ") + "Variance".ljust(10, " ") +  "Percent In Change" + '\n')
firstTotal = 0
secondTotal = 0
varainceTotal = 0
changePercentTotal = 0

for obj in data:
  firstNum =  int(obj['first'])
  lastNum = int(obj['last'])
  firstTotal += firstNum
  secondTotal += lastNum
  variance = firstNum - lastNum
  changePercent = variance / firstNum  * 100


  if variance < 0:
    varianceString = "(" + str(abs(variance)) + ")"
  else:
    varianceString = str(variance)      

  print(str(firstNum).ljust(9, " ") +  str(lastNum).ljust(9, " ") + varianceString.ljust(10, " ") +  str(round(changePercent, 2)) + '\n')

varainceTotal = firstTotal - secondTotal
changePercentTotal = varainceTotal / firstTotal * 100
print("Totals")
print("First".ljust(9, " ") +  "Last".ljust(9, " ") + "Variance".ljust(10, " ") +  "Percent In Change" )
print(str(firstTotal).ljust(9, " ") +  str(secondTotal).ljust(9, " ") + str(varainceTotal).ljust(10, " ") +  str(round(changePercentTotal, 2)) + '\n')

