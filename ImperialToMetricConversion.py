#---Imperial to Metric Conversion---#

#--Get the Inputs--->
# 1. Input for tons
# 2. Input for stones
# 3. Input for pounds
# 4. Input for ounces

#--Required Formula----
#--total ounces = 35840 * tons + 224 * stone + 16 * pounds + ounces
#--total kilos = total ounces / 35.274
#--metric tons = Int(kilos/1000)

#---Calculation--
# 1. totalOunces = (35840 * tons) + (224 * stones) + (16 * pounds) + ounces
# 2. totalKilos = totalOunces / 35.274
# 3. metricTons = int(totalKilos / 1000)
# 4. remainingKilos = int(totalKilos % 1000)
# 5. grams = (totalKilos - (metricTons * 1000 + remainingKilos)) * 1000

#---Output-----
# print results

#------Input--------
tons = int(input("Enter the number of tons: "))
stones = float(input("Enter the number of stones: "))
pounds = float(input("Enter the number of pounds: "))
ounces = float(input("Enter the number of ounces: "))

# Required Formula---
totalOunces = 35840 * tons + 224 * stones + 16 * pounds + ounces
totalKilos = totalOunces / 35.274

#--Convert to ounces--
totalOunces = (35840 * tons) + (224 * stones) + (16 * pounds) + ounces

#--Convert ounces to kilos
totalKilos = totalOunces / 35.274

#--Analysing metric tons, kilos and grams---#

# the operator // rounds to whole numbers (integars)
metricTons = int(totalKilos // 1000)

# the operator % returns the remaining integar value after getting the metric tons
remainingKilos = int(totalKilos % 1000) 
grams = (totalKilos - (metricTons * 1000 + remainingKilos)) * 1000

#<-----Output--------->
print()
print("Imperial to Metric Conversion")
print()
print("Enter the number of tons: {0}".format(tons))
print("Enter the number of stones: {0}".format(int(stones)))
print("Enter the number of pounds: {0}".format(int(pounds)))
print("Enter the number of ounces: {0}".format(int(ounces)))
print()
print("The metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.".format(metricTons, remainingKilos, grams))
print()
