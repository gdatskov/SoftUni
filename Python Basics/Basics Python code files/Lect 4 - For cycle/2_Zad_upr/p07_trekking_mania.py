trekker_groups = int(input())
total_trekkers = 0
musala_trekkers = 0
montblanc_trekkers = 0
kilimanjaro_trekkers = 0
k2_trekkers = 0
everest_trekkers = 0

for trekkers in range(trekker_groups):
    people_in_group = int(input())
    total_trekkers += people_in_group
    if people_in_group <= 5:
        musala_trekkers += people_in_group
    if 5 < people_in_group <= 12:
        montblanc_trekkers += people_in_group
    if 12 < people_in_group <= 25:
        kilimanjaro_trekkers += people_in_group
    if 25 < people_in_group <= 40:
        k2_trekkers += people_in_group
    if 40 < people_in_group:
        everest_trekkers += people_in_group

print(f"{musala_trekkers/total_trekkers*100:.2f}%")
print(f"{montblanc_trekkers/total_trekkers*100:.2f}%")
print(f"{kilimanjaro_trekkers/total_trekkers*100:.2f}%")
print(f"{k2_trekkers/total_trekkers*100:.2f}%")
print(f"{everest_trekkers/total_trekkers*100:.2f}%")
