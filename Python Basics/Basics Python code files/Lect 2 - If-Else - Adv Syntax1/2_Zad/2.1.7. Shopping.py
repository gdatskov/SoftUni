budget = float(input())
gpus = int(input())
cpus = int(input())
rams = int(input())

gpu_price = 250
cpu_price = gpu_price*gpus*.35
ram_price = gpu_price*gpus*.1

total = gpu_price * gpus + cpu_price*cpus  + ram_price*rams

if gpus > cpus:
    total = total*.85

if budget>=total:
    print(f"You have {budget-total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total-budget:.2f} leva more!")