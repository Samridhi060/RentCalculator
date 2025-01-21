# Author : Samridhi Gupta
# Date : 21-01-2025
# Project : Rent Calculator

# Thing to do:
# Total Rent
# Total food ordered for spending
# Electricity Bill
# Charge per unit
# Person living in the house

Rent = int(input("Total Rent: "))
food = int(input("Total food ordered: "))
electricity_bill = int(input("Electricity Bill: "))
charge_per_unit = int(input("Charge per unit: "))
people = int(input("Person living in the house: "))

Total_Electricity = electricity_bill * charge_per_unit
Total = Rent + food + Total_Electricity
Per_person = Total / people

print(f"Total amount to be paid by per person is {Total}")