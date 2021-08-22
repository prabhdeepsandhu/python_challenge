import csv
import os
pypoll_csv=os.path.join('Resources', 'election_data.csv')
with open(pypoll_csv, 'r') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter= ',')
    header=next(csv_reader)
    totalvotes=0
    a=0 # to count votes for Khan
    b=0 # to count votes for Correy
    c=0 # to count votes for Li
    d=0 # to count votes for O'Tooley

    for i in csv_reader:
        totalvotes=totalvotes+1
        if i[2] == 'Khan':
            a=a+1
        elif i[2] == 'Correy':
            b=b+1
        elif i[2] == 'Li':
            c=c+1
        else:
            d=d+1

    # Calculation of percentages
    Khan = int(a*100/totalvotes)
    Correy = int(b*100/totalvotes)
    Li = int(c*100/totalvotes)
    Otooley = int(d*100/totalvotes)

    # Comparing to find the greatest number
    if Khan>Correy and Khan>Li and Khan>Otooley:
        winner = ('Khan', Khan)
    elif Correy>Khan and Correy>Li and Correy>Otooley:
        winner =('Correy', Correy)
    elif Li>Khan and Li>Correy and Li>Otooley:
        winner = ('Li', Li)
    else:
        winner = ('OTooley', Otooley)
    
    # final result

    print('totalvotes: ', totalvotes)
    print(a,b,c,d)
    print(winner)
Results_txt=os.path.join('Analysis', 'Results.txt')
output = open(Results_txt,'w')
output.write(f'Election Results\n')
output.write(f'-------------------\n')    
output.write(f'Total number of votes: {totalvotes}\n')
output.write('-------------------------------\n')
output.write(f'Khan wins: {Khan} percentage with {a} votes \n')
output.write(f'Correy wins: {Correy} percentage with {b} votes\n')
output.write(f'Li wins: {Li} percentage with {c} votes\n')
output.write(f'OTooley wins: {Otooley} percentage with {d} votes\n')
output.write(f'---------------------\n')
output.write(f'The Winner is: {winner}\n' )
output.write('\n-----------------------------------------------')

    