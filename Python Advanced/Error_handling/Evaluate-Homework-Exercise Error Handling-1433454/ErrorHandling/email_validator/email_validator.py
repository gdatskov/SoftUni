import custom_exceptions

valid_domains = ['.com', '.bg', '.org', '.net']
while True:
    line = input()
    if line == 'End':
        break

    email_parts = (line.split('@'))
    username = email_parts[0]
    if len(email_parts) != 2:
        raise custom_exceptions.MustContainAtSymbolError('"Email must contain @')

    if len(username) < 5:
        raise custom_exceptions.NameTooShortError('Name must be more than 4 characters')

    domain = f'.{email_parts[1].split(".")[1]}'

    if domain not in valid_domains:
        raise custom_exceptions.InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
