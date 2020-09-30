<<<<<<< HEAD
import os
import csv

total_num_votes = 0
candidates = {
        "name":["Khan","Correy","Li","O'Tooley"],
        "votes":[0,0,0,0]
}
pov1 = 0.0
vote1 = 0
pov2 = 0.0
vote2 = 0
pov3 = 0.0
vote3 = 0
pov4 = 0.0
vote4 = 0
winner = str()


csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")

     for i in csvreader:
        total_num_votes +=1
        if i[2]==candidates["name"][0]:
                vote1+=1
        if i[2]==candidates["name"][1]:
                vote2+=1
        if i[2]==candidates["name"][2]:
                vote3+=1
        if i[2]==candidates["name"][3]:
                vote4+=1

if vote1==max(vote1,vote2,vote3,vote4):
        winner=candidates["name"][0]
if vote2==max(vote1,vote2,vote3,vote4):
        winner=candidates["name"][1]
if vote3==max(vote1,vote2,vote3,vote4):
        winner=candidates["name"][2]
if vote4==max(vote1,vote2,vote3,vote4):
        winner=candidates["name"][3]


pov1=(vote1/(total_num_votes-1))*100
pov2=(vote2/(total_num_votes-1))*100
pov3=(vote3/(total_num_votes-1))*100
pov4=(vote4/(total_num_votes-1))*100


outFileName="analysis\\analysis.txt"
f = open(outFileName, "w")
f.write(
" Election Results "
" ------------------- "
f" Total Votes: {total_num_votes-1} "
" -------------------" 
f' {candidates["name"][0]}: {pov1}% ({vote1}) '
f' {candidates["name"][1]}: {pov2}% ({vote2}) '
f' {candidates["name"][2]}: {pov3}% ({vote3}) '
f' {candidates["name"][3]}: {pov4}% ({vote4}) '
" ------------------- "
f' Winner: {winner} '
" -------------------" )
f.close()

print(" Election Results ")
print(" ------------------- ")
print(f" Total Votes: {total_num_votes-1} ")
print(" -------------------" )
print(f' {candidates["name"][0]}: {pov1}% ({vote1}) ')
print(f' {candidates["name"][1]}: {pov2}% ({vote2}) ')
print(f' {candidates["name"][2]}: {pov3}% ({vote3}) ')
print(f' {candidates["name"][3]}: {pov4}% ({vote4}) ')
print(" ------------------- ")
print(f' Winner: {winner} ')
print(" -------------------" )
=======
import os
import csv

total_num_votes = 0
candidates = {
        "name":["Khan","Correy","Li","O'Tooley"],
        "votes":[0,0,0,0]
}
pov1 = 0.0
vote1 = 0
pov2 = 0.0
vote2 = 0
pov3 = 0.0
vote3 = 0
pov4 = 0.0
vote4 = 0
winner = str()


csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")

     for i in csvreader:
        total_num_votes +=1
        if i[2]==candidates["name"][0]:
                vote1+=1
        if i[2]==candidates["name"][1]:
                vote2+=1
        if i[2]==candidates["name"][2]:
                vote3+=1
        if i[2]==candidates["name"][3]:
                vote4+=1

if vote1==max(vote1,vote2,vote3,vote4):
        winner=candidates["name"][0]
if vote2==max(vote1,vote2,vote3,vote4):
        winner=candidates["name"][1]
if vote3==max(vote1,vote2,vote3,vote4):
        winner=candidates["name"][2]
if vote4==max(vote1,vote2,vote3,vote4):
        winner=candidates["name"][3]


pov1=(vote1/(total_num_votes-1))*100
pov2=(vote2/(total_num_votes-1))*100
pov3=(vote3/(total_num_votes-1))*100
pov4=(vote4/(total_num_votes-1))*100


outFileName="analysis\\analysis.txt"
f = open(outFileName, "w")
f.write(
" Election Results "
" ------------------- "
f" Total Votes: {total_num_votes-1} "
" -------------------" 
f' {candidates["name"][0]}: {pov1}% ({vote1}) '
f' {candidates["name"][1]}: {pov2}% ({vote2}) '
f' {candidates["name"][2]}: {pov3}% ({vote3}) '
f' {candidates["name"][3]}: {pov4}% ({vote4}) '
" ------------------- "
f' Winner: {winner} '
" -------------------" )
f.close()

print(" Election Results ")
print(" ------------------- ")
print(f" Total Votes: {total_num_votes-1} ")
print(" -------------------" )
print(f' {candidates["name"][0]}: {pov1}% ({vote1}) ')
print(f' {candidates["name"][1]}: {pov2}% ({vote2}) ')
print(f' {candidates["name"][2]}: {pov3}% ({vote3}) ')
print(f' {candidates["name"][3]}: {pov4}% ({vote4}) ')
print(" ------------------- ")
print(f' Winner: {winner} ')
print(" -------------------" )
>>>>>>> 3e3dac5e55fda4c53d9c18573c26ee6bbe63de57
        