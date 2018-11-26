import os
import csv

path = os.path.join("Resource", "budget_data.csv")

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

outfile_path = os.path.join("Resource", "budget_out.txt")
with open(outfile_path, "w") as out_file:
    out_file.write("                  Financial Analysis                  \n ")
    out_file.write("-------------------------------------------------------\n")
    out_file.write("Total Months: {}\n".format(total_numof_months))
    out_file.write("Total: ${}\n".format(round(net_amount, 2)))
    out_file.write("Average  Change: ${}\n".format(round(net_amount / total_numof_months, 2)))
    out_file.write("Greatest Increase in Profits: {} (${})\n".format(greatest_profit_month, greatest_profit))
    out_file.write("Greatest Decrease in Profits: {} (${})\n".format(greatest_loss_month, greatest_loss))

    print("                  Financial Analysis                   ")
    print("-------------------------------------------------------")
    print("Total Months: {}".format(total_numof_months))
    print("Total: ${}".format(round(net_amount, 2)))
    print("Average  Change: ${}".format(round(net_amount / total_numof_months, 2)))
    print("Greatest Increase in Profits: {} (${})".format(greatest_profit_month, greatest_profit))
    print("Greatest Decrease in Profits: {} (${})".format(greatest_loss_month, greatest_loss))

