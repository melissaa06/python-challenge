import os
import csv

budget_data_csv = os.path.join("Resources","budget_data.csv")

total_profit_loss = 0
total_months = 0
previous_profit_losses = None
total_profit_losses_change = 0
max_profit_increase = float('-inf')
max_profit_increase_date = ""
min_profit_decrease = float('inf')
min_profit_decrease_date = ""

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Count the total number of months included in the dataset

    for row in csv_reader:
        total_months += 1

    #Sum the net total amount of "Profit/Losses" over the entire period
        profit_losses = int(row[1])
        total_profit_loss += profit_losses
            
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        if previous_profit_losses is not None:
            profit_losses_change = profit_losses - previous_profit_losses
            total_profit_losses_change += profit_losses_change
            
    # The greatest increase in profits (date and amount) over the entire period
            if profit_losses_change > max_profit_increase:
                max_profit_increase = profit_losses_change
                max_profit_increase_date = row[0]

    # The greatest decrease in profits (date and amount) over the entire period
                if profit_losses_change < min_profit_decrease:
                    min_profit_decrease = profit_losses_change
                    min_profit_decrease_date = row[0]
             
        previous_profit_losses = profit_losses
    average_profit_losses_change = round((total_profit_losses_change / (total_months - 1)),2)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " ,total_months)
print("Total:", total_profit_loss)
print("Average Change: $", average_profit_losses_change)
print("Greatest Increase in Profits:", max_profit_increase_date,"($",max_profit_increase,")")
print("Greatest Decrease in Profits:", min_profit_decrease_date,"($",min_profit_decrease,")") 