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

#Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis
    #print(election_data)
    file_reader = csv.reader(election_data)
    
    #print the header row
    headers = next(file_reader)
    print(headers)
    

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    #Write some data to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")


#Close the file.
#election_data.close()
#outfile.close()
#file_to_save.close()