import csv
from pathlib import Path


menu_path = Path('Resources/menu_data.csv')
sales_path = Path('Resources/sales_data.csv')
output_path = Path('ramen_report.txt')


menu = []
sales = []
report ={}
row_count = 0


with open(menu_path) as menu_data:
    menu_reader = csv.reader(menu_data)
    menu_header = next(menu_reader)
    
    for row in menu_reader:
        menu.append(row)
        
with open(sales_path) as sales_data:
    sales_reader = csv.reader(sales_data)
    sales_header = next(sales_reader)
    
    for row in sales_reader:
        sales.append(row)
        
        
for sales_row in sales:
    sales_item = sales_row[4] 
    qty = sales_row[3]   
    
    if sales_item not in report:
        report[sales_item] = {
            'Ramen Sold': 0, 
            'Revenue': 0, 
            'COGS': 0, 
            'Profit': 0,
        }
        
    if sales_item in report:
        report[sales_item]['Ramen Sold'] += int(qty)
        
    for menu_row in menu:
        menu_item = menu_row[0]
        px = menu_row[3]
        cost = menu_row[4]
    
        if sales_item == menu_item:
            report[menu_item]['Revenue'] += (int(px) * int(qty))
            report[menu_item]['COGS'] += (int(cost) * int(qty))    
            
            
for item, value in report.items():
     
    for key in value:
        
        cogs = report[item]['COGS']
        revenue = report[item]['Revenue']
        
        if key == 'Profit':
            report[item][key] = revenue - cogs
            
            
print('Ichiban Ramen Report:')
print('-----------------------------------------------------')
for key in report:
    print(f'{key} {report[key]}')