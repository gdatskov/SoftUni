from Error_handling.custom_error_classes import MustContainAtSymbolError, InvalidDomainError, NameTooShortError

valid_domains = ["com", "bg", "org", "net"]

while True:

    email = input()

    if len(email.split("@")) != 2:
        raise MustContainAtSymbolError("Email must contain exactly one '@' symbol")
    else:
        username, website = email.split("@")

    if len(username) < 4:
        raise NameTooShortError("Name must be at least 4 characters")

    if len(website.split(".")) != 2:
        raise InvalidDomainError("Domain must be separated by exactly one '.' symbol (in this case)")
    else:
        website_name, domain = email.split(".")

    if domain not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    print("Finally a free text homework!")