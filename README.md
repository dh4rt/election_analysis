# **Election Analysis**

## **Project Overview**
A State level employee of the Colorado Board of Elections has contracted me to perform an audit on the results of a race
for a local Congressional seat. This audit's goals where to provide a clear insight into the results of the most recent
election. The BoE stated that this is a routine request, and this was simply to corroborate the results that they had
gotten. This audit was broken down in to two distinct sections. 

The first seeking to confirm the results of the election in terms of the winning candidate and their share of the votes 
throughout the counties within the district. To do that I started by calculated the total number of votes cast, this 
allowed me to set a benchmark to know if my code was returning incorrect results. The second goal was to compile a list
of all candidates that received votes and number of votes each one received, part of that second goal was to determine
what percentage of the total vote each candidate received. This gave us all the information needed to determine who won
the election based on the popular vote.

The second section of the audit was focused on a county-by-county vote percentage. Since it was established during the
first section of the audit what the total number of votes for the entire district was I was instructed to ascertain
what each counties significance in the election was. This analysis showed what percentage of the total each county
individually represented. This allowed me to show which county was the population and turnout leader for the district.


## **Resources**
The resources required for this project included:

A data set provided by the BoE found here:
Python 3.7.6
Visual Studio Code 1.73
The code, which is partially refactored from code provided by the BoE, is listed here:

## **Summary**
The BoE has directed me to provide short answers in built point format to help readers quickly glean results.

-To count the number of ballots cast in the election I first needed to start where all good total counts begin.
at zero this was done with one line of code: `total_votes = 0` this code states that the "vote bucket" is empty.
Then I declare some variables that will be discussed later until you get to the code in line 45 
'total_votes = total_votes + 1' which tells the program that since the count starts at zero to treat the left
side of the equation as the portion to solve for. The `+ 1` tells the system to count another vote for each row
that it encounters since all the ballots included in this count are free from flaws. This code brought us to a
final count of 369,711 total votes.

-A breakdown of the number of votes and percentage of the total fell clearly along population numbers.
Since this district includes the largest city in the state which is surrounded by largely rural counties it 
makes a good deal of sense that the vote share was as follows:
1. Denver 82.8%
2. Jefferson 10.5%
3. Arapahoe 6.7%

-The county with the largest number of votes is unsurprisingly the county with the largest percentage, Denver
with a vote count of 306,055 votes.

-There were three candidates on the ballot in this election, their party affiliation has been scrubbed because
it is an unnecessary point in this analysis. The candidates will be listed as they are presented in the data
with their percentage share and total votes received in parentheses:
1. Charles C. Stockham 23.0% (85,213)
2. Diana DeGette: 73.8% (272,892)
3. Raymon A. Doane: 3.1% (11,606)

-The winning candidate by every metric is Diana DeGette with 272,892 votes which represented an astounding 73.8%
of the total vote.

## **Election Audit Summary**
### **Plus Future Uses**
This code provides a great framework for other congressional districts within the state to use for their own 
means going forward, I encourage the Board to continuously work on this code to add more features where they
might be helpful. The foundation laid by this code has two obvious potential uses to me but for totally
different, but not independent uses. The first use that I feel could be useful would be to provide a full
county by county breakdown of each candidates returns, for instance, we know that Mr. Doane had the smallest
turnout of the candidates listed but where did his support come from? It could have been from any one of the
counties. Meanwhile what about Congresswoman Elect DeGette? Did all of her support come from Denver County?
It is certainly possible given how much of the vote share came from there. But it would be helpful to know
when setting up her field offices. The other addition I think that could be made would be if/when Colorado
adopts Ranked Choice Voting, a program base such as this is not difficult to construct some additional lines
to show a tally of the total votes each candidate gets for each place on the ballot. Adding both of these
capacities should the Board need to would provide tremendous insight into the voting preferences of the
constituents.









