def loading_bar(loaded):
    print_list = []
    for percent in range(10):
        if percent < loaded/10:
            print_list.append("%")
        else:
            print_list.append(".")
    return "".join(print_list)


entry = int(input())
if entry == 100:
    print("100% Complete!")
    print(f"[{loading_bar(entry)}]")
else:
    print(f"{entry}% [{loading_bar(entry)}]")
    print("Still loading...")

