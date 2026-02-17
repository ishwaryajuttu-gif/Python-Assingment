
annual_salary = float(input("Enter your annual salary: ")) #taking user inputs
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

current_savings = 0.0      # Initial savings is zero
ar = 0.04                   # Annual return on investment is 4% 
months = 0
#montly calculation (total)
down_payment = total_cost * 0.25 # 25% down payment from total cost
monthly_salary = annual_salary / 12
monthly_deposit = monthly_salary * portion_saved  #portion of salary saved every month

while current_savings < down_payment:
    current_savings += current_savings * (ar / 12) #adding invest return for each month
    current_savings += monthly_deposit  #adding monthly salary savings of each month to total savings
    months += 1


print(f"Number of months: {months}")
