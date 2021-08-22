# analysis of the profit/loss
import csv
import os
budget_data_csv = os.path.join( 'Resources', 'budget_data.csv')
with open(budget_data_csv, 'r') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    header=next(csv_reader)
    # Declaring empty variables and empty lists
    row=0
    totalprofit=0
    averagechange=0
    gincrease=0
    gincreasemonth=''
    gdecrease=0
    gdecreasemonth = ''
    month=[]
    profit=[]
    difference=[]
    k=0
    x=1
    m=0
    # to make three different lists for months, profit and profit difference
    for i in csv_reader:
        row=row+1
        totalprofit=totalprofit+int(i[1])
        month.append(i[0])
        profit.append(i[1])        
        x=float(i[1])-float(k)
        difference.append(x) 
        k=i[1] 
    x=0
    # to find out greatest increase in the given range of profits
    for x in range(85):
        if float(difference[x]) > m:            
            gincrease=difference[x]
            gincreasemonth=month[x]
            m=difference[x]
    # to find out the greatest decrease in the give range of profits
    for x in range(86):
        if float(difference[x]) <m:
            gdecrease=difference[x]
            gdecreasemonth=month[x]
            m=difference[x]
    # to find out average change in months
    averagechange=(sum(difference)-difference[0])/85
    # printing output in terminal
    print('Financial Analysis')
    print('---------------------')
    print('Total Months:',row)
    print('Total Profit ',totalprofit)    
    print('Average  Change: ', averagechange)          
    print('Greatest Increase in Profits: ', gincrease, gincreasemonth)        
    print('Greatest decrease in profits ', gdecrease, gdecreasemonth)
# exporting result to external source as text file
results_txt=os.path.join('Analysis', 'Results.txt')
output = open(results_txt,'w')
output.write(f'Financial Analysis\n')
output.write(f'---------------\n') 
output.write(f'Total Months: {row}\n')   
output.write(f'Total Profit {totalprofit} \n')
output.write(f'Average change: {averagechange}\n')
output.write(f'Greatest Increase in profits: {gincrease}  {gdecreasemonth}\n')
output.write(f'Greatest decrease in profits: {gdecrease}  {gdecreasemonth}\n')