# PyPoll Homework

"""
  * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
  * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
  *     The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that 
  *     analyzes the votes and calculates each of the following:
  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote.

  * As an example, your analysis should look similar to the one below:

  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  
  In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""
# Required modules
import os
import csv

# Open text file for writing
outFile = open(r"C:\temp\MyFile.txt","w+") 

# Define variables
candidates = []

# Set path to CSV
#csvPath = os.path.join(r"Resources", "election_data.csv")
csvPath = r"C:\Users\spdow\Documents\Bootcamp\GT-ATL-DATA-PT-12-2019-U-C\Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"

# Open CSV
with open(csvPath, newline="") as csvRows:
  csvHeader = next(csvRows)
  
  # Get the vote count
  totalVotes = sum(1 for csvRow in csvRows)

  # Loop rows in CSV file
  with open(csvPath, newline="") as csvRows:
    csvHeader = next(csvRows)

    for csvRow in csvRows:
        # Define the current candidate
        candidate = csvRow.split(',')[2]
        # Check to see if candidate has been defined
        if candidate not in candidates:
            # if not yet defined, add to candidates list
            candidates.append(candidate)

outFile.write("Election Results\n")
outFile.write("---------------------\n")
outFile.write(f"Total Votes: {totalVotes}\n")
outFile.write("---------------------\n")

print("Election Results")
print("---------------------")  
print(f"Total Votes: {totalVotes}")
print("---------------------")

# Set winner count to 0
winnerCount = 0

# Loop over list of candidates, gathering votes for each one
for candidate in candidates:
  voteCount = 0
  currentCandidate = candidate.rstrip('\n\r')
  with open(csvPath, newline="") as csvRows:
    csvHeader = next(csvRows)

    for csvRow in csvRows:
      if (csvRow.split(',')[2] == candidate):
        # Add to candidates count
        voteCount = voteCount + 1
  outFile.write(f"{currentCandidate}: {round((voteCount / totalVotes)*100,2)}% ({voteCount})\n")
  print(f"{currentCandidate}: {round((voteCount / totalVotes)*100,2)}% ({voteCount})")

  if voteCount > winnerCount:
    winnerCount = voteCount
    winner = currentCandidate

outFile.write("---------------------\n")
outFile.write(f"Winner: {winner}\n")
outFile.write("---------------------")

print("---------------------")
print(f"Winner: {winner}")
print("---------------------")
  