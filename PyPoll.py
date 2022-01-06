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
#winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

#save the result to a text file
with open(file_to_save,"w") as txt_file:

    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")
    print(election_results, end="")

    #save the final vote count to the text file
    txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping
    #Iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes=candidate_votes[candidate_name]
        #calculate the percentage
        vote_percentage=float(votes)/float(total_votes)*100
    #Determine winning vote count and candidate
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #Determine winning candidate, count, and percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage 
            winning_candidate = candidate_name

    #Print winning results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

















