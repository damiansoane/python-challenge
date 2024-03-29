import csv
import os

file_load = os.join("Resources", "budget_data.csv")
file_out = os.path.join("Desktop")

month_total = 0
month_change = []
change_list = [] 
max_increase = ["", 0]
max_decrease = ["", 999999999999999]
net_total = 0 

with open(file_load) as fin_data:
    reader = csv.reader(fin_data)

    header = next(reader)

    first_row = next(reader)
    month_total = month_total + 1 
    net_total = net_total + int(first_row[1])
    prev_for_net = int(first_row[1])

    for row in reader:
        month_total = month_total + 1 
        net_total = net_total + int(first_row[1])
        net_change = int(row[1]) - prev_for_net
        prev_for_net = int(row[1])
        change_list = change_list + [net_change]
        month_change = month_change + [row[0]]

        if net_change > max_increase[1]:
            max_increase[0] = row[0]
            max_increase[1] = net_total
    
        if net_change < max_decrease[1]:
            max_decrease[0] = row[0]
            max_decrease[1] = net_total

net_avg = sum(change_list) / len(change_list)

output = (
    f'Financial Analysis\n'
    f'---------------\n'
    f'Total Months: {month_total}\n'
    f'Total: {net_total}\n'
    f'Average Change: {net_avg:.2f}\n'
    f'Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n'
    f'Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n'

)
print(output)

with open(file_out, "w") as txt_file:
    txt_file.write(output)