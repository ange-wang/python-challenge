import os
import csv

# Define file path for import and export
bank_csv = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("analysis", "output.txt")

with open(bank_csv) as csvfile:
    bank_data = csv.reader(csvfile, delimiter=",")
    header = next(bank_data)
    # Define empty lists
    month = []
    pnl = []
    change = []

    # Split the bank data to seperate lists of months and PnL
    for row in bank_data:
        month.append(row[0])
        pnl.append(int(row[1]))
    
    # Create new list of the change from each month
    change = [j-i for i, j in zip(pnl[:-1], pnl[1:])]

# -------------------------------------------------------- 
    # Calculate summary
    inc = max(change)
    dec = min(change)
    # Find correlating months of greatest increase/decrease with index function
    # +1 to shift the count by one due to the first month data
    inc_month = month[change.index(max(change))+1]
    dec_month = month[change.index(min(change))+1]
    ave_change = round(sum(change)/len(change), 2)

# --------------------------------------------------------    

# Output file
file = open(output_file, "w") 
file.write("Financial Analysis")
file.write("\n----------------------------")
file.write("\nTotal Months: " + str(len(month)))
file.write("\nTotal: $" + str(sum(pnl)))
file.write("\nAverage Change: $" + str(ave_change))
file.write("\nGreatest Increase in Profits: " + inc_month + " ($" + str(inc) + ")")
file.write("\nGreatest Decrease in Profits: " + dec_month + " ($" + str(dec) + ")")