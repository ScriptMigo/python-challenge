# PyBank Homework

"""
  * Your task is to create a Python script that analyzes the records to calculate each of the following:
  ** The total number of months included in the dataset
  ** The net total amount of "Profit/Losses" over the entire period
  ** The average of the changes in "Profit/Losses" over the entire period
  ** The greatest increase in profits (date and amount) over the entire period
  ** The greatest decrease in losses (date and amount) over the entire period

  * As an example, your analysis should look similar to the one below:

  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  
  * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""

# Import required libaries
import os
import csv

# Variable definitions
netTotal  = 0
avgTotal  = 0

# Set path to CSV
#csvPath = os.path.join(r"Resources", "budget_data.csv")
csvPath = r"C:\Users\unhea\Documents\Bootcamp\GT-ATL-DATA-PT-12-2019-U-C\Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"

# Open CSV
with open(csvPath, newline="") as csvFile:
  # Set header row
  csvHeader = next(csvFile)
  
  # Create empty list to hold values returned from the csv (this is needed in order to use len() to get the row count)
  csvData   = []
  changes   = []
  
  # Loop over the CSV
  for row in csvFile:
    # Clean up the values, concat, and add to csvData list
    csvData.append(int(row.split(",")[1]))
    # Add values together to get net result
    netTotal = netTotal + int(row.split(",")[1])

# Loop the string list to do the average calculation for the changes
row = 1
while row < len(csvData):
  # Get the current value and subtract from the previous value, unless the row is the first (0)
  avgTotal = avgTotal + int(csvData[row])-int(csvData[row-1])
  # Append the change amount to the changes list for value evaluation
  changes.append(int(csvData[row])-int(csvData[row-1]))
  row += 1

#print(avgTotal)
#print(len(csvData))

# Set totalMonths variable to length of csvData
totalMonths = len(csvData)
# Calculate average change (we remove one from the total months to account for the first row not being included in the avg)
avgChange = avgTotal / (totalMonths-1)

largestChange   = max(changes)
with open(csvPath, newline="") as csvFile:
  next(csvFile)
  for row in csvFile:
    if int(largestChange) == int(row.split(",")[1]):
      print(row.split(",")[0])
    else:
      print("Not Found")

smallestChange  = min(changes)



print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {totalMonths}')
print(f'Average Change: {avgChange}')
print(f'Greatest Increase in Profits: {largestChange}')
print(f'Greatest Decrease in Profits: {smallestChange}')



