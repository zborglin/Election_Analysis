# Election_Analysis
Python Application

## Project Overview
A Colorado Board of Elections employee requested completion the following taks to audit a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate received.
5. Calculate the percentage of votes each candidate won.
6. Determine the winner of the election based on popular vote.

## Resources
- Data Sources: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were "369,711" votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received "23.0%" of the vote and "38,855" number of votes
  - Diana DeGette received "73.8%" of the vote and "272,892" number of votes
  - Raymon Anthony Doane received "3.1%" of the vote and "11,606" number of votes
- The winner of the election was:
  - Diana DeGette, who received "73.8%" of the vote and "272,892" number of votes.
-Here is the txt file output that may be used cross-platform:
![PyPoll Election Analysis Algorithm: Txt File Output](https://github.com/zborglin/Election_Analysis/blob/main/analysis/election_results_output.png)

## Challenge Overview
A deeper dive into the voter data reveals differences in county voter turnout rates. This request requires the following additional tasks:

1. Calculate the total number of votes cast in each county
2. Calculate the voter turnout for each county (%)
3. Determine which county had the highest voter turnout
## Challenge Summary
The analysis of the voting data by county shows that:
-The counties were:
  -Jefferson
  -Denver
  -Arapahoe
 -The county results were:
  -Jeferson County received 38,855 ballots
  -Denver County received 306,055 ballots
  -Arapahoe County received 24,801 ballots
 -The county with the highest voter turnout:
  -Denver
 ## Election Audit Summary
 This script enables an efficient and precise election analysis that can be configured to securely analyze all election data in the country. There are a few elements to this technology that enable is capability to meet the diverse needs of the different voting districts:
 -Efficiency: the algorithm is built for speed computing and can easily handle large amounts of data
 -Column driven database structure: any election data that is organized with CSV format can be accomodated by this tool. To give an example, the image below shows where in the code you can assign the target columns in the election data file
 ![Configurable Column-Based Analysis](https://github.com/zborglin/Election_Analysis/blob/main/analysis/column_info.png)
 -Complete Information Customization: There are no limits to the types of data and calculations you may implement within the script. If you want to add categorical information to describe additional data factors you may add them to the analysis. For example, you can add information regarding state election information, the congressional voting results, the funding received by each candidate, or the party affiliation. In addition, you may had any calculations to the results in order to provide the analytics that best represent the essential information. For example, you might be interested in supplementing the analysis to include the electoral votes associated with the popular vote or an analysis of the distribution of voting times relative to election day to see if voters turnout earlier in some districts. 
 
