# Dependencies
import csv
import os

# Set root path
path = 'python-challenge'

# Set path to Data CSV
csvPath = os.path.join(path, "PyParagraph/Resources", "paragraph.txt")

with open(csvPath, newline="") as csvFile:
  # Set header row
  csvHeader = next(csvFile)

  print(csvFile)