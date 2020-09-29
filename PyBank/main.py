import os
import csv

total_num_months = 0
total_profits_list = []
total_profit = 0.0
totalchange = 0.0
average_change = 0.0
greatest_increase_profit = 0.0
greatest_decrease_profit = 0.0

csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     #print(csvreader)
     
     for i in csvreader:

         total_num_months +=1
         total_profits_list.append(i[1])
         #totalchange= total_profits_list[i+1] - totalchange

#average_change= totalchange/(total_num_months-1)
total_profits_list.pop(0)
print(sum(total_profits_list))
#for num in total_profits_list:
        #total_profit= total_profit + num   
          
#total_num_months=total_num_months-1       

print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_num_months-1}")
print(f"Total profits: {total_profits_list}")
print(f"Total profits: {total_profit}")
print(f"Average change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_profit}")
print(f"Greatest Decrease in Profits: {greatest_decrease_profit}")
