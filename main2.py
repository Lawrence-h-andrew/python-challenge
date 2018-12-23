import os
import csv
pollCSV = os.path.join('..', 'election_data.csv')


def getPoll(pollCSV):
    "Total Number of votes cast, do I need to 'delete' the first row or make it read from the 2nd line?"
with open(pollCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Same as wrestling functions opening lines
    # now use a counter, starts at zero, adds one to itself
    for row in csvreader:
        count = 0
        count = count + 1
            #"A Complete list of candidates who received votes"
        CandidateList.append(row[2])
    for A in set(CandidateList):
        UniqueCandidate.append(A)
        #finds candidate unique values
        B = CandidateList.count(A)
        VoteCount.append(B)
        #adds candidate names to list
        C = (B/count)*100
        VotePercent.append(C)
        #calculated percent values with simple math formula
WinnerVoteCount = max(VoteCount)
winner = UniqueCandidate[VoteCount.index(winnerVoteCount)]

print(f"Election Results")
print(f"----------------------")
print(f"Total Votes:  {str(count)}")
print(f"----------------------")
print(f"Khan: " {str(C)} str{B})
        "Correy " {str(C)} str{B})
        "Li : " {str(C)} str{B})
        "O'Tooley " {str(C} str{B})
        "-----------------------")
print(f"Winner: " {str(winner)} )

#"Now I have to convert the output printed to a text file..."   
Textfile = open("getPoll.txt", "w+")