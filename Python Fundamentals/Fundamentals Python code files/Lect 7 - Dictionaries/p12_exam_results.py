results = {}
submissions = {}
banned = []

while True:
    entry = input()

    if entry == "exam finished":
        break

    if "banned" in entry:
        banned.append(entry.split("-")[0])
        continue

    username, language, points = entry.split("-")
    points = int(points)

    if username not in results.keys():
        results[username] = [points]
    else:
        results[username].append(points)

    if language not in submissions.keys():
        submissions[language] = 1
    else:
        submissions[language] += 1


print("Results:")
for user, result in results.items():
    if user not in banned:
        print(f"{user} | {max(result)}")

print("Submissions:")
for lang, subms in submissions.items():
    print(f"{lang} - {subms}")
