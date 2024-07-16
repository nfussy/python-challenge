import os #to ensure all os can read and open the file
import csv #to ensure the program can read the csv file

#cd Resources/
election_data = os.path.join("Resources", "election_data.csv")
analysis = os.path.join("analysis", "analysis.txt")

#open and read the budget csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    #lists for storing the data
    ballot = []
    candidate_list = []
    
    #dictionary to hold totals of votes for candidates
    votes = {}

    #finding endrow
    for row in csvreader:
        ballot.append(row[0])

        #if the candidate is not in the candidate_list, then add to list and start the running total
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            #needed to start the addition of votes towards each candidate
            votes[row[2]] = 0

        votes[row[2]] = votes[row[2]] + 1

    #variables to hold the winning amount of votes and winning candidate
    winner_tot = 0
    winner = ""

    #printing the results into the terminal
    print(f"Election Results")
    print(f"---------------------------------------------------------------------")
    print(f"Total Votes: {len(ballot)}")
    print(f"---------------------------------------------------------------------")
    
    #for loop that runs the calculation of the votes for each candidate in the list of candidates
    for row[2] in votes:
        tot_vote = votes[row[2]]

        #finding the percent of votes the candidate received over the total amount of votes
        percent_vote = (float(tot_vote) / float(len(ballot) - 1)) * 100

        #calculation for the winner
        if tot_vote > winner_tot:
            winner_tot = tot_vote
            winner = row[2]
        totals = f"{row[2]}: {round(percent_vote, 3)}% ({tot_vote})\n"
        print(totals)
    
    print(f"---------------------------------------------------------------------")
    print(f"Winner: {winner}")
    print(f"---------------------------------------------------------------------")

#writing the results into the analysis.txt file in the analysis folder
with open(analysis, 'w') as file:
    file.write(f"Election Results\n")
    file.write(f"---------------------------------------------------------------------\n")
    file.write(f"Total Votes: {len(ballot)}\n")
    file.write(f"---------------------------------------------------------------------\n")

    #no need to calculate the winner twice
    for candidate in votes:
        tot_vote = votes[candidate]
        percent_vote = (float(tot_vote) / float(len(ballot) - 1)) * 100

        totals = f"{candidate}: {round(percent_vote, 3)}% ({tot_vote})\n"
        file.write(totals)
    
    file.write(f"---------------------------------------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"---------------------------------------------------------------------\n")