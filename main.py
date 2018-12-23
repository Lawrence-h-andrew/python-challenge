import os
import csv
"Collect Data from the CSV file saved in Python Challenge"
csvpath = os.path.join('..', '..', 'budget_data.csv')
with open(csvpath, 'w',) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    budgetCSV = [] 
    for row in csvreader:
        budgetCSV.append(row)

#"Now I need to define my function
def getBudget(budgetCSV):
    "Total Months? This would be length of data row"
    for row in csvreader:
        totalMonths += 1
        totalProfit += int(row[1])
        if int(row[1]) >= GreatestProfit:
            GreatestProfit = int(row[1])
            GreatestProfitDate = row[0]
        if int(row[1]) <= GreatestLoss:
            GreatestLoss = int(row[1])
            GreatestLossDate = row[0]
    "Net amount over all periods of time"
    totalProfit = 0
    totalProfit = totalProfit + int(budgetCSV[1])
    "Average changes of Profit/Loss of entire time. This wil be sum of data row 1 / total months function we did earlier!"
    AverageProfitLoss = (int(totalProfit) / (totalMonths))
    "Greatest Increase in Profits so just the largest value in Profit/Loss row"
    GreatestProfit = max(int((budgetcsv[1]))
#   "Greatest Decrease in Profits"
    #GreatestLoss = min(int((budgetcsv[1]))

    print(f"Financial Analysis")
    print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"Total Months: {str(totalMonths)}")
    print(f"Total: {str(totalProfit)}")
    print(f"Average Change: {str(AverageProfitLoss)}")
    print(f"Greatest Increase in Profits: Feb-2012  {str(GreatestProfit)}")
    print(f"Greatest Decrease in Profits: Sep-2013 {str(GreatestLoss)}")

"Now I have to convert the output printed to a text file..."
Textfile = open("getBudget.txt", "w+")