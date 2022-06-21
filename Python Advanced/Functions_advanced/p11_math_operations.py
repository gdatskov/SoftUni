from collections import deque


def math_operations(*args, **kwargs):
    args = deque(args)
    dekargs = deque(kwargs)     # from deq - key - args

    while args:
        number = args.popleft()

        if dekargs[0] == "a":
            kwargs["a"] += number
        elif dekargs[0] == "s":
            kwargs["s"] -= number
        elif dekargs[0] == "d" and number != 0:
            kwargs["d"] /= number
        elif dekargs[0] == "m":
            kwargs["m"] *= number

        dekargs.append(dekargs.popleft())

    sort = [f"{k}: {v:.1f}" for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
    return "\n".join(sort)



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))
