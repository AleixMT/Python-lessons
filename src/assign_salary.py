employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

employees_dict = {}
for employee in employees:
    employees_dict[employee] = defaults

employees_dict["Emma"]["salary"] += 1000
print(employees_dict)

