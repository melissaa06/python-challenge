import os
import csv

budget_data_csv = os.path.join("Resources","election_data.csv")

candidate_votes = {}
total_votes = 0
results = []

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    next(csv_reader)  
    
    for row in csv_reader:
        candidate = row[2]  
        #The total number of votes cast
        total_votes += 1
        #The total number of votes each candidate won
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

for candidate, votes in candidate_votes.items():
    #The percentage of votes each candidate won
    percentage = round(((votes / total_votes) * 100),2)
    results.append((candidate, percentage, votes))

#The winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

print("Election Results")
print("-------------------------")
print("Total Votes:",total_votes)
print("-------------------------")
for candidate, percentage, votes in results:
    print(candidate,":",percentage,"% (",votes,")")

print("-------------------------")
print("Winner:", winner)
print("-------------------------")