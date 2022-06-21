def age_assignment(*args, **kwargs):
    text = [f"{name} is {kwargs[name[0]]} years old." for name in sorted(args)]
    return "\n".join(text)



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))