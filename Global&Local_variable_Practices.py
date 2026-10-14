cups_sold = 200 #initiate global variable
def update_sales():
    cups_sold = 250 # initiate local variable
    print(cups_sold) # display local variable
update_sales()

print(cups_sold) # display global variable
print("List of Daily Orders")
daily_orders = [120, 150, 180, 90, 200]

daily_revenue = list(map(lambda x:x*5, daily_orders))# calculate daily Revenue with fixed price of $5
# calculating the total revenue
total_revenue = 0 
for sale in daily_revenue:
    total_revenue += sale
# computing the day wth the highest order and revenue
Highest_order = max(daily_orders)
busiest_day_revenue = max(daily_revenue)

print("List of Daily Revenue")
print(daily_revenue)

print("Total Revenue")
print("$",total_revenue)

print("The day with the busiest order and it revenue")
print("Order",Highest_order,"Highest revenue",busiest_day_revenue)
