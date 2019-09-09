import csv
import os

file_load = os.join("Resources", "election_data.csv")
file_output = os.path.join("Desktop")

vote_total = 0

candidates = []
candidates_votes = {}
winner = ""
winner_votes = 0 

with open(file_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
    
        vote_total = vote_total + 1 
        name = row[2]
        if name not in candidates:
            candidates.append(name)
            candidates_votes[name] = 0 
            candidates_votes[name] = candidates_votes[name] + 1 
with open(file_output, "w") as txt_file:
    results = (
        f'Election Results\n'
        f'------------\n'
        f'Total Votes: {vote_total}\n'
        f'------------------\n')
print(results, end="")


for candidate in candidates_votes:
    votes = candidates_votes.get(candidate)
    vote_percent = float(votes) / float(vote_total) * 100
    if (votes > winner_votes):
        winner_votes = votes
        winner = candidate
        vote_output = f'{candidate}: {vote_percent:.3f}% ({votes})\n'
print(vote_output, end="")


Winning_Candidate_Sum = (
f'----------------------\n'
f'Winner: {winner}\n'
        )
print(Winning_Candidate_Sum)
