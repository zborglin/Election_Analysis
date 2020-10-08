# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:58:57 2020

@author: borglz1
"""

# The data we need to retrieve
# The total number of votes cast
# a complete list of candidates who received cotes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Initialize candidate name list
candidate_options = []
# Initialize a dictionary
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis
    #print(election_data)
    file_reader = csv.reader(election_data)
    
    #print the header row
    headers = next(file_reader)
    #print(headers)
    
    #For each row in the csv file
    for row in file_reader:
        #print(row)
        total_votes += 1
        
        #print candidate name for each row
        candidate_name = row[2]
        
        #Add candidate name to the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            #track candidate's vote count
            candidate_votes[candidate_name]=0
            
        #add a vote to the candidate's count
        candidate_votes[candidate_name] += 1
    
    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        
        #Add title and total votes to text file
        election_results = (
            f"\nElection Results\n"
            f"-------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------\n")  
        print(election_results, end="")
        #save the final vote count to the text file.
        txt_file.write(election_results)                  
        
        # Print the total votes
        #print(total_votes)
        
        #Calculate  the vote percentages
        #Iterate through the candidate list
        
        for candidate_name in candidate_votes:
                #Retrieve vote count of a candidate
                votes = candidate_votes[candidate_name]
                #calculate the percentage of votes
                vote_percentage = float(votes)/ float(total_votes)*100
                #print candidate name and percentage of votes
                #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                candidate_results = (
                    f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                
                #print each candidate's voter count and percentage to the terminal
                print(candidate_results)
                
                #save the candidate results to our text file
                txt_file.write(candidate_results)
                
                #determine if the votes is greater than the winning count
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                    #If  true then set winning_count = votes and winning_percent =
                    #vote_percentage
                    winning_count = votes
                    winning_percentage = vote_percentage
                    #And, set the winning_candidate equal to the candidate's name
                    winning_candidate = candidate_name
                    #print(winning_candidate_summary)
                #print th ewinning candidates results to the terminal
                            #Print out the winning candidate, vote count and percentage to terminal
        winning_candidate_summary = (
                f"--------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"--------------------------\n")
        print(winning_candidate_summary)
            
            # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)



    

    #print the candidate list
    #print(candidate_options)
    
    #Print the candidate vote dictionary
    #print(candidate_votes)
            
    # Using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:

    #Write some data to the file
    #txt_file.write("Arapahoe\nDenver\nJefferson")


#Close the file.
#election_data.close()
#outfile.close()
#file_to_save.close()