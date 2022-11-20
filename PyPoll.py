# the data we need to retrieve
# 1. total number of votes cast
# 2. a complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote
#file_to_load = 'resources/election_results.csv'
#Open the election results and read the file
#with open(file_to_load) as election_data:


# Add our dependencies.
#import csv
#import os
# Assign a variable to load a file from a path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#using the open() function with the "w" mode we will write data to the file
#open(file_to_save, "w")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
#    file_reader = csv.reader(election_data)
#print each row in the CSV file
#for row in file_reader:
#    print(row)
# 
# 
#Read and print the header row.
#    headers = next(file_reader)
#    print(headers)
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)