import os
import csv

total_num_votes = 0
candidates = {}
candidates = dict()


csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     #print(csvreader)

     for i in csvreader:
        total_num_votes +=1
        candidates = {"name": i[2]}
        candidates["name"] = i[2]

print(f'{candidates["name"]}')
total_num_votes = total_num_votes-1
print("Election Results")
print("-------------------")
print(f"Total Votes: {total_num_votes}")
print("-------------------")

#print(f"Total profits: {total_profits_list}")
#print(f"Total profits: {total_profit}")
#print(f"Average change: {average_change}")
#print(f"Greatest Increase in Profits: {greatest_increase_profit}")
print("-------------------")
#print(f"Greatest Decrease in Profits: {greatest_decrease_profit}")
        