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
csvPath = r"C:\Users\spdow\Documents\Bootcamp\GT-ATL-DATA-PT-12-2019-U-C\Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"

outFile = open(r"C:\Users\spdow\Documents\Bootcamp\My Repositories\python-challenge\PyBank\Resources\financial_analysis.csv","w+")

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
    csvData.append([row.split(",")[0],int(row.split(",")[1])])
    # Add values together to get net result
    netTotal = netTotal + int(row.split(",")[1])

# Loop the string list to do the average calculation for the changes
row = 1
while row < len(csvData):
  # Get the current value and subtract from the previous value, unless the row is the first (0)
  avgTotal = avgTotal + int(csvData[row][1])-int(csvData[row-1][1])
  # Append the change amount to the changes list for value evaluation
  changes.append([str(csvData[row][0]),int(csvData[row][1])-int(csvData[row-1][1])])
  row += 1

#print(avgTotal)
#print(len(csvData))

# Set totalMonths variable to length of csvData
totalMonths = len(csvData)
# Calculate average change (we remove one from the total months to account for the first row not being included in the avg)
avgChange = avgTotal / (totalMonths-1)

largestChange   = max(changes)


smallestChange  = min(changes)

topValue = 0
botValue = 0
botMonth = ""
topMonth = ""

for currentRow in changes:
  if int(topValue) < int(currentRow[1]):
    topValue = currentRow[1]
    topMonth = currentRow[0]
  elif botValue > currentRow[1]:
    botValue = currentRow[1]
    botMonth = currentRow[0]

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {totalMonths}')
print(f'Total: ${netTotal}')
print(f'Average Change: ${round(avgChange,2)}')
print(f'Greatest Increase in Profits: {topMonth} (${topValue})')
print(f'Greatest Decrease in Profits: {botMonth} (${botValue})')

outFile.write('Financial Analysis\n')
outFile.write('----------------------------\n')
outFile.write(f'Total Months: {totalMonths}\n')
outFile.write(f'Total: ${netTotal}\n')
outFile.write(f'Average Change: ${round(avgChange,2)}\n')
outFile.write(f'Greatest Increase in Profits: {topMonth} (${topValue})\n')
outFile.write(f'Greatest Decrease in Profits: {botMonth} (${botValue})\n')