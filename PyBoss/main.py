# Import required libaries
import os
import csv

# Define states
states = (['AL','Alabama'],['AK','Alaska'],['AZ','Arizona'],['AR','Arkansas'],['CA','California'],['CO','Colorado'],['CT','Connecticut'],['DE','Deleware'],
    ['FL','Florida'],['GA','Georgia'],['HI','Hawaii'],['ID','Idaho'],['IL','Illinois'],['IN','Indiana'],['IA','Iowa'],['KS','Kansas'],['KY','Kentucky'],
    ['LA','Louisiana'],['ME','Maine'],['MD','Maryland'],['MA','Massachusetts'],['MI','Michigan'],['MN','Minnesota'],['MS','Mississippi'],['MO','Missouri'],
    ['MT','Montana'],['NE','Nebraska'],['NV','Nevada'],['NH','New Hampshire'],['NJ','New Jersey'],['NM','New Mexico'],['NY','New York'],['NC','North Carolina'],
    ['ND','North Dakota'],['OH','Ohio'],['OK','Oklahoma'],['OR','Oregon'],['PA','Pennsylvania'],['RI','Rhode Island'],['SC','South Carolina'],['SD','South Dakota'],
    ['TN','Tennessee'],['TX','Texas'],['UT','Utah'],['VT','Vermont'],['VI','Virginia'],['WA','Washington'],['WV','West Virginia'],['WI','Wisconson'],['WY','Wyoming'])


# Set root path
path = 'python-challenge'

# Set path to Data CSV
csvPath = os.path.join(path, "PyBoss/Resources", "employee_data.csv")

# Set path to output CSV
outFilePath = os.path.join(path, "PyBoss", "new_employee_data.csv")
outFile = open(outFilePath,"w+")

# Create output file header
outFile.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")

# Open CSV
with open(csvPath, newline="") as csvRows:
    # Set header row
    csvHeader = next(csvRows)

    # Loop over each row, building the new version
    # Existing Format
    #Emp ID,Name,DOB,SSN,State

    # New format
    #Emp ID,First Name,Last Name,DOB,SSN,State
    for csvRow in csvRows:
        empID   = csvRow.split(',')[0]
        fName   = csvRow.split(',')[1].split(' ')[0]
        lName   = csvRow.split(',')[1].split(' ')[1]
        dob     = csvRow.split(',')[2].split('-')[1] + '/' + csvRow.split(',')[2].split('-')[2] + '/' + csvRow.split(',')[2].split('-')[0]
        ssn     = '***-**-' + csvRow.split(',')[3].split('-')[2]

        # Loop over state result to find abbreviation
        for state in states:
            if state[1] == csvRow.split(',')[4].rstrip('\n\r'):
                stateCode = state[0] 


        outFile.write(f"{empID},{fName},{lName},{dob},{ssn},{stateCode}\n")

      
      