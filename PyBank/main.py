import os #to ensure all os can read and open the file
import csv #to ensure the program can read the csv file

#cd Resources/
budget_data = os.path.join("Resources", "budget_data.csv")
analysis = os.path.join("analysis", "analysis.txt")

#open and read the budget csv file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csvheader = next(csvreader)

    #lists for storing the data
    profit_and_loss = []
    months = []

    #reading through each row of the csv file and adding them to the list
    for row in csvreader:
        months.append(row[0])
        profit_and_loss.append(int(row[1]))

    #finding the change in revenue with list comprehension
    delta_rev = [(int(profit_and_loss[value]) - int(profit_and_loss[value - 1])) for value in profit_and_loss for value in range(1, len(profit_and_loss))]

    #finding total number of months
    tot_months = len(months)

    #finding the average revenue change
    avg_rev = sum(delta_rev) / len(delta_rev)

    #finding the largest increase in revenue
    greatest_inc = max(delta_rev)
    greatest_inc_mon = months[delta_rev.index(greatest_inc) + 1]

    #finding the largest decrease in revenue
    greatest_dec = min(delta_rev)
    greatest_dec_mon = months[delta_rev.index(greatest_dec) + 1]

    #printing the results
    print(f"Financial Analysis")
    print(f"---------------------------------------------------------------------")
    print(f"Total Months: {tot_months}")
    print(f"Total: ${sum(profit_and_loss)}")
    print(f"Average Change: ${round(avg_rev, 2)}")
    print(f"Greatest Increase in Profits: {greatest_inc_mon} $({greatest_inc})")
    print(f"Greatest Decrease in Profits: {greatest_dec_mon} $({greatest_dec})")

with open(analysis, 'w') as file:
    file.write(f"Financial Analysis\n")
    file.write(f"---------------------------------------------------------------------\n")
    file.write(f"Total Months: {tot_months}\n")
    file.write(f"Total: ${sum(profit_and_loss)}\n")
    file.write(f"Average Change: ${round(avg_rev, 2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest_inc_mon} $({greatest_inc})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_dec_mon} $({greatest_dec})\n")




    

        







