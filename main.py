import os
import csv
"Collect Data from the CSV file saved in Python Challenge"
budgetCSV = os.path.join('..', 'Python-challenge', 'budget_data.csv')
"Now I need to define my function"
def getBudget(budgetCSV):
    "Total Months? This would be length of data row"
    totalMonths = len(budgetCSV[0])
    "Net amount over all periods of time"
    totalProfitLoss = 0
    totalProfitLoss = totalProfitLoss + int(budgetCSV[1])
    "Average changes of Profit/Loss of entire time. This wil be sum of data row 1 / total months function we did earlier!"
    AverageProfitLoss = (int(totalProfitLoss) / (totalMonths))
    "Greatest Increase in Profits so just the largest value in Profit/Loss row"
    GreatestProfit = max(int((budgetcsv[1]))
    

    print(f"Financial Analysis")
    print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"Total Months: {str(totalMonths)}")
    print(f"Total: {str(totalProfitLoss)}")
    print(f"Average Change: {str(AverageProfitLoss)}")
    print(f"Greatest Increase in Profits: Feb-2012  {str(GreatestProfit)}")
    print(f"Greatest Decrease in Profits: Sep-2013 {str(GreatestLoss)}")

