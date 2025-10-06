#---Imperial to Metric Conversion---#

#--Get the Inputs--->
# 1. Input for tons
# 2. Input for stones
# 3. Input for pounds
# 4. Input for ounces
tons = ()

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
# print
#------Input--------
tons = int(input("Enter the number of imperial tons: "))
stones = input("Enter the number of stones: ")
pounds = float(input("Enter the number of pounds: "))
ounces = float(input("Enter the number of ounces: "))

