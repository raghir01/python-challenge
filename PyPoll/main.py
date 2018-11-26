import os
import csv

path = os.path.join("Resource", "election_data.csv")

# Read in the CSV file
with open(path) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    candidate_dict = {}

    total = 0
    winning_votes = 0
    winner = ""

    for row in csvreader:
        candidate = row[2]
        total += 1
        if candidate not in candidate_dict:
            candidate_dict[candidate] = 1.0
        else:
            candidate_dict[candidate] = candidate_dict[candidate] + 1.0
            if winning_votes < candidate_dict[candidate]:
                winning_votes = candidate_dict[candidate]
                winner = candidate

    print("Election Results                    ")
    print("------------------------------------")
    print("Total Votes: {}".format(total))
    print("------------------------------------")

    for name, votes in candidate_dict.items():
        percentage = round((votes / total) * 100, 3)
        print("{}: {}% ({})".format(name, percentage, votes))
    print("------------------------------------")
    print("Winner: {}".format(winner))
    print("------------------------------------")





