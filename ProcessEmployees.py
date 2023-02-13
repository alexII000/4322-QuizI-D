"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file


infile = open("employee_data.csv", "r")
sales = csv.reader(infile, delimiter=",")
next(sales)

# create an empty dictionary
csr_dict = {}

# use a loop to iterate through the csv file
for row in sales:
    first_name = row[1]
    last_name = row[2]
    old_salary = row[5]
    salary = float(row[5]) * 1.1

    full_name = first_name + " " + last_name

    csr_dict[full_name] = salary

    # check if the employee fits the search criteria

    print(f"Manager Name: {full_name} Current Salary: ${old_salary}")

print()
print("=========================================")
print()

for row in sales:
    infile = open("employee_data.csv", "r")
sales = csv.reader(infile, delimiter=",")
next(sales)
    print(f"Manager Name: {full_name} New Salary: ${salary}")
# iternate through the dictionary and print out the key and value as per printout

print(f"")
