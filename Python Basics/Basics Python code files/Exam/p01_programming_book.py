page_cost = float(input())
cover_cost = float(input())
paper_print_discount_percent = int(input())
designer_cost = float(input())
paid_by_team_percent = int(input())

pages = 899
covers = 2

initial_cost = page_cost*pages + covers*cover_cost
cost_with_discount = initial_cost*(1 - paper_print_discount_percent/100)
cost_with_designer = cost_with_discount + designer_cost
leftover_cost_after_team_help = cost_with_designer * (1 - paid_by_team_percent/100)

print(f"Avtonom should pay {leftover_cost_after_team_help:.2f} BGN.")
