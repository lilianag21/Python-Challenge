# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_prof = 0 
previous_profit_loss = 0
prof_loss_change = 0
prev_loss = 0
avg_change = 0
greatest_increase = [' ', 0]
greatest_decrease = [' ', 99999]

# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader) 

  # Process each row of data
    for row in reader:

        # Track the total

        total_months += 1
        total_prof += int(row[1])

        # Track the net change

        prof_loss_change = int(row[1]) - prev_loss
        prev_loss = int(row[1])

        # Calculate the greatest increase in profits (month and amount)

        if(prof_loss_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = prof_loss_change

        # Calculate the greatest decrease in losses (month and amount)

        if(prof_loss_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = prof_loss_change


# Calculate the average net change across the months

avg_change = (total_prof/total_months,2)

# Generate the output summary

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_prof}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]}(${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]}(${greatest_decrease[1]})")

# Print the output

output = (
    f"\nFinancial Analysis\n"
    f"------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_prof}\n"
    f"Average Change: {avg_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]}(${greatest_increase[1]}\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]}(${greatest_decrease[1]}\n")

# Write the results to a text file

print(output)
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
