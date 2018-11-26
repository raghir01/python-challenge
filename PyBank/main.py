import os
import csv

path = os.path.join("/Users/raghi/PycharmProjects/python-challenge/PyBank/Resource", "budget_data.csv")

# Read in the CSV file
with open(path) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    total_numof_months = 0
    net_amount = 0
    greatest_profit = 0
    greatest_loss = 0
    greatest_profit_month = ""
    greatest_loss_month = ""

    for row in csvreader:
        total_numof_months += 1
        net_amount += float(row[1])

        if float(row[1]) >= 0:
            if greatest_profit < float(row[1]):
                greatest_profit = float(row[1])
                greatest_profit_month = row[0]

        if float(row[1]) < 0:
            if greatest_loss > float(row[1]):
                greatest_loss = float(row[1])
                greatest_loss_month = row[0]

print("                  Financial Analysis                   ")
print("-------------------------------------------------------")
print("Total Months: {}".format(total_numof_months))
print("Total: ${}".format(round(net_amount, 2)))
print("Average  Change: ${}".format(round(net_amount / total_numof_months, 2)))
print("Greatest Increase in Profits: {} (${})".format(greatest_profit_month, greatest_profit))
print("Greatest Decrease in Profits: {} (${})".format(greatest_loss_month, greatest_loss))

