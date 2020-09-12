import os
import csv 
from datetime import datetime

# Define import and export file path
state_ab_py = os.path.join("Resources", "us_state_abbrev.py")
employee_csv = os.path.join("Resources", "employee_data.csv")
output_file = os.path.join("analysis", "output.txt")

# Import dictionary of US states and abbreviations
abb = eval(open(state_ab_py,).read())

# -------------------------------------------------------- 
with open(employee_csv) as csvfile:
    employee_data = csv.reader(csvfile, delimiter=",")
    header = next(employee_data)
    # Define blank lists
    ids = []
    first_name = []
    last_name = []
    dob = []
    ssn = []
    state = []
    long_state = []

    for row in employee_data:
        ids.append(row[0])
        # Find names from data and split to first and last name
        name = row[1].split(" ")
        first_name.append(name[0])
        last_name.append(name[1])
        # Read in the date with 'datetime' and re-format
        old_date = datetime.strptime(row[2],'%Y-%m-%d') 
        dob.append(old_date.strftime('%m/%d/%Y'))
        ssn.append("***-**" + row[3][-5:])
        # Match state names to abbreviations from imported dict
        state.append(abb[row[4]])

# Zip lists together to new dataframe
new_struct = zip(ids, first_name, last_name, dob, ssn,state)

# -------------------------------------------------------- 
# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    export = csv.writer(datafile)
    export.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    export.writerows(new_struct)