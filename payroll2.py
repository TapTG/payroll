"""
Chapter 4 Practice Project
Program: payroll2.py
Author: Teri  06.28.23

Payroll application that reads employee data from a text file and outputs payroll info in tabular format.
"""

# Input phase
fileName = input("Please enter the name of the employee payroll file that you wish to  use: ")

# Processing phase
data = open(fileName, "r")

# Output phase
print()
print("%-18s%7s%7s%10s" % ("Last Name", "Wage", "Hours", "Earnings"))
print("-" * 43)

# Loop through the file data line by line. Split up the data from each line. Place each component  into tabular format.
for line in data:
	# break the line into individual string values
	dataArray = line.split()
	# extract the last name from that array and store it
	name = dataArray[0]
	# extract the wage from the array, convert it to a float and store it
	wage = float(dataArray[1])
	# extract the hours from the array, convert it to a float and store it
	hours = float(dataArray[2])
	# next, calculate the earnings and store it
	earnings = wage * hours
	# output the employee's info in tabular format
	print("%-18s%7.2f%7.2f%10.2f" % (name, wage, hours, earnings))

# final sign off  message and dummy prompt
input("\nEnd of file, press ENTER to exit.")