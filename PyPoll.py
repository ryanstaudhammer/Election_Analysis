# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to load a file from a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0
#Candidate Options
candidate_options =[]
#Declare empty dictionary
candidate_votes ={}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    for row in file_reader:
        #Add total vote count
        total_votes +=1

        #Print the candidate name from each row
        candidate_name = row[2]

        #So we don't duplicate names
        if candidate_name not in candidate_options:
            # Add candidates' names
            candidate_options.append(candidate_name)
            # Initialize count to zero
            candidate_votes[candidate_name] = 0
        #Begin adding votes
        candidate_votes[candidate_name] +=1
#Determine the percentage of votes for each candidate by looping
#Iterate through the candidate list
for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes=candidate_votes[candidate_name]
    #calculate the percentage
    vote_percentage=float(votes)/float(total_votes)*100
    #print candidate name and percentage
    print(f"{candidate_name}: received {vote_percentage :,.1f} % of the vote.")


#Print the candidate vote dictionary
print(candidate_votes)


#3. Print total votes
print(total_votes)


















