company_users = {}

while True:
    entry = input()
    if entry == "End":
        break
    company, user = entry.split(" -> ")
    if company not in company_users.keys():
        company_users[company] = [user]
    else:
        if user not in company_users[company]:
            company_users[company].append(user)

for company, users in company_users.items():
    print(company)
    for user in users:
        print(f"-- {user}")
