import os
import csv

total_num_months = 0
total_profits_list = []
date_list = []

total_profit = 0.0
totalchange = int()
diff = 0.0
average_change = 0.0
greatest_increase_profit = 0
date1 = str()
greatest_decrease_profit = 0.0
date2 = str()


csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     
     for i in csvreader:
         
         total_num_months +=1
         total_profit+=int(i[1])
         total_profits_list.append(i[1])
         date_list.append(i[0])
         
for a in range(0,len(total_profits_list)-1):
     for b in range(1,len(total_profits_list)):
          totalchange+=int(total_profits_list[b])-int(total_profits_list[a])
          if int(total_profits_list[b])-int(total_profits_list[a])>greatest_increase_profit:
               greatest_increase_profit=int(total_profits_list[b])-int(total_profits_list[a])
               date1 = date_list[b]
          if int(total_profits_list[b])-int(total_profits_list[a])<greatest_decrease_profit:
               greatest_decrease_profit=int(total_profits_list[b])-int(total_profits_list[a])
               date2 = date_list[b]

average_change= totalchange/(total_num_months)
outFileName="analysis\\analysis.txt"
f = open(outFileName, "w")
f.write("Financial Analysis "
" ------------------- "
f" Total Months: {total_num_months} "
f" Total profits: ${total_profit} "
f" Average change: ${average_change} "
f" Greatest Increase in Profits: {date1}  (${greatest_increase_profit}) "
f" Greatest Decrease in Profits: {date2}  (${greatest_decrease_profit}) ")
f.close()

print("Financial Analysis ")
print(" ------------------- ")
print(f" Total Months: {total_num_months} ")
print(f" Total profits: ${total_profit} ")
print(f" Average change: ${average_change} ")
print(f" Greatest Increase in Profits: {date1}  (${greatest_increase_profit}) ")
print(f" Greatest Decrease in Profits: {date2}  (${greatest_decrease_profit}) ")
