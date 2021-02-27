import csv
from pathlib import Path


load_path = Path('Resources/budget_data.csv')
output_path = Path('budget_analysis.txt')


total_months = 0
month_of_change = []
net_change_amount_list = [] 
greatest_increase_amount = ['', 0] 
greatest_decrease_amount = ['', 99999999]
total_net_amount = 0


with open(load_path) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)

    row_one = next(reader)
    total_months += 1
    total_net_amount += int(row_one[1])
    prev_net_amount = int(row_one[1]) 
    
    for row in reader:
        total_months += 1
        total_net_amount += int(row[1])
        
        net_amount_change = int(row[1]) - prev_net_amount
        prev_net_amount = int(row[1]) 
        net_change_amount_list += [net_amount_change]
        month_of_change += [row[0]] 
        
        if net_amount_change > greatest_increase_amount[1]:
            greatest_increase_amount[0] = row[0] 
            greatest_increase_amount[1] = net_amount_change
            
        if net_amount_change < greatest_decrease_amount[1]:
            greatest_decrease_amount[0] = row[0]
            greatest_decrease_amount[1] = net_amount_change

average_change = round(sum(net_change_amount_list) / len(net_change_amount_list),2)


print('Financial Analysis')
print('-----------------------------------------------------')
print(f'Total Months: {total_months} months')
print(f'Total Profit/Loss: $ {f"{total_net_amount:,}"}')
print(f'Average Change in Budget: $ {f"{average_change:,}"}')
print(f'Greatest Increase in Profits: on {greatest_increase_amount[0]} at $ {f"{greatest_increase_amount[1]:,}"}')
print(f'Greatest Decrease in Profits: on {greatest_decrease_amount[0]} at $ {f"{greatest_decrease_amount[1]:,}"}')