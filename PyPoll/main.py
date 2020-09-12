import os
import csv

# Define import and export file paths
election_csv = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("analysis", "output.txt")

# -------------------------------------------------------- 
with open(election_csv) as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    header = next(election_data)
    # Define initial variables
    total_count = 0
    candidates = []
    can_count = [0, 0, 0, 0, 0, 0]
    winner = 0

    for row in election_data:
        if row[0] != "":
            total_count += 1
        if row[2] not in candidates:
            candidates.append(row[2])
                # for row[2] in candidates:
    # for x in range(len(candidates)):
    #     can_count.append(0)
        can_index = candidates.index(row[2])
        can_count[can_index] += 1

# -------------------------------------------------------- 
    # Output file
    file = open(output_file, "w") 
    file.write("Election Results")
    file.write("\n----------------------------")
    file.write("\nTotal Votes: " + str(total_count))
    file.write("\n----------------------------")
    
    for i in range(len(candidates)):
        if int(can_count[i]) > winner:
            winner = int(can_count[i])
            can_winner = candidates[i]
        percent = float(can_count[i])/float(total_count) * 100

        # Print summary of each candidate
        file.write(f"\n{candidates[i]}: {percent:.3f}% ({str(can_count[i])})")
    
    file.write("\n----------------------------")
    file.write("\nWinner: " + can_winner)
    file.write("\n----------------------------")